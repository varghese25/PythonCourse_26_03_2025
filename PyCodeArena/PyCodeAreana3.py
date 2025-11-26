class Parent:
    def greet(self):
        return "Hello from Parent"
class child(Parent):
    def greet(self):
        return "Hello from Child"
obj=child()
print(obj.greet())