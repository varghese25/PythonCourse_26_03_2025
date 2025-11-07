class App: 
    version = 1.0 # class variable
    
a = App()
b = App()

a.version = 2.0
print(App.version,a.version,b.version)

""""
Explanation:
a.version = 2.0 creates an instance variable for a App version and 
b.version still point to the original
class variable

So 
App.version - 1.0
a.version - 2.0 (instance override)
b.version - 1.0 


"""