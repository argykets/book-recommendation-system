# Book Recommendation System


This is the repository for a Book Recommendation System, a web application built with FastAPI.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- [Anaconda](https://www.anaconda.com/products/distribution) (for managing Conda environment)
- [Python](https://www.python.org/) version 3.8

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/argykets/book-recommendation-system.git
   cd book-recommendation-system

2. **Create a Conda Environment**

   ```bash
   conda create -n your_env_name python=3.8

3. **Activate Conda Environment**

   ```bash
   conda activate your_env_name

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt

5. **Run the application**

   ```bash
   uvicorn app:app --reload

6. **Access the application**

    By default, the FastAPI server runs on http://127.0.0.1:8000. You can access the API documentation (provided by Swagger UI) at http://127.0.0.1:8000/docs.


