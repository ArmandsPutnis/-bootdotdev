# def get_books_text(path):
#     with open(path) as f:
#         return f.read()
#
#
# def main():
#     text = get_books_text("books/frankenstein.txt")
#     print(text)
#
#
# main()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
