#!/usr/bin/env python3
import requests
from Book import Book
from ReadingList import ReadingList


def get_api_items(query):
    """ Return a JSON dictionary based on user's search term. """
    while query == '' or query.isspace():
        print('You entered an empty search query.')
        query = input('What do you want to search for?\n')
    url = ('https://www.googleapis.com/books/v1/volumes?' +
           'q={}&maxResults=5').format(query)
    try:
        obj = requests.get(url).json()
    except requests.exceptions.RequestException:
        print('There was an error connecting to the Google Books API.' +
              'Please check your internet connection and try again')
        return False
    else:
        items = obj.get('items')
        if items is None:
            print("\nSorry, your search didn't return any results.")
            return False
        return items


def construct_books_array(items):
    """ Build a books array of all of the returned items """
    books = []
    for i in range(len(items)):
        books.append(Book(items, i))
        books[i].print_book()
    return books


def validate_book_choice(books):
    book_choice = input('\nEnter the corresponding number to add a book to' +
                        ' your reading list or any other key to return' +
                        ' to the main menu:\n')
    if book_choice.isdigit() and 0 < int(book_choice) <= len(books):
        return books[int(book_choice) - 1]
    return False


def main():
    reading_list = ReadingList('ReadingList.txt')
    while True:
        choice = input('\nWelcome to your reading list.' +
                       ' Please choose an option:\n\n' +
                       '1: Add a book\n2: View your reading list\n3: Exit\n')
        if choice == '1':
            items = get_api_items(input('\nWhat are you looking for?\n'))
            if items is False:
                continue
            books = construct_books_array(items)
            book = validate_book_choice(books)
            if book is False:
                continue
            reading_list.add_book(book)
        elif choice == '2':
            reading_list.view()
        elif choice == '3':
            exit()
        else:
            print("That is not a valid choice. Please choose 1, 2, or 3.\n")


if __name__ == '__main__':
    main()
