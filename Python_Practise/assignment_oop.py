"""Part 1: Basic Classes, Objects, Attributes, and Methods
Assignment 1: Simple Car Class Create a class named Car.
• It should have three attributes: make, model, and year.
• It should have a method display_info() that prints out the car's make, model,
and year in a readable format (e.g., "2020 Honda Civic").
• Create two different Car objects, assign them values for their attributes, and
call the display_info() method for each."""

class Car:
    year=0
    make, model = '', ''
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

car1 = Car()
car2 = Car()

car1.make = 'Honda'
car1.model = 'AnotherSomething'
car1.year = 2020

car2.make = 'Toyota'
car2.model = 'Something'
car2.year = 2022

car1.display_info()
car2.display_info()

print('###-----------1NO------------------>>>>>>>>>>>>')

"""Part 2: Constructors (__init__) and String Representation (__str__)
Assignment 6: Enhanced Car Class Modify the Car class from Assignment 1:
• Use an __init__ method to initialize the make, model, and year attributes
when an object is created.
• Implement an __str__ method that returns a string representation of the car,
for example, "2020 Honda Civic".
• When you print a Car object, it should now use your __str__ method. Create
a Car object and print it."""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.make} {self.make} {self.model}"

car1 = Car('Tata', 'Nexon', 2020)
car2 = Car('Mahindra', 'BE6', 2025)
print(car1)
print(car2)


print('###--------------2NO--------------->>>>>>>>>>>>')

"""Assignment 2: Book Details Create a class named Book.
• Attributes: title, author, pages.
• Method: get_summary() that returns a string formatted as: "Title: [title],
Author: [author], Pages: [pages]".
• Create an instance of Book and print its summary."""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_summary(self):
        print(f"Title: [{self.title}],Author: [{self.author}], Pages: [{self.pages}]")
b1 = Book('Story of a snake, Python', 'Sameer', 200)
b2 = Book('Story of Coffee, Java', 'Koushik', 500)
b2.get_summary()


print('###---------------3NO-------------->>>>>>>>>>>>')

"""Assignment 3: Rectangle Calculations Create a class named Rectangle.
• Attributes: length, width.
• Methods:
○ calculate_area() which returns the area (length * width).
○ calculate_perimeter() which returns the perimeter (2 * (length +
width)).
• Create a Rectangle object, calculate, and print its area and perimeter."""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        area = self.length * self.width
        return area
    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter
R1 = Rectangle(10, 20)
print(R1.calculate_area())
print(R1.calculate_perimeter())

print('###---------------4NO-------------->>>>>>>>>>>>')


"""Assignment 4: Simple BankAccount Create a class BankAccount.
• Attributes: account_holder_name, balance (initialize to 0 by default if not
provided).
• Methods:
○ deposit(amount): Adds the amount to the balance. Print a confirmation.
○ withdraw(amount): Subtracts the amount from the balance. Ensure the
balance does not go below zero. If it would, print an "Insufficient funds"
message and do not change the balance. Otherwise, print a
confirmation.
○ display_balance(): Prints the current balance.
• Create an account, perform some deposits and withdrawals, and display the
balance."""

class BankAccount:
    def __init__(self, account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print('Amount successfully deposited in ',self.account_holder_name, "account.")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print('Withdrawal process completed, please take the cash.')
        else:
            print('Insufficient funds.')
    def display_balance(self):
        print(f"Hi {self.account_holder_name}, \nYour current balance is {self.balance}")

B=BankAccount('k')
B.deposit(1100)
B.withdraw(1001)
B.display_balance()


print('###----------------5NO------------->>>>>>>>>>>>')

"""Assignment 5: Student Grades Create a class Student.
• Attributes: name, grades (this should be a list of numbers, e.g., [85, 90, 78]).
• Method: calculate_average_grade() that returns the average of the grades in
the list. If there are no grades, it should return 0.
• Create a Student object and print their average grade."""
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def calculate_average_grade(self):
        if len(self.grades) > 0:
            sum=0
            for grade in self.grades:
                sum += grade
            return sum
        else:
            return 0

someone = Student('chucha', [85,90,78])
print('Average grade is ',someone.calculate_average_grade())


print('###-----------------6NO------------>>>>>>>>>>>>')

"""Assignment 7: Point in 2D Space Create a class Point.
• It should be initialized with x and y coordinates using __init__.
• Implement __str__ to return a string like "(x, y)".
• Add a method distance_from_origin() that calculates and returns its
Euclidean distance from the origin (0,0). The formula is x2+y2
. (You can use math.sqrt from the math module).
• Create a Point object, print it, and print its distance from the origin."""
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
point = Point(3, 4)
print(f"Point: {point}")
print(f"Distance from origin: {point.distance_from_origin()}")


print('###-----------------7NO------------>>>>>>>>>>>>')

"""Assignment 8: Enhanced BankAccount with __init__ and __str__ Modify 
the BankAccount class from Assignment 4: • Use __init__ to
 initialize account_holder_name and an 
 initial balance (which should default to 0 
 if no initial balance is provided).
  • Add an __str__ method that returns a string like
   "Account Holder: [name], Balance: $[balance]". 
• Create an account and print the account object to see the __str__ output."""
class BankAccount:
    def __init__(self, account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance
    def __str__(self):
        return f"Account Holder: {self.account_holder_name}, Balance: {self.balance}"
    def deposit(self, amount):
        self.balance += amount
        print('Amount successfully deposited in ',self.account_holder_name, "account.")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print('Withdrawal process completed, please take the cash.')
        else:
            print('Insufficient funds.')
    def display_balance(self):
        print(f"Hi {self.account_holder_name}, \nYour current balance is {self.balance}")
account = BankAccount("Ramchandra", 1000)
account.withdraw(500)
account.deposit(250)
print(account)

print('###------------------8NO----------->>>>>>>>>>>>')

"""art 3: Encapsulation (Private Attributes, Getters/Setters)
Assignment 9: Employee Salary Create an Employee class.
• It should have a "Protected" attribute _salary (use a single underscore
convention).
• Initialize name and _salary using __init__.
• Provide a get_salary() method to return the salary.
• Provide a set_salary(new_salary) method that updates the salary. This
method should ensure the new_salary is a positive number; otherwise, it
should print an error and not change the salary.
• Create an employee, try to set a valid and an invalid salary, and get the
salary."""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    def get_salary(self):
        return self._salary
    def set_salary(self, new_salary):
        if new_salary>0:
            self._salary = new_salary
        else:
            print('Error: give a positive figure to update the salary.')
employee = Employee('Ramchandra', 50000000)
employee.set_salary(60000000000)
print('salary is ', employee.get_salary())


print('###----------------9NO------------->>>>>>>>>>>>')

"""Assignment 10: TemperatureConverter Create a TemperatureConverter class.
• It should store temperature internally in Celsius (e.g., as a private attribute
_celsius).
• Methods:
○ __init__(self, temp_celsius=0): Initializes with a Celsius temperature.
○ get_celsius(): Returns the temperature in Celsius.
○ set_celsius(temp_celsius): Sets the temperature in Celsius.
○ get_fahrenheit(): Converts Celsius to Fahrenheit and returns it (F = C *
9/5 + 32).
○ set_fahrenheit(temp_fahrenheit): Takes Fahrenheit, converts it to
Celsius (C = (F - 32) * 5/9), and stores it.
• Test by setting a Celsius temperature, getting Fahrenheit, then setting a
Fahrenheit temperature and getting Celsius."""


class TemperatureConverter:
    def __init__(self, temp_celsius=0):
        self.__celsius = temp_celsius
    def get_celsius(self):
        return self.__celsius
    def set_celsius(self, temp_celsius):
        self.__celsius = temp_celsius
    def get_fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32
    def set_fahrenheit(self, temp_fahrenheit):
        self.__celsius = (temp_fahrenheit - 32) * 5 / 9
temp_converter = TemperatureConverter(25)


print(f"Temperature Celsius: {temp_converter.get_celsius()}°C")
print(f"Temperature Fahrenheit: {temp_converter.get_fahrenheit()}°F")
temp_converter.set_fahrenheit(77)
print(f"Celsius to Fahrenheit: {temp_converter.get_celsius()}°C")


print('###-------------10NO---------------->>>>>>>>>>>>')

"""Assignment 11: Secure BankAccount Further modify the BankAccount class:
• Make the _balance attribute "private" (using a single underscore _balance).
• Ensure that deposit and withdraw are the only public methods that can
modify this _balance.
• The display_balance method (or __str__) should still be able to access
_balance to show it.
• Test that you cannot directly change _balance from outside the class (e.g.,
my_account._balance = 1000000 might still work due to Python's name
mangling not being true privacy, but the convention is important)."""


class BankAccount:
    def __init__(self, account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount

    def display_balance(self):
        return f"Account Holder: {self.account_holder_name}, Balance: {self.__balance}"

    def __str__(self):
        return self.display_balance()


account = BankAccount("Ramchandra", 1000)

print(account)
account.deposit(500)
print(account)
account.withdraw(200)
print(account)

account.__balance = 100000   # confusion error should appear in this line, but not occuring
print(account)


print('###-----------------11NO------------>>>>>>>>>>>>')

"""Part 4: Inheritance
Assignment 12: Animal and Dog
1. Create a base class Animal with:
○ An __init__ method that takes a name.
○ A method speak() that prints a generic sound like "Some animal sound".
2. Create a derived class Dog that inherits from Animal.
○ Its __init__ method should call the parent's __init__.
○ Override the speak() method to print "Woof!".
3. Create instances of Animal and Dog and call their speak() methods."""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some animal sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")


animal = Animal("Animal")
dog = Dog("Dog")

animal.speak()
dog.speak()


print('###----------------12NO------------->>>>>>>>>>>>')

"""Assignment 13: Vehicle, Car, and Motorcycle
1. Create a base class Vehicle with attributes make, model, year (initialized in
__init__).
2. Add a method display_info() to Vehicle that prints these common details.
3. Create a derived class Car that inherits from Vehicle.
○ Add an attribute num_doors (initialized in Car's __init__).
○ Override display_info() to print the make, model, year, AND the number
of doors.
4. Create a derived class Motorcycle that inherits from Vehicle.
○ Add an attribute engine_type (e.g., "2-stroke", "4-stroke", initialized in
Motorcycle's __init__).
○ Override display_info() to print the make, model, year, AND the engine
type.
5. Create instances of Car and Motorcycle and call their display_info()
methods."""


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.make} {self.model} {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        print(f"{self.make} {self.model} {self.year}, Doors: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_type):
        super().__init__(make, model, year)
        self.engine_type = engine_type

    def display_info(self):
        print(f"{self.make} {self.model} {self.year}, Engine Type: {self.engine_type}")


car = Car("Tata", "Safari", 2020, 4)
motorcycle = Motorcycle("Mahindra", "Bolero", 2021, "4-stroke")

car.display_info()
motorcycle.display_info()


print('###---------------13NO-------------->>>>>>>>>>>>')

"""Assignment 14: Shape, Circle, Square Area
1. Create a base class Shape.
○ It should have a method area(). In the base class, this method can simply
pass or raise a NotImplementedError (because a generic shape doesn't
have a specific area formula).
2. Create a derived class Circle that inherits from Shape.
○ Its __init__ should take a radius.
○ Implement the area() method to return the area of a circle (π⋅r2). Use
math.pi.
3. Create a derived class Square that inherits from Shape.
○ Its __init__ should take a side_length.
○ Implement the area() method to return the area of a square
(side_length^2).
4. Create instances of Circle and Square and print their areas."""
import math


class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


circle = Circle(5)
square = Square(4)

print(circle.area())
print(square.area())


print('###--------------14NO--------------->>>>>>>>>>>>')

"""Assignment 15: Book and EBook
1. Use the Book class you created earlier (with title, author, pages, and
__init__). Add a display_details() method that prints these attributes.
2. Create a derived class EBook that inherits from Book.
○ Add an attribute file_format (e.g., "PDF", "EPUB") initialized in EBook's
__init__.
○ Override display_details() to include the file_format in addition to the
book's other details.
3. Create an EBook object and display its details."""


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


class EBook(Book):
    def __init__(self, title, author, pages, file_format):
        super().__init__(title, author, pages)
        self.file_format = file_format

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, File Format: {self.file_format}")


ebook = EBook("Python Programming", "Harsha", 250, "PDF")
ebook.display_details()


print('###----------------15NO------------->>>>>>>>>>>>')

"""
Assignment 16: Polymorphism with Animals
1. Using the Animal, Dog classes from Assignment 12, create another derived
class Cat that also inherits from Animal and overrides speak() to print
"Meow!".
2. Create a list containing different animal objects (e.g., an Animal object, a Dog
object, a Cat object).
3. Write a function make_animal_speak(animal_list) that iterates through the
list and calls the speak() method on each animal object.
4. Test this function.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some animal sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Meow!")


def make_animal_speak(animal_list):
    for animal in animal_list:
        animal.speak()


animal = Animal("Animal")
dog = Dog("Dog")
cat = Cat("Cat")

animal_list = [animal, dog, cat]
make_animal_speak(animal_list)


print('###---------------16NO-------------->>>>>>>>>>>>')

"""
Assignment 17: Polymorphism with Shapes
1. Using the Shape, Circle, Square classes from Assignment 14.
2. Create a list containing different shape objects (a Circle and a Square).
3. Write a function print_shape_areas(shape_list) that iterates through the list
and prints the area of each shape by calling its area() method.
4. Test this function.
"""

import math


class Shape:
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


def print_shape_areas(shape_list):
    for shape in shape_list:
        print(shape.area())


circle = Circle(5)
square = Square(4)

shape_list = [circle, square]
print_shape_areas(shape_list)


print('###---------------17NO-------------->>>>>>>>>>>>')

"""
Assignment 18: Dog Population Count
1. Modify the Dog class (from Assignment 12 or create a new one).
2. Add a class variable population_count initialized to 0.
3. In the __init__ method of the Dog class, increment population_count every
time a new Dog object is created.
4. Add a class method get_population() that returns the value of
population_count.
5. Create a few Dog objects and then call Dog.get_population() to see the total
count.
"""


class Dog:
    population_count = 0

    def __init__(self, name):
        self.name = name
        Dog.population_count += 1

    @classmethod
    def get_population(cls):
        return cls.population_count


dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Bella")

print(Dog.get_population())


print('###-----------------18NO------------>>>>>>>>>>>>')

"""
Assignment 19: Item with Sales Tax
1. Create a class Item with:
    - Instance variables: name and price (initialized in __init__).
    - A class variable sales_tax_rate set to 0.05 (for 5% tax).
2. Add an instance method get_price_with_tax() that calculates and returns the
total price of the item including sales tax (price + price * sales_tax_rate).
3. Create an Item object and print its price with tax.
4. Demonstrate that you can change Item.sales_tax_rate and it will affect the
calculation for new calculations on existing or new objects.
"""


class Item:
    sales_tax_rate = 0.05

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price_with_tax(self):
        return self.price + self.price * Item.sales_tax_rate


item = Item("Laptop", 1000)
print(item.get_price_with_tax())

Item.sales_tax_rate = 0.07
item2 = Item("Phone", 500)
print(item2.get_price_with_tax())