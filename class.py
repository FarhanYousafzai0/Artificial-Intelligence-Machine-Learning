"""
Object-Oriented Programming (OOP):

OOP is a programming paradigm where we structure our code using Classes and Objects.

- A Class is a blueprint/template. 
  It describes what properties (attributes) and behaviors (methods) an object will have.

- An Object is an instance of a class.
  It contains actual data and can perform actions defined by the class methods.

Why OOP?
- Helps organize code
- Makes programs scalable and reusable
- Allows real-world modelling (Car, Student, BankAccount, etc.)

Attributes  = Variables inside a class (store data)
Methods     = Functions inside a class (define behavior)

When a function belongs to a class, we call it a Method.
This is the foundation of OOP.
"""


class Student:
    def __init__(self,name,age):
          self.name = name;
          self.age = age





s1 = Student("Farhan",20)      
s2 = Student("Hassan",27)       


print(s1.name,s1.age)
print(s2.name,s2.age)
    


"""
# Types of Contructor : So there are two types of construtor in the python :

1:Defult Contructor 
2:Parameterized Contructor




"""