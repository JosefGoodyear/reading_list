#!/usr/bin/env python3
from Book import Book
from ReadingList import ReadingList


def main():
    while True:
        choice = input('Welcome to your reading list.' +
                       ' Please choose an option:' +
                       '\n1: Add a book\n2: View your reading list\n3: Exit\n')
        reading_list = ReadingList('ReadingList.txt')
        if choice == '1':
            obj = Book.get_books(input('What are you looking for?\n'))
            books = []
            for i in range(5):
                books.append(Book(obj, i))
                books[i].print_book()
            book_to_add = input('Enter the corresponding number' +
                                ' to add a book to your reading list' +
                                ' or any other key to exit:\n')
            if book_to_add.isdigit() and 0 < int(book_to_add) <= 5:
                reading_list.add_book(books[int(book_to_add) - 1])
        elif choice == '2':
            reading_list.view()
        elif choice == '3':
            exit()
        else:
            print("That is not a valid choice. Please choose 1, 2, or 3.")


if __name__ == '__main__':
    main()
