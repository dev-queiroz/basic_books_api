from fastapi import FastAPI
import sqlite3

app = FastAPI()

# The book is added through the console
title = str(input("Book's title: "))
author = str(input("Author: "))


@app.get("/add_book")
def add_book():
    """
    Adds a new book to the database.

    This endpoint accepts a POST request with the following parameters in the request body:

    - **title (str):** The title of the book (required).
    - **author (str):** The author of the book (required).

    Returns a JSON response with a success message or an error message if the book could not be added.
    """

    try:
        if not title or not author:
            return {"erro": "Title and author are required."}

        conn = sqlite3.connect("books.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            (title, author),
        )
        conn.commit()
        conn.close()

        return {"message": "Book added successfully!"}

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
