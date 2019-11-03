import requests


def search(query):
    """ Search for a keyword and return an array containing title, author and
        publisher information of the first 5 results """
    url = 'https://www.googleapis.com/books/v1/volumes?q={}'.format(query)
    obj = requests.get(url).json()
    book_list = []
    item_range = min(obj.get('totalItems'), 5)
    if item_range == 0:
        print("Sorry, your search didn't return any results.")
        exit()
    for i in range(item_range):
        book_info = obj.get('items')[i].get('volumeInfo') 
        title = book_info.get('title')
        authors = book_info.get('authors')
        publisher = book_info.get('publisher')
        book_list.append([title, authors, publisher])
    return book_list
    

def add_book():
    """ Search, choose and add a book to your reading list """
    query = input("What book are you looking for?\n")
    print(search(query))
