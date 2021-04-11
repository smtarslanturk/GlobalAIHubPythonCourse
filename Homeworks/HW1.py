# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:11:24 2021
@author: samet.arslanturk

Soruların bir cok cevabı bolum bolum eklenmistir. 

Qestion:
Create two lists. The first list should consist of odd numbers. The second list is also of even numbers.
Merge two lists. Multiply all values in the newlist by 2.
Use the loop to print the data type of the all values in the new list.
"""
# In[ ]: Answer 1:

import random 

listDim = random.randint(2,20)    
if listDim%2!=0:
    listDim=listDim+1;

randomlist = []
for i in range(0,listDim):
    n = random.randint(1,30)
    randomlist.append(n)

print(f'Random Lis: {randomlist}')

swapPoint1 = int(listDim/2);
sw1=randomlist[0:swapPoint1]
sw2=randomlist[swapPoint1:]
result = sw2+sw2
print(f'Swap List: {result}')

# In[ ]: Answer 2:
n = int(input("Please enter number: "))
# input() func. always keep like string.
    
while (n>9 or n<-9):
     n= int(input("Please enter single digit number: "))
     
if n>0:
    for i in range(n+1):
        if i%2 ==0:
            print("number {}".format(i))
else:  #sayının negatif olma durumu icin yazilmistir. 
    n=-n
    for i in range(n+1):
         if i%2 ==0:
             if i==0:
                 print("number {}".format(i))
             else:
                 print("number -{}".format(i))
            
