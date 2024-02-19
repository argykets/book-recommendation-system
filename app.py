from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np

popular_df = pickle.load(open("popular.pkl", "rb"))
pt = pickle.load(open("pt.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))
similarity_scores = pickle.load(open("similarity_scores.pkl", "rb"))

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.route("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "book_name": list(popular_df['Book-Title'].values),
        "author": list(popular_df['Book-Author'].values),
        "image": list(popular_df['Image-URL-M'].values),
        "votes": list(popular_df['Number of Ratings'].values),
        "rating": list(np.round(popular_df['Avg Rating'].values, 2))
    })

@app.get("/recommend")
async def recommend_ui(request: Request):
    return templates.TemplateResponse("recommend.html", {"request": request})

@app.post("/recommend_books")
async def recommend(request: Request, user_input: str = Form(...)):
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return templates.TemplateResponse("recommend.html", {"request": request, "data": data})
