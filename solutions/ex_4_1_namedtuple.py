# Define a namedtuple called Book with fields title, author, and price. Create a
# Book object and try out some of the namedtuple operations presented above on
# it. Write a function sort_books_by_price that takes a list of Book instances
# and returns a new list sorted by price.
from collections import namedtuple


Book = namedtuple("Book", "title, author, price")
my_book = Book("Brave New World", "Huxley, Aldous", 12)
print(my_book.title, my_book.price)
print(my_book._asdict())


def sort_books_by_price(books):
    return sorted(books, key=lambda b: b.price)


my_books = [
    Book("Animal Farm", "Orwell, George", 8),
    Book("Foucault's Pendulum", "Eco, Umberto", 16),
    my_book,
]
sorted_books = sort_books_by_price(my_books)
print(sorted_books)

# Create a namedtuple called Point that represents a point in a 2D space with x
# and y coordinates. Write a function distance_from_origin that takes a Point
# and calculates its distance from the origin (0,0): √(x2 + y2).

Point = namedtuple("Point", "x y")


def distance_from_origin(point):
    return (point.x ** 2 + point.y ** 2) ** 0.5


p1 = Point(2, 1)
print(distance_from_origin(p1))
