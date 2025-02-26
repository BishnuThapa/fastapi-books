from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'Science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'Science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'History'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'Math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'Math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'Math'},
]

# @app.get("/")
# async def get_books():
#     return {"books": ["Python", "Java", "C++"]}


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get('/books/{book_title}')
async def read_book(book_title: str):
   for book in BOOKS:
       # casefold() is used to make the string case-insensitive or lower case
       if book.get('title').casefold() == book_title.casefold():
           return book


# filter by category
@app.get('/books/')
async def read_category_by_query(category: str):
   books_to_return = []
   for book in BOOKS:
       if book.get('category').casefold() == category.casefold():
           books_to_return.append(book)
   return books_to_return
   
# books by author and category as a querystring
@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author:str,category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book) 
    return books_to_return

    
            
