from fastapi import FastAPI
from databases import Database

app = FastAPI()
database = Database("sqlite:///books.db")


@app.on_event("startup")
async def database_connect():
    """
    Asynchronously connects to the SQLite database 'books.db'.
    """
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    """
    Asynchronously disconnects from the SQLite database 'books.db'.
    """
    await database.disconnect()


@app.get("/")
async def read_root():
    """
    Provides a welcome message for the root path ('/').
    """
    return {"message": "Welcome to the Books API!"}


@app.get("/books/")
async def list_books():
    """
    Retrieves a list of all books from the 'books' table.
    """
    query = "SELECT * FROM books"
    return await database.fetch_all(query=query)


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    """
    Retrieves a specific book by its ID from the 'books' table.

    Args:
        book_id (int): The ID of the book to retrieve.

    Returns:
        Dictionary: The book data if found, or None if not found.
    """
    query = "SELECT * FROM books WHERE id = :book_id"
    return await database.fetch_one(query=query, values={"book_id": book_id})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
