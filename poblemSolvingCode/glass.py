
# Class & Object

class MyClass:
    " This is my class"
    a = 10
    def func(self):
        print("Hello")

print(MyClass.a)
print(MyClass.func)  # <function MyClass.func at 0x000001E2C3B3C4C0>
print(MyClass.__doc__)  # This is my class

# Object
object1 = MyClass()
print(object1.a)  # 10

object2 = MyClass()
print(object2.a + 5)  # 10


# Constructor,Means we can give value called constructor.
# Self - means class 

class ComplexNumber:
    def __init__(self, r=0, i=0): # constructor with default values
        self.real = r
        self.image = i
    def getData(self):
        print("{0} + {1}j".format(self.real, self.image)) # {0} {1} are placeholders can change values

c1 = ComplexNumber(2, 3) # 2 realvale, 3 is image value, we passed arguments to constructor so it will assign to r and i default values are ignored
c1.getData()  # 2 + 3i

c2 = ComplexNumber() # default values
c2.getData()  # 0 + 0i


# Inheritance

class Mammal:
    def displayMammalFeatures(self):
        print("Mammals give birth to live young ones.")
class Dog(Mammal):  # Dog class inherits Mammal class
    def bark(self):
        print("Woof Woof")
d = Dog()
d.displayMammalFeatures()  # Mammals give birth to live young ones.
d.bark()  # Woof Woof

