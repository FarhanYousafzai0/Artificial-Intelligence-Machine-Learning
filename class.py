# """
# Object-Oriented Programming (OOP):

# OOP is a programming paradigm where we structure our code using Classes and Objects.

# - A Class is a blueprint/template. 
#   It describes what properties (attributes) and behaviors (methods) an object will have.

# - An Object is an instance of a class.
#   It contains actual data and can perform actions defined by the class methods.

# Why OOP?
# - Helps organize code
# - Makes programs scalable and reusable
# - Allows real-world modelling (Car, Student, BankAccount, etc.)

# Attributes  = Variables inside a class (store data)
# Methods     = Functions inside a class (define behavior)

# When a function belongs to a class, we call it a Method.
# This is the foundation of OOP.
# """


# # class Student:
# #     def __init__(self,name,age):
# #           self.name = name;
# #           self.age = age





# # s1 = Student("Farhan",20)      
# # s2 = Student("Hassan",27)       


# # print(s1.name,s1.age)
# # print(s2.name,s2.age)
    


# """
# # Types of Contructor : So there are two types of construtor in the python :

# 1:Defult Contructor 
# 2:Parameterized Contructor

# So default contrutors are those contructors which is have only self parameter as default ,and parameterized contructors are those are those init method which 
# have more then two three parameter like we create at the top.So this is the differnce.

# .Each class will have only one constructor ,it will not have more than one ,if we create more than one contructor so by default the last one will be run.




# "Artributes"

# So there are two types of artributes :

# 1: Class artributes => which belongs to class.

# 2: Object artributes => which belongs to object


# So those artributes which we are defined by class are class artibutes, but those artibutes which we define by constructor _init_(self,name,age) are 
# called Object artributes. 



# "Methods" :

# So there are three types of methods in python :
# 1:instance
# 2:class
# 3:static methods



# *  So instance method can access class artributes and instance as welll.
#    But Class artributes can't access instance artributes.

# * So class artributes only acces only class artribures get_laptop_storage(cls)

# * So static methods cant access class artributes neither instance artributes.So static methods are stand alone functions in the class.




# Notes :
# Almost everything in Python is an object, with its properties and methods.


# """







# # Question NO 1:



# # class Product:
# #     total_products = 0

# #     def __init__(self, name, price):
# #         self.name = name
# #         self.price = price
# #         Product.total_products += 1

# #     def get_info(self):
# #         print(f"Product Name: {self.name}, Price: {self.price}")

# #     @classmethod
# #     def get_products(cls):
# #         print(f"Total Products Created: {cls.total_products}")

# #     @staticmethod
# #     def cal_discount(price, discount):
# #         discounted_price = price - (price * discount / 100)
# #         return discounted_price


# # # Creating objects
# # p1 = Product("Samsung Galaxy", 10000)
# # p2 = Product("iPhone 13 Pro Max", 50000)

# # # Display total products
# # Product.get_products()

# # # Show product info
# # p1.get_info()
# # p2.get_info()

# # # Calculate and print discounts
# # print(f"Discounted price for {p1.name}: {Product.cal_discount(p1.price, 10)}")
# # print(f"Discounted price for {p2.name}: {Product.cal_discount(p2.price, 20)}")




# # Object Oriented Programming Language Core Pillars => Important Topic :





# # class object:
# #     x = 5



# # p1 = object()



# # print(p1.x);


# # del p1

# # Note: The __init__() method is called automatically every time the class is being used to create a new object.


# # class Person:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age



# # p1 = Person("Farhan",20);
# # p2 = Person("Ali",26);


# # print(f"So my name is {p1.name} and i am {p1.age} old.")
# # print(f"So my name is {p2.name} and i am {p2.age} old.")

        





# # Create a class without iniit methot:Without the __init__() method, you would need to set properties manually for each object:

# # The pass Statement :class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# # class Student:
# #     pass




# # p1 = Student();
# # p1.name= "Farhan"
# # p1.age = 5


# # print(f"My name is {p1.name}")



# """ 
# Self parameter : 

# The self parameter is a reference to the current instance of the class.

# It is used to access properties and methods that belong to the class.


# """




# # class Self:
# #     def __init__(self,name,age,school):
# #         self.name = name
# #         self.age = age
# #         self.school = school


# #         # great funciton:
# #     def greet(self):
# #         print(f"Helo my name is {self.name} and i am studing at {self.school} and my age is {self.age}");




# # s1 = Self("Farhan",20,"Fg Public High School Nowshera cantt.");

# # s1.greet();
        


# # class Car:
# #     def __init__(self,brand,model,year):
# #         self.brand = brand
# #         self.model = model
# #         self.year = year

# #     def display_infor(self):
# #         print(f"The brand is |{self.brand}| ,the model is |{self.model}| and the year is |{self.year}|");
   

# #     def let_buy(self):
# #         message = self.display_infor()
# #         print(f"So how this model did you like it or not.")

# # c1 = Car("BMW","M5 Compitition",2025);

# # c1.let_buy()
                



# """
# Encapsulations And Data hiding ,





# """

# # Questiono:


# # class Bank:
# #     def __init__(self,name,balance):
        
# #         self.name = name
#         # self.__balance = balance


#       # Getter Functions so get the values of private attributes:
#       # 
#       # 
# #     def get_info(self):

# #         return self.__balance


# #     def set_info(self,newbalance):
# #         self.__balance = newbalance 


# # b1 = Bank("Farhan",400000)


# # b1.set_info(200000);

# # print(b1.name,b1.get_info());


# # So there fist we get the value of private artributes and then set the values of privates by using the setter and getter functions.



# # Interitence:

# # Question :

# # class Employe:
# #     startTime = "10PM"
# #     endTime = "6PM"

# #     def change(self, new_time):
# #         self.endTime = new_time


# # class Teacher(Employe):
# #     def __init__(self, subject):
# #         self.subject = subject


# # # Creating object
# # t1 = Teacher("Mathematics")

# # # Changing end time using inherited method
# # t1.change("8PM")

# # # Printing details
# # print(f"The subject is {t1.subject}, the start time is {t1.startTime}, and the end time is {t1.endTime}")




# # Types of inheritence :
        




# # class Employe:
# #     start_time = "5PM"
# #     end_time = "6Pm"


# # class AdminStaff(Employe):
# #     def __init__(self,role):
# #         self.role = role


# # class Account(AdminStaff):
# #      def __init__(self,salary, role):
# #          super().__init__(role)    
# #          self.salary = salary    



# # a1 = Account(40000,"Asistant Officer");


# # print(a1.end_time,a1.start_time,a1.salary,a1.role);
        





# # from abc import ABC ,abstractmethod



# # class Animal(ABC):
# #     @abstractmethod
# #     def make_sound(self):
# #         pass
    

# # class Lion(Animal):
# #     def make_sound(self):
# #         print("Roar")

# # class Cat(Animal):
# #     def make_sound(self):
# #         print("Meow")
        

# # c1 = Lion();
# # c2 = Cat();

# # c1.make_sound();
# # c2.make_sound()





# # class PakistanArmy():
# #     def attact(self):
# #         print("Ground Attact");



# # class PakistanNavy():
# #     def attact(self):
# #         print("Sea Attact");

# # class PakistanAirforce():
# #     def attact(self):
# #         print("Air Attact");


# # forces = [PakistanArmy(),PakistanNavy(),PakistanAirforce()]

# # for i in forces:
# #     i.attact();






# # Assignment Questions :

# # Problems Question 1 :



# # class BankAccount:
# #     def __init__(self, account_number, owner_name, account_balance):
# #         self.account_number = account_number
# #         self.owner_name = owner_name
# #         self.account_balance = account_balance

# #     def deposit(self, add_money):
# #         self.account_balance += add_money
# #         print(f"Deposit successful! New balance: {self.account_balance}")

# #     def withdraw(self, amount):
# #         if amount > self.account_balance:
# #             print("Insufficient balance.")
# #         else:
# #             self.account_balance -= amount
# #             print(f"Withdrawn: {amount}. Remaining balance: {self.account_balance}")

# #     def check_balance(self):
# #         print(f"Current balance: {self.account_balance}")


# # # Creating object (correct)
# # b1 = BankAccount(879065784, "United Bank Limited", 7000000)

# # # Testing
# # b1.deposit(7000000);




# # Question No 2 :


# # class Book:
# #     def __init__(self, title, author, list_of_reviews=None):
# #         self.title = title
# #         self.author = author
# #         self.list_of_reviews = list_of_reviews if list_of_reviews is not None else []

# #     def add_review(self, review):
        
# #         self.list_of_reviews.append(review)
# #         print(f"Review added: {review}")

# #     def count_reviews(self):
# #         print(f"Total reviews: {len(self.list_of_reviews)}")

# #     def display_reviews(self):
# #         if len(self.list_of_reviews) == 0:
# #             print("No reviews found.")
# #         else:
# #             print("All Reviews:")
# #             for r in self.list_of_reviews:
# #                 print("-", r)


# # # Creating object
# # b1 = Book("Guardians of the Galaxy", "Adam Hills", [])

# # # Add review
# # b1.add_review("Great book with powerful concepts!")
# # b1.add_review("A bit slow in the middle but worth reading.")

# # # Display reviews
# # b1.display_reviews()

# # # Count reviews
# # b1.count_reviews()




# # Question NO 3 :




# # class Student:
# #     def __init__(self,name,roll_no,marks):
# #         self.__name = name
# #         self.__roll_no = roll_no
# #         self.__marks = marks
    

# #     def get_info(self,name):
# #         if name == "":
# #             print("Name cannot be empty")
# #         else:
# #             self.__name = name    


# #     def New_marks(self,marks):
# #         if marks >= 0:
# #             self.__marks = marks
# #         else:
# #             print("Marks cannot be nagetive.")             


# #     def change_roll(self,roll_no):
# #           if 1 <= roll_no <= 100:
# #                self._roll_no = roll_no
# #           else:
# #              print("Invalid roll number")
    


    




# # Question No 4 :


# # import math

# # # Base class
# # class Shape:
# #     def area(self):
# #         pass

# # # Circle subclass
# # class Circle(Shape):
# #     def __init__(self, radius):
# #         self.radius = radius
    
# #     def area(self):
# #         return math.pi * self.radius ** 2

# # # Rectangle subclass
# # class Rectangle(Shape):
# #     def __init__(self, length, width):
# #         self.length = length
# #         self.width = width
    
# #     def area(self):
# #         return self.length * self.width

# # # Triangle subclass
# # class Triangle(Shape):
# #     def __init__(self, base, height):
# #         self.base = base
# #         self.height = height
    
# #     def area(self):
# #         return 0.5 * self.base * self.height


# # # Testing the code
# # if __name__ == "__main__":
# #     # Create objects
# #     circle = Circle(5)
# #     rectangle = Rectangle(10, 6)
# #     triangle = Triangle(8, 4)
    
# #     # Display areas
# #     print(f"Circle Area: {circle.area():.2f}")
# #     print(f"Rectangle Area: {rectangle.area():.2f}")
# #     print(f"Triangle Area: {triangle.area():.2f}")
    
# #     # Demonstrating polymorphism
# #     print("\n--- Polymorphism Demo ---")
# #     shapes = [circle, rectangle, triangle]
# #     for shape in shapes:
# #         print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
        
             




#  #Question 5:

# # Base class
# # class Vehicle:
# #     def __init__(self, brand, model):
# #         self.brand = brand
# #         self.model = model
    
# #     def display_info(self):
# #         print(f"Brand: {self.brand}, Model: {self.model}")


# # # Car subclass
# # class Car(Vehicle):
# #     def __init__(self, brand, model, seats):
# #         super().__init__(brand, model)  # Call parent constructor
# #         self.seats = seats
    
# #     def display_info(self):
# #         super().display_info()
# #         print(f"Seats: {self.seats}")


# # # Bike subclass
# # class Bike(Vehicle):
# #     def __init__(self, brand, model, engine_cc):
# #         super().__init__(brand, model)  # Call parent constructor
# #         self.engine_cc = engine_cc
    
# #     def display_info(self):
# #         super().display_info()
# #         print(f"Engine CC: {self.engine_cc}")


# # # Testing the code
# # if __name__ == "__main__":
# #     # Create Car object
# #     car = Car("Toyota", "Camry", 5)
# #     print("--- Car Details ---")
# #     car.display_info()
    
# #     print()
    
# #     # Create Bike object
# #     bike = Bike("Honda", "CBR", 1000)
# #     print("--- Bike Details ---")
# #     bike.display_info()
    
# #     print()
    
# #     # Accessing attributes directly
# #     print("--- Direct Access ---")
# #     print(f"Car Brand: {car.brand}, Model: {car.model}, Seats: {car.seats}")
# #     print(f"Bike Brand: {bike.brand}, Model: {bike.model}, Engine CC: {bike.engine_cc}")
                    
      
    
  

# # Question no 6 :


# from abc import ABC, abstractmethod

# # Abstract base class
# class Employee(ABC):
#     def __init__(self, name, emp_id):
#         self.name = name
#         self.emp_id = emp_id
    
#     @abstractmethod
#     def calculate_salary(self):
#         pass
    
#     def display_info(self):
#         print(f"Employee ID: {self.emp_id}, Name: {self.name}")


# # Intern subclass
# class Intern(Employee):
#     def __init__(self, name, emp_id, stipend):
#         super().__init__(name, emp_id)
#         self.stipend = stipend
    
#     def calculate_salary(self):
#         return self.stipend


# # FullTimeEmployee subclass
# class FullTimeEmployee(Employee):
#     def __init__(self, name, emp_id, monthly_salary):
#         super().__init__(name, emp_id)
#         self.monthly_salary = monthly_salary
    
#     def calculate_salary(self):
#         return self.monthly_salary


# # ContractEmployee subclass
# class ContractEmployee(Employee):
#     def __init__(self, name, emp_id, hours_worked, hourly_rate):
#         super().__init__(name, emp_id)
#         self.hours_worked = hours_worked
#         self.hourly_rate = hourly_rate
    
#     def calculate_salary(self):
#         return self.hours_worked * self.hourly_rate


# # Testing the code
# if __name__ == "__main__":
#     # Create employee objects
#     intern = Intern("Alice", "E001", 5000)
#     full_time = FullTimeEmployee("Bob", "E002", 50000)
#     contract = ContractEmployee("Charlie", "E003", 160, 500)
    
#     # Display information and calculate salaries
#     print("--- Intern ---")
#     intern.display_info()
#     print(f"Salary: Rs. {intern.calculate_salary()}\n")
    
#     print("--- Full Time Employee ---")
#     full_time.display_info()
#     print(f"Salary: Rs. {full_time.calculate_salary()}\n")
    
#     print("--- Contract Employee ---")
#     contract.display_info()
#     print(f"Salary: Rs. {contract.calculate_salary()}\n")
    
#     # Demonstrating polymorphism with abstraction
#     print("--- All Employees Salary Summary ---")
#     employees = [intern, full_time, contract]
#     for emp in employees:
#         print(f"{emp.name}: Rs. {emp.calculate_salary()}")




# clas Student:






# Revision :


# """

# So the class which inhertited ,is called base class,and the the class which inherit values from that class class called
# Drived class,and the parent class is aslo called base class.



# """


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2024)
# x.welcome()






"""
The word polymorphism meany many forms,but in programming its refers to methods,operators,functions that has same name
but that can be excuted on many objects,classes and functions.
"""


# Same name ,and performing operation on differnt varaibles,and methos.

# x = "Hello World";


# print(len(x));




# y = ("Apple","Mango","Oranage");


# print(len(y));





"""
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
"""




# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("The Car Move on the road.")




# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("The boat Sail in the ocean.")    


# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand 
#         self.model = model

#     def move(self):
#         print("The Plane fly in the air.")       






# car1 = Car("Toyoto",2004)  
# plan1 = Plane("F17 Thunder",2017);
# boat1 = Boat("DeepOcean1",2010);




# for x in (car1,plan1,boat1):
#     x.move();


"Look at the end for loop due to polymorphism we used the same method for all of the classes."





# class Vehicle:

#     def __init__(self,brand,model):
#         self.brand = brand 
#         self.model = model
#     def move(self):
#         print("Move")     
        


# class Car(Vehicle):
#     pass




# class Boat(Vehicle):
#     def move(self):
#         print("Sail");


# class Plane(Vehicle):
#     def move(self):
#         print("Fly.")
            



# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")   



# for x in (car1,boat1,plane1):
#     print(x.brand,x.model)

#     x.move()







# "Python Encapsulation : Python encupsulation means protecting data inside class."





# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age # Private property


#   def get_age(self):
#     return self.__age;
# p1 = Person("Emil", 25)

# def set_age(self,age):
#   if age > 0:
#     self.__age = age

#   else:
#     print("Age must be a positive number")
     

    

# p1 = Person("Tobias", 25)
# print(p1.get_age())

# p1.set_age(26)
# print(p1.get_age())



# So cant get values the of class which is private direclty ,so for this we used the setter and maker helper functions.





# class Student:
#     def __init__(self,name):
#         self.name = name
#         self.__grade = 0



#     def set_grade(self,grade):

#         if 0 <= grade <= 100:
#             self.__grade = grade
#         else:
#             print("Grade must be between 0 and 100.")

#     def get_grade(self):
#         return self.__grade



#     def get_status(self):

#         if self.__grade >= 60:
#            return "Passed"
#         else:
#             print("You are faild.")            
        





# student = Student("Emil")
# student.set_grade(85)
# print(student.get_grade())
# print(student.get_status())




        



# class Calculator:
#   def __init__(self):
#     self.result = 0

#   def __validate(self, num):
#     if not isinstance(num, (int, float)):
#       return False
#     return True

#   def add(self, num):
#     if self.__validate(num):
#       self.result += num
#     else:
#       print("Invalid number")

# calc = Calculator()
# calc.add(10)
# calc.add(5)
# print(calc._Calculator__validate)        






"""
Name Mangling :
Name mangling is how Python implements private properties and methods.

When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.

For example, __age becomes _Person__age


While  you can  acces the private properities with mangled name,but its not recomended becase it defeats the meanning of encupsulation.


"""




"Python Inner Classes :"




# class Outer:
#   def __init__(self):
#     self.name = "Emil"

#   class Inner:
#     def __init__(self, outer):
#       self.outer = outer

#     def display(self):
#       print(f"Outer class name: {self.outer.name}")

# outer = Outer()
# inner = outer.Inner(outer)
# inner.display()





class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.engine = self.Engine()

  class Engine:
    def __init__(self):
      self.status = "Off"

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()
        