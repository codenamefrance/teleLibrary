import time
import telebot
from sql import *
from isbnscanner import *
from isbnsearch import*
import json

with open("config.json", "r") as json_data_file:
    data = json.load(json_data_file)

TOKEN = data['telegram-bot']['token']


db = dbConnect()
bot = telebot.TeleBot(TOKEN)
print(db.is_connected())

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, text='Benvenuto nella tua libreria!')

@bot.message_handler(func = lambda message : True, content_types=['photo'])
def download_image(message):
    imgs = message.photo
    # select best quality image (last one)
    photoId = imgs[len(imgs)-1].file_id
    file = bot.get_file(photoId)
    bytes = bot.download_file(file.file_path)

    with open('img.jpeg', 'wb') as destFile:
        destFile.write(bytes)
    isbn = readBarcodeImage('img.jpeg')
    if(isbn == None):
        bot.send_message(message.from_user.id, text='Immagine non valida.')
        return
    
    book_data = getISBNdata(isbn)

    if book_data is None:
        bot.send_message(message.from_user.id, text=f'Non riesco a trovare questo libro - ISBN: {isbn}')
        return
    if dbInsertBook(db, message.from_user.id, isbn):
        bot.send_message(message.from_user.id, text=f'Ho correttamente inserito "{book_data.bookTitle}" all\'interno della tua libreria.')
        return
    bot.send_message(message.from_user.id, text='Il libro è già presente nella tua libreria.')


@bot.message_handler(commands=['books'])
def getBooks(message):
    userID = message.from_user.id
    books_data = dbGetUserBooks(db, userID)
    books = list()

    for isbn in books_data:
        books.append(getISBNdata(isbn))

    text = ''
    for book in books:
        text += book.bookTitle + '\n'
    bot.send_message(userID, text=text)

while True:
    bot.infinity_polling()
    time.sleep(100)