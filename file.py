# File Handling :





#Question NO 1 : So Now there we are trying to find a word,in simple.txt file,so how can find that,so use loops for this condition
# So we used the while loop it always be true and returning the line,then we used funtion f.readline() which readline of fiel,
#and so with loop he read each line ,line by line at the end when he find a line he print the success message.


# data = True
# with open("simple.txt","r") as f:
#     while data:
#           data = f.readline();
#           if("islam" in data):
#                print("We found the word")
#                break
#           print(data)
    



# When you are creating a file ,or opening a file ,then you have to also close the file .when we want to read the file,so we read() function.
"""
File handling 


"""

"1 :Opening and Reading "

# with open("hello.txt","rt") as f:
#     print(f.readlines());





"Note: You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file."





'2 :Write to an Existing File :'



# with open("hello.txt","a") as f:
#     f.write(f"\n I love to code and express feeling about my self.")



# with open("hello.txt","rt") as f:
#     print(f.read());    





"Overwriting the Existing Content:"



with open("hello.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("hello.txt") as f:
  print(f.read())