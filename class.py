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




Notes :
Almost everything in Python is an object, with its properties and methods.


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





# class object:
#     x = 5



# p1 = object()



# print(p1.x);


# del p1

# Note: The __init__() method is called automatically every time the class is being used to create a new object.


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age



# p1 = Person("Farhan",20);
# p2 = Person("Ali",26);


# print(f"So my name is {p1.name} and i am {p1.age} old.")
# print(f"So my name is {p2.name} and i am {p2.age} old.")

        





# Create a class without iniit methot:Without the __init__() method, you would need to set properties manually for each object:

# The pass Statement :class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# class Student:
#     pass




# p1 = Student();
# p1.name= "Farhan"
# p1.age = 5


# print(f"My name is {p1.name}")



""" 
Self parameter : 

The self parameter is a reference to the current instance of the class.

It is used to access properties and methods that belong to the class.


"""




# class Self:
#     def __init__(self,name,age,school):
#         self.name = name
#         self.age = age
#         self.school = school


#         # great funciton:
#     def greet(self):
#         print(f"Helo my name is {self.name} and i am studing at {self.school} and my age is {self.age}");




# s1 = Self("Farhan",20,"Fg Public High School Nowshera cantt.");

# s1.greet();
        


# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_infor(self):
#         print(f"The brand is |{self.brand}| ,the model is |{self.model}| and the year is |{self.year}|");
   

#     def let_buy(self):
#         message = self.display_infor()
#         print(f"So how this model did you like it or not.")

# c1 = Car("BMW","M5 Compitition",2025);

# c1.let_buy()
                



"""
Encapsulations And Data hiding ,





"""

# Questiono:


# class Bank:
#     def __init__(self,name,balance):
        
#         self.name = name
        # self.__balance = balance


      # Getter Functions so get the values of private attributes:
      # 
      # 
#     def get_info(self):

#         return self.__balance


#     def set_info(self,newbalance):
#         self.__balance = newbalance 


# b1 = Bank("Farhan",400000)


# b1.set_info(200000);

# print(b1.name,b1.get_info());


# So there fist we get the value of private artributes and then set the values of privates by using the setter and getter functions.



# Interitence:


class Employe:
    startTime = "10PM"
    endTime = "6PM"

    def change(self, new_time):
        self.endTime = new_time


class Teacher(Employe):
    def __init__(self, subject):
        self.subject = subject


# Creating object
t1 = Teacher("Mathematics")

# Changing end time using inherited method
t1.change("8PM")

# Printing details
print(f"The subject is {t1.subject}, the start time is {t1.startTime}, and the end time is {t1.endTime}")

        
        