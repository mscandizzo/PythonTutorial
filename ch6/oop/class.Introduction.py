class Point():
    x = 10
    y = 7

p = Point()
print(p.x)  # 10 (from class attribute)
print(p.y)  # 7 (from class attribute)

p.x = 12  # p gets its own `x` attribute
print(p.x)  # 12 (now found on the instance)
print(Point.x)  # 10 (class attribute still the same)

del p.x  # we delete instance attribute
print(p.x)  # 10 (now search has to go again to find class attr)

p.z = 3  # let's make it a 3D point
print(p.z)  # 3

print(Point.z)
# AttributeError: type object 'Point' has no attribute 'z'

"""
NAME SPACES
"""

class Person():
    species = 'Human'


print(Person.species)  # Human
Person.alive = True  # Added dynamically!
print(Person.alive)  # True

man = Person()
print(man.species)  # Human (inherited)
print(man.alive)  # True (inherited)

Person.alive = False
print(man.alive)  # False (inherited)

man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)  # Darth Vader

print(Person.name)
# This doesn't work. We try to access an instance attribute
# from a class. Doing the opposite works, but this will give
# the following error:
# AttributeError: type object 'Person' has no attribute 'name'

"""
SELF 
"""


class Square():
    side = 8

    def area(self):  # self is a reference to an instance
        return self.side ** 2


sq = Square()
print(sq.area())  # 64 (side is found on the class)
print(Square.area(sq))  # 64 (equivalent to sq.area())

sq.side = 10
print(sq.area())  # 100 (side is found on the instance)

"""
BASIC INHERINTANCE
"""
class A:
    label = 'a'


class B(A):
    pass  # was: label = 'b'


class C(A):
    label = 'c'


class D(B, C):
    pass


d = D()
print(d.label)  # 'c'
print(d.__class__.mro())  # notice another way to get the MRO
# prints:
# [<class '__main__.D'>, <class '__main__.B'>,
#  <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

"""
INIT
"""


class Rectangle():
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b


r1 = Rectangle(10, 4)
print(r1.side_a, r1.side_b)  # 10 4
print(r1.area())  # 40

r2 = Rectangle(7, 3)
print(r2.area())  # 21

"""
MUST NOT DO !!
NEVER DUPLICATE ATTRIBUTES!!
"""


class Book:

    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages


class Ebook(Book):

    def __init__(self, title, publisher, pages, format_):
        self.title = title
        self.publisher = publisher
        self.pages = pages
        self.format_ = format_

"""
CLASSES ARE BLUE PRINTS
ONCE CREATED THEY WILL MULTIPLY AND MUTATE
"""


class Price():
    def final_price(self, vat, discount=0):
        """Returns price after applying vat and fixed discount."""
        return (self.net_price * (100 + vat) / 100) - discount


p1 = Price()
p1.net_price = 100
print(Price.final_price(p1, 20, 10))  # 110 (100 * 1.2 - 10)
print(p1.final_price(20, 10))  # equivalent
