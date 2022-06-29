import math
from fractions import Fraction
from pprint import pprint

# Data Types:
some_var = "This is a variable now!"

# print(some_var)

some_string = "This is a string."
some_string_halfquote = 'This is a string.'
some_string_escaped = "This is a string with \"quotes in it\"."
some_string_multiline = """
This is a string.  It can have multiple lines in it, and even matching quotes like so: " " " " " ".
"""
some_string_multiline_half = '''
This is also a multiline string.
'''
some_fmt_string = "Some math numbers: {pi}, {tau}, {e}"
pyfmt_url = "https://pyformat.info/"


# print(some_fmt_string.format(
#     pi=math.pi,
#     e=math.e,
#     tau=math.tau
# ))

some_float = 0.0
some_int = 0
# print(0.1 + 0.2)
# print(Fraction(1, 10) + Fraction(2, 10))

some_true = True
some_false = False

some_dict = {
    "some key": "some value",
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau
}

# pprint(some_dict)
# print(some_dict["pi"])

some_list = [
    "They contain a bunch of items.",
    "of any data type,",
    "including other lists:",
    ["Like this!"],
    "https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range"
]

# pprint(some_list)
# some_list.append("This value was added after the list was created!")
# pprint(some_list)

some_none = None

#---------------------------------------------------------------#

# # This array represents a cyberpunk library.
books = [
    {
        "title": "Neuromancer",
        "author": "William Gibson",
        "year_published": 1984,
        "isbn": "",
        "rating": 100
    },
    {
        "title": "Snow Crash",
        "author": "Neal Stephenson",
        "year_published": 1992,
        "isbn": "978-01336162-0",
        "rating": 100
    },
    {
        "title": "Altered Carbon",
        "author": "Richard K. Morgan",
        "year_published": 2002,
        "isbn": "",
        "rating": 100
    }
]

# for book in books:
#     pprint(book)
#     print("----")
# print("This is out of the scope of the loop.")

# for idx, book in enumerate(books):
#     print(idx, book)

# for x in range(1, 11):
#     print(x)

# while len(books) < 5:
#     print("We're in a loop!")
#     books.append("")

# print("What do you think is going to happen when I run other.py?")

# def some_function():
#     print("This is in the function!")
#     return "This is the return value."

# print(some_function.__name__)
# print(some_function())

# some_lambda = lambda x, y: x + y

# print(some_lambda.__name__)
# print(some_lambda(0.1, 0.2))

# print("One string " + "another string.")
# print(" ".join(["This", 'list', "will", 'be', 'joined', 'with', 'spaces.']))

# if __name__ == "__main__":
#     print("This will only run if the file is run manually.")

# print(__name__)

# This array represents a cyberpunk library.
books = [
  # This object represents a book.
  {
    "title": "Neuromancer",
    "author": "William Gibson",
    "year_published": 1984,
    "isbn": "",
    "rating": 90,
  },
  {
    "title": "Snow Crash",
    "author": "Neal Stephenson",
    "year_published": 1992,
    "isbn": "978-01336162-0",
    "rating": 95,
  },
  {
    "title": "Altered Carbon",
    "author": "Richard K. Morgan",
    "year_published": 2002,
    "isbn": "",
    "rating": 100,
  },
  {
    "title": "Cryptonomicon",
    "author": "Neal Stephenson",
    "year_published": 1999,
    "isbn": "978-0-380-78862-0",
    "rating": 85,
  }
]

# pprint(
#     list(
#         map(
#             lambda x: x["title"] + ", " + x["author"],
#             books
#         )
#     )
# )

# pprint(
#     list(
#         filter(
#             lambda x: x["year_published"] > 1992,
#             books
#         )
#     )
# )

# print("Unsorted:")
# pprint(books)
# books.sort(key=lambda x: x["rating"])
# print("books.sort():")
# pprint(books)
# print("sorted(books):")
# pprint(sorted(books, key=lambda x: x["year_published"]))

# lipsum = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Etiam consequat dapibus mauris ut accumsan.
# Integer suscipit metus justo, eget pharetra urna eleifend ut.
# Nam eu ultrices diam. Aenean bibendum tortor sed ligula vestibulum, eu iaculis neque euismod.
# Vivamus aliquet mauris sit amet tortor scelerisque cursus.
# Nunc pretium feugiat posuere.
# Curabitur congue ligula quis luctus laoreet.
# Praesent suscipit tempor ante nec fringilla.''';

# print(lipsum.isascii())

class Book(object):
    title = None
    year_published = None
    isbn = None
    author = None
    rating = None

    def __init__(
        self,
        title=None,
        year_published=None,
        isbn=None,
        author=None,
        rating=None,
    ):
        self.title = title
        self.year_published = year_published
        self.isbn = isbn
        self.author = author
        self.rating = rating

    def __repr__(self):
        return "<Book {title} by {author}>".format(
            title=self.title,
            author=self.author
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def serialize(self):
        return {
            "title": self.title,
            "author": self.author,
            "year_published": self.year_published,
            "isbn": self.isbn,
            "rating": self.rating,
        }
    
    @staticmethod
    def deserialize(x):
        return Book(
            title=x.get("title", None),
            year_published=x.get("year_published", None),
            isbn=x.get("isbn", None),
            author=x.get("author", None),
            rating=x.get("rating", None)
        )
    

books_obj = list(
    map(
        lambda x: Book.deserialize(x),
        books
    )
)

# pprint(books)
# pprint(books_obj)

# for book in books_obj:
#     pprint(book.serialize())

# neuro = Book.deserialize(
#     books_obj[0].serialize()
# )

# neuro_copy = Book.deserialize(
#     books_obj[0].serialize()
# )

# print("Equality:", neuro_copy == neuro)
# print("Identity:", neuro_copy is neuro)

# pprint(neuro.serialize())
# pprint(neuro_copy.serialize())

# neuro.year_published = 2022

# print("Equality:", neuro_copy == neuro)
# print("Identity:", neuro_copy is neuro)

# pprint(neuro.serialize())
# pprint(neuro_copy.serialize())

# print("\n\nI've added isbns to Neuromacer and Altered Carbon.\n\n")

# books_obj[0].isbn = "9780441569595"
# books_obj[2].isbn = "9780345457684"

# for book in books_obj:
#     pprint(book.serialize())


