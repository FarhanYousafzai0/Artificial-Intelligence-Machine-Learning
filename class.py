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


# class Student:
#     def __init__(self,name,age):
#           self.name = name;
#           self.age = age





# s1 = Student("Farhan",20)      
# s2 = Student("Hassan",27)       


# print(s1.name,s1.age)
# print(s2.name,s2.age)
    


"""
# Types of Contructor : So there are two types of construtor in the python :

1:Defult Contructor 
2:Parameterized Contructor

So default contrutors are those contructors which is have only self parameter as default ,and parameterized contructors are those are those init method which 
have more then two three parameter like we create at the top.So this is the differnce.

.Each class will have only one constructor ,it will not have more than one ,if we create more than one contructor so by default the last one will be run.




"Artributes"

So there are two types of artributes :

1: Class artributes => which belongs to class.

2: Object artributes => which belongs to object


So those artributes which we are defined by class are class artibutes, but those artibutes which we define by constructor _init_(self,name,age) are 
called Object artributes. 



"Methods" :

So there are three types of methods in python :
1:instance
2:class
3:static methods



*  So instance method can access class artributes and instance as welll.
   But Class artributes can't access instance artributes.

* So class artributes only acces only class artribures get_laptop_storage(cls)

* So static methods cant access class artributes neither instance artributes.So static methods are stand alone functions in the class.
"""


# Question NO 1:



# class Product:
#     total_products = 0

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.total_products += 1

#     def get_info(self):
#         print(f"Product Name: {self.name}, Price: {self.price}")

#     @classmethod
#     def get_products(cls):
#         print(f"Total Products Created: {cls.total_products}")

#     @staticmethod
#     def cal_discount(price, discount):
#         discounted_price = price - (price * discount / 100)
#         return discounted_price


# # Creating objects
# p1 = Product("Samsung Galaxy", 10000)
# p2 = Product("iPhone 13 Pro Max", 50000)

# # Display total products
# Product.get_products()

# # Show product info
# p1.get_info()
# p2.get_info()

# # Calculate and print discounts
# print(f"Discounted price for {p1.name}: {Product.cal_discount(p1.price, 10)}")
# print(f"Discounted price for {p2.name}: {Product.cal_discount(p2.price, 20)}")




# Object Oriented Programming Language Core Pillars => Important Topic :