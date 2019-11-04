import requests


def search(query):
    """ Search for a keyword and return an array containing title, author and
        publisher information of the first 5 results """
    url = 'https://www.googleapis.com/books/v1/volumes?q={}'.format(query)
    obj = requests.get(url).json()
    books = []
    item_range = min(obj.get('totalItems'), 5)
    if item_range == 0:
        print("Sorry, your search didn't return any results.")
        exit()
    for i in range(item_range):
        book_info = obj.get('items')[i].get('volumeInfo')
        title = book_info.get('title')
        authors = book_info.get('authors')
        publisher = book_info.get('publisher')
        books.append([title, authors, publisher])
    return books


def format_books(books):
    """ Format results into strings for printing """
    formatted_books = []
    for num, book in enumerate(books):
        if book[1] is not None:
            authors = ', '.join(book[1])
        else:
            authors = 'None'
        formatted_books.append('{}: {} by {} ({})'
                               .format(num + 1, book[0], authors, book[2]))
    return formatted_books


def print_books(formatted_books):
    """ print books from user query and ask user to add a specific book """
    for book in formatted_books:
        print(book)
    book_to_add = input(
        'Enter the corresponding number to add a book to your reading list,' +
        'or any other key to exit\n')
    if book_to_add.isdigit() and 0 < int(book_to_add) <= len(formatted_books):
        return formatted_books[int(book_to_add) - 1]
    else:
        exit()


def add_to_reading_list(book, reading_list):
    """ Append book to file, creating file if necessary """
    book = book[3:]
    try:
        with open(reading_list, "a+") as f:
            f.write(book + '\n')
        print("{} was added to your reading list".format(book))
    except IOError:
        print('There was an error opening/writing to the file.' +
              ' {} was not added to your reading list'.format(book))


def add_book():
    """ Search, choose and add a book to your reading list """
    query = input("What book are you looking for?\n")
    books = search(query)
    formatted_books = format_books(books)
    book = print_books(formatted_books)
    add_to_reading_list(book, "ReadingList.txt")
