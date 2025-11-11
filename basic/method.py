"""Method
1> A function defined inside a class
2> always associated with object
3> its is defined inside a class.
4> Typically operated on the data contained within its associated object.
Examples: list.appends(), dict.items(),str.upper(),set.add()  etc."""

# method (inside a  class)
class student: # student class is object
    def greet(self, name):  # 'self' + 'name' are parameters
        print("Hello from student name is: ", name)

# Method call
obj = student()
obj.greet("Varghese")  # method call,  # "Varghese" is the argument