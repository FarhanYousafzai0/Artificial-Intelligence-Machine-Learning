# File Handling :





#Question NO 1 : So Now there we are trying to find a word,in simple.txt file,so how can find that,so use loops for this condition
# So we used the while loop it always be true and returning the line,then we used funtion f.readline() which readline of fiel,
#and so with loop he read each line ,line by line at the end when he find a line he print the success message.


data = True
with open("simple.txt","r") as f:
    while data:
          data = f.readline();
          if("islam" in data):
               print("We found the word")
               break
          print(data)
    