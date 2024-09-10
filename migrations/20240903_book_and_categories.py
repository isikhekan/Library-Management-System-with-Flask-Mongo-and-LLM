import json
from Services.bookServices import create_book

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


keys_to_check = ['title', 'publishedDate', "longDescription"]
imported_books = load_json('amazon.books.json')

try:
    for book in imported_books:
        if not all(key in book for key in keys_to_check):
            continue
        if not book['authors'] or not book['categories']:
            continue
        else:
            print("going to import book")
            book = {
                'title': book['title'],
                'creator': book['authors'][0],
                'content': book['longDescription'],
                'category': book['categories'][0],
            }
            create_book(book, create_and_add=True)
except ValueError as e:
    print('hata', e)
