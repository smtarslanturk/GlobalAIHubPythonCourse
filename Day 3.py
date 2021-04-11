# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 19:06:06 2021

@author: samet.arslanturk
"""

"""
Question-1:
Write a program that inputs an integer value (stop_number) from the user and 
prints the sum of all numbers from 0 to stop_number. You can assume the user will enter a valid value.
Toplarken stop numberıda dahil ettik."""

stopNumber = int(input("Enter stop number: "));
results=0;
for i in range(0,stopNumber+1):
    results = results+i
    
print(f'Sum of all numbers: {results}')


"""
Question-2:
Extend your program to also input the start_number from the user. 
In this case, your program will add all numbers from start_number to stop_number. 
You can assume that the user will enter two valid values.
Stop numberı da dahil ediyorum."""

startNumber = int(input("Start number: "))
stopNumber = int(input("Stop number: "))
results=0;
for i in range(startNumber,stopNumber+1):
    results=results+i;
print(f'Sum of all numbers: {results}')



"""Question-3¶
Extend your program to check if the start_number is an integer between 0 and 100. 
If so, your program will continue to ask for the second input and perform calculations; 
otherwise, it prints an error and stops execution."""

start_number = int(input("Please enter a start number: "))

if 0 <= start_number <= 100:
  stop_number = int(input("Please enter a stop number: "))
  
  if start_number <= stop_number <= 100:
  
    result = 0
    for i in range(start_number, stop_number):
      result += i
    print(result)
  else:
    print("Invalid stop number")
  
else:
  print("Invalid start number")
  
# In[ ]:

""" Dictionaries:
        A data type in Python.
        Dictionaries are indexed by keys and these keys can be a String and integer type.
        Shown as key:value pairs and keys are the unique values.
        {}"""

d= {}
d
print(type(d))

d1 = {"python": 1,
     "course": 2}   #Sozluk tanımlama yontemi.
print(d1)
print(type(d1))  

d2 = dict(python=1 ,course=2) #Sozluk tanımlama yontemi.
print(d2)  
print(type(d2))  

d3 = {"machine": ["learning", "deneme"],
      "artifical": "intellegent"}
print(d3)  
print(type(d3)) 
d3["machine"][1]

d3["samet"] = ["arslanturk", 26, "AI researcher"]
d3  
d3.keys()  
d3.values()  
d3.items()  

# list1 =[]
# k=0
for i in d3.values():
    print(i)
    
for i in d3.keys():
    print(i)

for k,v in d3.items():
  print("Key:", k, "Value:", v)

for k,l in d3.items():
    print(k,l)
    # list3 = k;
    # list4 = l;

d3.get("samet")


#creating a dictionary from a list
nums = list(range(9)) # [0,1,2,3,4,5,6,7,8]

even_sqr = {x: x**2 for x in nums if x % 2 == 0}
print(even_sqr)


  
  