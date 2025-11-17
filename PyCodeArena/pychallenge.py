class Car:
    wheels = 4
c1 = Car ()
c2 = Car ()
c1.wheels = 6
print(c1.wheels, c2.wheels)


#OutPut: "6 4"



'''Explanation:
wheels = 4 → class variable, shared by all instances initially.

c1.wheels = 6 → creates a new instance variable wheels for c1, which overrides the class variable only for c1.

c2 doesn’t have an instance variable wheels, so it still uses the class variable, which is 4.'''