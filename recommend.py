import numpy as np

class BookRecommender:
    def __init__(self, books, similarity_scores, pt) -> None:
        self.books = books
        self.similarity_scores = similarity_scores
        self.pt = pt

    def recommend_book(self, book_name):
        index = np.where(self.pt.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(self.similarity_scores[index].squeeze())), key=lambda x: x[1], reverse=True)[1:5]
        data = []
        for i in similar_items:
            item = []
            temp_df = self.books[self.books["Book-Title"] == self.pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Title"].values))
            item.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Author"].values))
            item.extend(list(temp_df.drop_duplicates("Book-Title")["Image-URL-M"].values))

            data.append(item)

        return data