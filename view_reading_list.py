def view_reading_list():
    try:
        with open('ReadingList.txt') as f:
            reading_list = f.read()
        print(reading_list)
    except IOError:
        print('Your reading list could not be found.' +
              'Please name the file ReadingList.txt.')
