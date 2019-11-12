#!/usr/bin/env python3
from Book import Book
from ReadingList import ReadingList


def main():
    choice = input("Welcome to your reading list. Please choose an option:\n" +
                   "1: Add a book\n2: View your reading list\n3: Exit\n")
    if choice == '1':
        obj = Book.get_books(input('What are you looking for?\n'))
        books = []
        for i in range(5):
            books.append(Book(obj, i))
            books[i].print_book()
    elif choice == '2':
        reading_list = ReadingList('ReadingList.txt')
        reading_list.view()
    elif choice == '3':
        exit()
    else:
        print("That is not a valid choice. Please choose 1, 2, or 3.")
        main()


if __name__ == '__main__':
    main()
