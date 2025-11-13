# # Example with constructor   
# # & def -> define function , init -> initizalier, self -> current object
class Student: # class
  def __init__(self,name,age,grade): # constructor, def _init need space
    self.name = name # instance variable
    self.age = age # instance variable
    self.grade = grade # instance variable
    print("Constructor Called") #  # prints when object is created


# Creating an object of the Student class
s1 = Student("Evan", 20, "Grade 1") # s1 is an object of Student class
print(s1.name, s1.age, s1.grade + "  Constructor called")



print("-------------------------------------------------")

# Example 2 without initializer Or constructor
class Student:
    pass

s1 = Student()
s1.name = "Evan"
s1.age = 10

s2 = Student()
s2.name = "Alice"
s2.age = 12

print(s1.name, s1.age , "Without constructor")
print(s2.name, s2.age, "Without constructor")



"""
Explanation:

Student("Evan", 10) → creates an object.

__init__ runs automatically → sets self.name and self.age.

Prints "Student object created!".

So the purpose of __init__ is to:

Initialize (set up) an object with specific data when it is created.



Summary Table
Concept	Description	Example
def	Defines a function	def greet():
__init__	Constructor method used to initialize object data	def __init__(self, name):
self	Refers to the current object	self.name = name
When it runs	Automatically when object is created	s1 = Student("Evan", 10)



"""