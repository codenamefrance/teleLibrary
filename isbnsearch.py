import requests

API_URL = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'


class Book:
    def __init__ (self, bookTitle, bookAuthors, bookYear):
        self.bookTitle = bookTitle
        self.bookAuthors = bookAuthors
        self.bookYear = bookYear

def getISBNdata(isbn) -> Book:

    x = requests.get(API_URL+isbn)
    if(x.status_code!=200):
        return None

    x = x.json()


    author = x['items'][0]['volumeInfo']['authors']
    title = x['items'][0]['volumeInfo']['title']
    year = x['items'][0]['volumeInfo']['publishedDate']

    bookData = Book(title, author, year)

    return bookData
