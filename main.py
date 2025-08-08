from fastapi import FastAPI , HTTPException , Response , status
from services.select_books import fetch_all_books
from services.get_book_by_author import get_book_by_author
from schemas.book import Book
from typing import List



app = FastAPI()

@app.get('/books' , response_model=List[Book] ,tags= ["services"])
def show_books():
    try :
        rows = fetch_all_books()
        
        books = [Book(id= row[0] , title=row[1] , author = row[2] , available = row[3]) for row in rows]
        
        return books
    except Exception as e:
        raise HTTPException (status_code= status.HTTP_406_NOT_ACCEPTABLE , detail= f"some error occured{e}")
    
@app.get('/book/author/{author_name}' , response_model= List[Book] , tags=["services"])
def show_by_author(author_name : str):
    try:
        rows = get_book_by_author(author_name)
        books = [Book(id=row[0],title=row[1] , author=row[2], available=row[3]) for row in rows]
        return books
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail=f"some error occured{e}")
    
        