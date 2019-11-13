#!/usr/bin/env python3
import requests
from Book import Book
from ReadingList import ReadingList


def get_books(query):
    """ Return a JSON dictionary based on user's search term. """
    while query == '' or query.isspace():
        print('You entered an empty search query.')
        query = input('What do you want to search for?\n')
    url = 'https://www.googleapis.com/books/v1/volumes?q={}'.format(query)
    try:
        obj = requests.get(url).json()
    except requests.exceptions.RequestException:
        print('There was an error connecting to the Google Books API.' +
              'Please check your internet connection and try again')
        exit()
    else:
        return obj


def construct_books_array(obj):
    """ build a books array of at most 5 Book objects """
    books = []
    item_range = min(obj.get('totalItems'), 5)
    if item_range == 0:
        print("Sorry, your search didn't return any results.")
        exit()
    for i in range(item_range):
        books.append(Book(obj, i))
        books[i].print_book()
    return books


def validate_book_choice(books):
    book_choice = input('Enter the corresponding number to add a book to' +
                        ' your reading list or any other key to exit:\n')
    if book_choice.isdigit() and 0 < int(book_choice) <= 5:
        return books[int(book_choice) - 1]
    exit()


def main():
    reading_list = ReadingList('ReadingList.txt')
    while True:
        choice = input('Welcome to your reading list.' +
                       ' Please choose an option:' +
                       '\n1: Add a book\n2: View your reading list\n3: Exit\n')
        if choice == '1':
            obj = get_books(input('What are you looking for?\n'))
            books = construct_books_array(obj)
            book = validate_book_choice(books)
            reading_list.add_book(book)
        elif choice == '2':
            reading_list.view()
        elif choice == '3':
            exit()
        else:
            print("That is not a valid choice. Please choose 1, 2, or 3.")


if __name__ == '__main__':
    main()
