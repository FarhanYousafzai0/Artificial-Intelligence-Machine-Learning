# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))

# average = (first + second) / 2

# print("The average of", first, "and", second, "is", average);


# Problem Number 1






# name = input("Enter your name : ");
# age = int(input("Enter your age : "));

# print("Hello", name, "you are", age, "years old");










# Problem Number 2

# FirstNumber = int(input("Enter first number : "));
# SecondNumber = int(input("Enter second number : "));

# Sum = FirstNumber + SecondNumber;
# Product = FirstNumber * SecondNumber;
# Difference = FirstNumber - SecondNumber;
# Quotient = FirstNumber / SecondNumber;

# print("Sum of", FirstNumber, "and", SecondNumber, "is", Sum);
# print("Product of" , FirstNumber, "and", SecondNumber, "is", Product);
# print("Difference of", FirstNumber, "and", SecondNumber, "is", Difference);
# print("Quotient of", FirstNumber, "and", SecondNumber, "is", Quotient);




# Problem Number 3




# a = int(input("Enter first number : "));
# b = int(input("Enter second number : "));
# c = float(input("Enter third number : "));


# average = float((a + b + c) / 3);

# print("The average of", a, b, c, "is", average);







# Problem Number 4

# val = input("Enter a value :");

# print("The type of", val, "is", type(int(val)));
# print("The type of", val, "is", type(float(val)));
# print("The type of", val, "is", type(str(val)));





# Problem Number 5


# print(10 + 3 * 2 ** 2)
# So the anwser will be 22,becase we learn today about operator precedence so that why
# ,so it will be 22 



# Problem Number 6

# a = input("Enter a value : ");
# b = input("Enter a value : ");

# a = b;
# b = a;

# print("The value of a is", a);
# print("The value of b is", b);









# Problem 7


# Temp = input("Enter the temperature in celsius : ");

# Temp = float(Temp);

# F = (Temp * 9/5) + 32;

# print("The temperature in fahrenheit is", F);





# Problem 8
# r = float(input("Enter the radius of the circle : "));

# area = 3.14 * r * r;

# print("The area of the circle is", area);



# Problem 9



# P = int(input("Enter the principal amount : "));
# R = int(input("Enter the rate of interest : "));
# T = int(input("Enter the time period : "));


# SI  = float((P * R * T) / 100);

# print("The simple interest is", SI);



# Problem 10 



# num = float(input("Enter a decimal number: "))

# # integer part=
# integer_part = int(num)

# # fractional part
# fractional_part = num - integer_part

# print("Integer part:", integer_part)
# print("Fractional part:", fractional_part)




# "Lecture Assignment Problems Done"




#Lecture No 2 :

# Conditional Statements :



# Question No 1

# age = int(input("Enter your age : "));


# if age < 13 :
#     print("You are a child.")

# elif age >= 13 and age < 18 :
#     print("You are a teenager")
# else:
#     print("You are an adult")    



# Question NO 2 

# username = input("Enter your username : ");
# password = int(input("Enter your passoword : "));


# if username == "admin" and password == 1234:
#     print("Welcome to the system")
# else:
#     print("Please enter the right values.")



# Question NO 3



# Number = int(input("Enter a number :"));


# if Number % 5 == 0:
#     print("The number is divisible by 5")
# else:
#     print("The number is not divisible by 5")





# Question No 4 

# To find that ,the number is even or odd.

# Num = int(input("Enter a number :"));

# if Num % 2 == 0:
#     print(Num ,"is a even number")
# else:
#     print(Num ,"is a odd number")    




#Nesting : In simple terms nesting means when you are wirte a condition inside another condition .





#  username = input("Enter your username : ");
# password = int(input("Enter your passoword : "));


# if username == "admin" and password == 1234:
#     print("Welcome to the system")
# else:
#     if username != "admin": # So there ,we are doing nesting,inside the else state ,we are writing other if statement to check .
#         print("Wrong username")
#     else:
#         print("Wrong password")
         


 #Match Case 
# color = input("Enter a color : ").title()

# match color:
#     case "Red":
#         print("Stop")
#     case "Yellow":
#         print("Ready")
#     case "Green":
#         print("Go")
#     case _:
#         print("Invalid color")






# While Loop :

# count = 40

# while (count >= 1):
#     print(count)
#     count -= 1








# For Loop :

# n = int(input("Enter a number : "));

# tab = 1
# while (tab <= 10):
#     print(n,"*",tab,"=",n*tab)
#     tab += 1



# Continue statment 



# i = 0 ;

# while (i < 10):
#     i +=1
#     if(i % 2 == 0): # so when the number is divisalbe of 2 ,so it will skip ,so then it will print odd numbers.
#         continue
#     print(i)

    


    # For Looop : So for loop work same as while ,both can do same the task,
    # if one task can perform by while so it can perform by for loop,but for loop is used when you want to do sequential travel.
    




# So now there with the help of if statement and for loop we check how many time is "a" comes in the phrase ,the total of number "a" : so the anwser should be => 6.


# phrase = "Muhammad Farhan Yousafzai";

# count = 0;

# for ch in phrase:
#     if(ch =="a"):
#         count +=1

# print("Number of a in phrase is ", count)



# To Find The Number of Vowel present in the word or phrase.



# word = "Artificial Inteligence"

# count = 0;

# for vo in word:
#     if(vo == "a" or vo == "e" or vo == "i" or vo == "o" or vo == "u"):
#         count +=1
# print("Number of vowels are :" ,count)    


# n = int(input("Enter a number: "))

# total = 0

# for i in range(1, n + 1):
#     total += i

# print("The sum is:", total)


# **************************************Functions*****************************************
# So fuction are some reuseable block of code ,which you can use to perfrom actions,fuction divided into two ,phases ,funciton defination ,where you define 
# all the logic ,and fuction call ,where you call the fucntion to perform the action .

# Question No 1,Sum of 2 Numbers.



# def Sum(a,b):
#     s = a + b
#     return s

# ans = Sum(1304,6785)
# print("The sum of of number are :", ans)

# Question No 2 

 # So here we enter a default parameter ,so when you are writing a fucntion and you want to pass parameter,so first parameter comes,then default 
    #parameter comes,so if the value of c ,for exoample not avialable so 3 will be used.

# def Avg(a,b,c=3): 
#     a = (a + b + c) / 3
#     return a ;

# ans = Avg(5,10)
# print(ans)



# Types of Functions ,so there are two types of fucntion in python ,Built-in funciton,User defined function :
# So built-in function are those functions which is defined by python itself ,for example ,print(),input(),type() etc,.
# And User defined fucntio are function are build by user to perform some specific task ,and do something ,its is resuable ,and word same as Built-in funcitons.




# Lambda  Functions:



# def Fac(n):
#     fact = 1
#     for f in range(1, n + 1):
#         fact *= f
#     return fact


# n = int(input("Enter a number :"))

# print(Fac(n))




# Assignment Problems :

#Question NO 1:


# salary = int(input("Please enter your salary: "))

# if salary < 30000:
#     print("Your tax rate is 5%.")
# elif salary <= 70000:
#     print("Your tax rate is 15%.")
# else:
#     print("Your tax rate is 25%.")
   


#Question NO 2:


# def even_num(a, b):
#     for i in range(a, b + 1):
#         if i % 2 == 0:
#             print(i)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# even_num(a, b)      



# Question No 3 :



# def print_digit(n):
#     digit = n % 10
#     print(digit)
#     n = n // 10


# num = int(input("Enter a number :"));
# print_digit(num)  



# Question no 4:


# def count_number(n):
#     count = 0;
#     while n > 0:
#         n = n // 10
#         count += 1
#     return count

# num = int(input("Enter a number :"))
# print(count_number(num))



# Question no 5 :

# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         digit = n % 10      
#         total += digit       
#         n = n // 10          
#     return total

# num = int(input("Enter a number: "))
# print(sum_of_digits(num))



# 

# Question No 6

# for i in range(1,100):

#     if i % 3 == 0 or i % 5 ==0:
#         print(i)

# Question No 7



# while True:
#     n = input("Enter a number or Quit: ")

#     if n.lower() == "quit":
#         break
    
#     num = int(n)   # convert string to number

#     if num > 0:
#         print("Positive")
#     else:
#         print("Negative")



# Question No 8 :


# def calculator(a,b,operation):
#     if operation == "+":
#         return a + b
        
#     elif operation == "-":
#         return a - b

#     elif operation == "*":
#         return a * b

#     elif operation == "/":
#         return a / b    

#     else:
#         print("Invalid Operation")

# first = int(input("Enter you first number :"))
# second= int(input("Enter you second number :"))
# ope = input("Enter a operation")       

# print(calculator(first,second,ope))



# Question No 9 :
# def is_prime(n):
#     if n < 2:              # Prime numbers start from 2
#         return False

#     for i in range(2, n):  # Check divisibility from 2 to n-1
#         if n % i == 0:     # If divisible → NOT prime
#             return False

#     return True            # No divisor found → PRIME


# # Example usage:
# num = int(input("Enter a number: "))
# print(is_prime(num))




# secret_number = 99

# while True:

#     guess_num = int(input("Guess the number :"))

#     if guess_num > secret_number:
#         print("Too High")
#     elif guess_num < secret_number:
#         print("Too Low")   
#     else:
#         print("Correct")    
#         break




    # Lecture 2 Assignment Problmes Done.



    # Sting 

    
# So this is called string formating and there are two ways to format string :
# So the first one is the {} curly barces formating and the other is f string is formating .so f sting is intruded after python 3.6.and mostly we will be using that.




# a = 6
# b = 8 

# sum = a + b

# print("The sum of {} and {} is {}".format(a,b,sum));




# List are mutalbe which store data in the square bracktedd and it is mutable .



# Numbers = [1,2,3,4,5,6,7,8];

# # So there are we are performing the indexing ,we can perform slicing the in two ways,Positive slicing,and nagetive slcing and also perform ,indexing .

# Numbers[4] = 77     
# print(Numbers[-6:-2])
# print(Numbers[3:len(Numbers)])      
# print(Numbers)



# So there are List method we can perfrom by List.
# So what are methods ,so method are class specific functions,we can use that for antoher things ,these are function but specific for each variralbe.

# So for List some are append(),insert();sort(),reverse() => so this is for Lists.



# Num = [1,3,4,5,2,8,6]

# Num.append(9)
# Num.insert(2,10)
# Num.sort()
# print(Num)




# Loops in List:



# nums = [1,2,3,4,5,10]
# x = 10
# idx = 0
# for val in nums:
     
#      if val == x:
#          print(f"So the value of {x} is find at {idx} index.")
#          break
#      idx +=1



#Tuples are immutable data type in pthon which is used parenthesis ,so we create tuples using () ,and we cant do indexing there and cant change the value .




# So we cant create single values in tuple ,like tup = (1) if do this it will be math expression and its type will be int ,we have to add comman after first index.
# If we add single thing in tuple like ,string,int,float,boolean,so it will be the same data type we enter the values,not will be tuple data type,so we have to add comma.





# tup = (1,2,3,4,5,6,7,8,9,10);
# print(tup.count(10));
# print(tup.index(5));

# print(tup)

# sum = 0
# for val in tup:
#     sum += val
# print(f"The Sum of all the values is {sum}");






# Dictionary "

# So dictoinary is another data which we will be using to store data about user,and its is create by curly braces{} and it is mutable .



# User_Data = {

#     "name":"Muhammad Farhan Yousafzai",
#     "city":"Nowshera",
#     "cgpa":9,
#     "course":"Ai/Ml"
# }

# User_Data["cgpa"] = 10 

# # print(User_Data.keys())
# # print(User_Data.values())
# # print(User_Data.items());
# # print(User_Data.get("Company"))
# print(User_Data);


# So Dictoinary aslo have Method which is build specific for dictionary and we used some of them .






#'''''''''''''''''''''''''"Sets""''''''''''''''''''''''''''''''''''''''''":

# So Sets is another data type ,and a collectio of unique elements.

# Create a List :
# dic = {}

# info = [
#     ("Farhan","Maths"),
#     ("Hassan","English"),
#     ("Haseeb","Maths"),
#     ("Musa Khan","Chemistry"),
#     ("Hamza","Physics"),
#     ("Ayesh","English")
# ]


# for name, subject in info:
#      if(dic.get(name) == None):
#           dic.update({name:set()})
#           dic[name].add(subject)

#      else:
#           dic[name].add(subject)



# print(dic)
  







# 


# Ask user for a string
# s = input("Enter a string: ")

# # Reverse the string manually using a loop
# rev = ""
# for ch in s:
#     rev = ch + rev   # add each character to the front

# # Check if palindrome
# if s == rev:
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")




# Question No 2:


# Total = 0
# numbers = [2,3,4,5,6,8,9,10];

# length = len(numbers);

# for s in numbers:
#     Total += s

# ans = Total / length

# print(ans);



# Question No 3 :



# list1 = list(input("Enter first list :").split());
# list2 = list(input("Enter second list :").split());



# marged = list1 + list2 
# marged.sort()
# print(marged);





# Question No 4 :


# So in this question ,first we create a tuples ,types are immtable ,and we can append to tuples,so then we create two List even and odd ,then loop over 
# nums and and find out which number is odd and even ,and and apppned in the even and odd list and the after that we convert those two list into tuples.

# nums = (1,2,3,4,5,6,7,8,9,10,11,12)

# even_list = []
# odd_list = []

# for t in nums:
#     if t % 2 == 0:
#         even_list.append(t)
#     else:
#         odd_list.append(t)

# even_tuples = tuple(even_list);
# odd_tuples = tuple(odd_list);

# print(even_list)
# print(odd_list)
             


# Queston No 5 :


# students = {}

# while True:
#     print("\nMenu:")
#     print("A - Add a student")
#     print("B - Update marks")
#     print("C - Search for a student")
#     print("D - Display all students and marks")
#     print("E - Exit program")
    
#     choice = input("Enter your choice (A/B/C/D/E): ").upper()

#     if choice == "A":
#         name = input("Enter your name: ")
#         marks = int(input("Enter your marks: "))
#         students[name] = marks
#         print(f"{name} added successfully.")

#     elif choice == "B":
#         name = input("Enter your name: ")
#         if name in students:
#             marks = int(input("Enter new marks: "))
#             students[name] = marks
#             print(f"Marks updated for {name}")
#         else:
#             print("Student not found.")

#     elif choice == "C":
#         name = input("Enter a student name to search: ")
#         if name in students:
#             print(f"{name} is available with marks: {students[name]}")
#         else:
#             print("Student is not available.")

#     elif choice == "D":
#         if len(students) == 0:
#             print("No Students Available")
#         else:
#             print("\nStudents List:")
#             for name, marks in students.items():
#                 print(f"Student Name: {name}  |  Student Marks: {marks}")

#     elif choice == "E":
#         print("Exiting program...")
#         break

#     else:
#         print("Invalid choice. Please choose A, B, C, D, or E.")



# Question NO 6 :
# words = ["apple", "banana", "kiwi", "cherry", "mango"]

# fruits = {}

# for w in words:
#     length = len(w)
#     fruits[w] = length   # <-- This is what you were missing

# print(fruits)





# Question NO 7 :


# phrase = input("Enter a phrase please :");


# dashes = phrase.count(" ");

# print(f"So the number of dashes in the {phrase} is {dashes}");


# Question NO 8



# list1 = [1,3,4,5,6]
# list2 = [6,7,8,9,10]

# s1 = set(list1)
# s2 = set(list2)

# ans = s1.isdisjoint(s2)
# print(ans)



# Question No 9 :


# list = [1, 2, 3, 2, 4, 5, 1]


# seen = set();
# duplicate = set();

# for number in list:
#     if number in seen:
#         duplicate.add(number)
#     else:
#         seen.add(number)


# print(f"Elements that appear more than once: { duplicate} "),




# Quetion 10 :


# word = input("Enter a word :");

# unique_words = set(word);

# length = len(unique_words);

# print(f"The unique words are : {unique_words} and the length of unique words are :{length}")
    



# # Chapter 3 Question are done .All the 10 Question.


