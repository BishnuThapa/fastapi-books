from fastapi import FastAPI,Body

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

    
@app.post('/books/create_book')
async def create_book(new_book= Body()):
    BOOKS.append(new_book)
    return BOOKS

@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)): # to find how many key values are there
        if BOOKS[i].get('title').casefold()==updated_book.get('title').casefold():# if title matches update body section means category and author section
            BOOKS[i]=updated_book
    