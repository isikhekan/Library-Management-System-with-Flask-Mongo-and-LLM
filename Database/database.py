from pymongo import MongoClient
import os
client = MongoClient(os.getenv('MONGODB_HOST'), int(os.getenv('MONGODB_PORT')))
db = client.book_database
categories = db.categories
books = db.books
def create_db():
    return {
        'books': books,
        'categories': categories,
    }
