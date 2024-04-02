import requests

API_URL = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

class Book:
    def __init__ (self, bookTitle, bookAuthors, bookYear):
        self.bookTitle = bookTitle
        self.bookAuthors = bookAuthors
        self.bookYear = bookYear

def getISBNdata(isbn) -> Book:

    api_data = requests.get(API_URL+isbn)
    if(api_data.status_code!=200):
        return None

    api_data = api_data.json()
    try:
        author = api_data['items'][0]['volumeInfo']['authors']
        title = api_data['items'][0]['volumeInfo']['title']
        year = api_data['items'][0]['volumeInfo']['publishedDate']
    except KeyError:
        return None

    bookData = Book(title, author, year)

    return bookData
