'''

A class to represent books in a database.

Is this better than a plain old dict?

'''

class Book:
    isbn = ""
    name = ""
    price = 0.0
    publisher = ""
    
a = Book()
b = Book()
c = Book()
d = Book()

a = Book()
a.isbn = "1234"
a.name = "Learn C++"
a.price = 10.0
a.publisher = "Good Books"

e = {'isbn':"test", 'name':"name"}

print(e)
