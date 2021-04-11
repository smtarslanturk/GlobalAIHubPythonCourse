# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:26:05 2021
@author: samet.arslanturk

Soruların bir cok cevabı bolum bolum eklenmistir. 

Qestion:
User login app.:
    - Get username and password value from user
    - Check the value in an if statement and tell succes.

Extra: 
    - Try building the same user lagin app. with use dictionary!
"""

# In[ ]: Answer 1:
name = "samet"
passWord = 123   

userName = input("Enter username as string: ");


if (userName==name):
    userPassword = int(input("Enter password as number: "))
    if (userPassword==passWord):
        print("Congart you are in")
    else:
        print("Wrong password")
else:
    print("Wrong input")
 
# In[ ]: Answer 2:
name = "samet"
passWord = 123   

userName = input("Enter username as string: ");
userPassword = int(input("Enter password as number: "))
i=0
count=3

if (userName==name and userPassword==passWord ):
  print("Congart you are in")
else:
    print("Wrong username or password")
    while (i<3):
        print("You can try {} ".format(count))
        userName = input("Enter username as string: ");
        userPassword = int(input("Enter password as number: "))
        if (userName==name and userPassword==passWord ):
            print("Congart you are in")
            break
        i+=1
        count-=1
        if(i==3):
            print("You can try nex time. See you later")
# In[ ]: Answer 3:
    
d = {'name':'samet',
     'pass': 123}

userName = input("Enter username as string: ");
userPassword = int(input("Enter password as number: "))
i=0
count=3

if (userName==d["name"] and userPassword==d["pass"] ):
  print("Congart you are in")
else:
    print("Wrong username or password")
    while (i<3):
        print("You can try {} ".format(count))
        userName = input("Enter username as string: ");
        userPassword = int(input("Enter password as number: "))
        if (userName==d["name"] and userPassword==d["pass"]):
            print("Congart you are in")
            break
        i+=1
        count-=1
        if (i==3):
            print("You can try nex time. See you later")
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

