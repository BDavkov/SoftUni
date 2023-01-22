favorite_book = input()
checked_books = 0

while True:
    current_book = input()
    if current_book == "No More Books":
        print(f"The book you search is not here!\nYou checked {checked_books} books.")
        break
    elif current_book == favorite_book:
        print(f"You checked {checked_books} books and found it.")
        break
    checked_books += 1
