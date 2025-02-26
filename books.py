from fastapi import FastAPI

app=FastAPI()

BOOKS=[
    {'title':'Title One', 'author':'Author One','category':'Science'},
    {'title':'Title Two', 'author':'Author Two','category':'Science'},
    {'title':'Title Three', 'author':'Author Three','category':'History'},
    {'title':'Title Four', 'author':'Author Four','category':'Math'},
    {'title':'Title Five', 'author':'Author Five','category':'Math'},
    {'title':'Title Six', 'author':'Author Two','category':'Math'},
]

# @app.get("/")
# async def get_books():
#     return {"books": ["Python", "Java", "C++"]}


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get('/books/{book_title}')
async def read_book(book_title:str):
   for book in BOOKS:
       if book.get('title').casefold()==book_title.casefold(): #casefold() is used to make the string case-insensitive or lower case
           return book