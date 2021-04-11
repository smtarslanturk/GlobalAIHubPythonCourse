# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:48:02 2021

@author: samet.arslanturk
"""


    #LOGICAL OPERATION:
t = True;
f = False;

print(t)
print(f)
print(t or f)
print(t and f)
print(not t)  # not: True if operand is false (complements the operand)
#print(t not)  Hata verir.
print(t != f) # != not equal
print(t == f) #equal 

    #len():
hello = "Hello"
word = "Word"

len(hello) #int deger dondurur.
print(len(hello))
type(len(hello))

print(word + " " +     tr(len(hello)) + "\n" + "Hello" )
#\n: bir alt satıra indirir. 

word2 = '%s %d' %(word, len(word))
word2
#%s: string ifadeleri tanımlar.
#%d: int ifadeleri tanımlar.
print("%s Lenght: %d" %(word, len(word)))
print(word, len(word))


    # 'TYPE CONVERSION': 
    # str()
    # float()
    # int()

# print(word + len(word))
# TypeError: can only concatenate str (not "int") to str
print(word +' '+ str(len(word)))
str("Python")    
float(5)    
int(5)    
type(5.0)    
# float('Hello')    
# ValueError: could not convert string to float: 'Hello'
int(5.6)
    
    # Indexing and Slicing:
bites = "Bites"
print(bites)
type(bites)
print(bites[0]) #indexler 0dan baslıyor.
print(bites[4])
# print(bites[5]) #5. index yok.
# IndexError: string index out of range

b2 = ' Bites'
b2[0]
bites[-1]
bites[-4]
bites[-5]
# bites[-6] #Sınırların disina cikmistir.
# IndexError: string index out of range

hello[2:4]  # [x:y] --> take the values from x th to y th but don't take y th value.
SA = "Samet Arslanturk"
ad = SA[0:5] #0'dan baslar 5. indexe kadar alır ama 5 dahil degildir.
print(ad)
soyad = SA[6:] #6 dan baslar sonuna kadar alir. 
print(soyad)
ters = SA[::-1] #Stringleri ters cevirir.
print(ters)
print(SA[:-9])# 0dan basladı -9. terime kadar yazdı. 
print(SA[-9:])#-9. terimden basladı 0 a kadar.

print(SA)
SA[2:4:1]   # [start:end:step]
SA[4:len(SA):2] #4. indexten baslayacak 2 ser 2 ser sonuncu indexe kadar gidecek.

city = "istanbul"
city[0:6:2]
"t" in city #t stringi city icinde var mı?
"z" in city
city[0:6:2]
"anb" in city
"ist" in city
s = '13'
type(int(s))

n = 10
type(str(n))
s = 'A'
# int(s)
# ValueError: invalid literal for int() with base 10: 'A'

    #captilize: İlk harften sonrası kücültür.
w = "Machine Learning"
print(w.capitalize()) 
a = "Machine Learning SAMET AI "
print(a.capitalize())
print(w.upper()) #Tum karakterler buyuk yazilir.
print(w.replace("Learning", "Samet" )) #Leraning ile Sameti yer degistirir.
#replace() fonksiyonu geri deger dondurmedi. Kayıt edilmesini istiyorsak atama yapmalıyız.
print(w) 

w2="     Machine     Learning     Samet"
print(w2.strip()) #Sol taraftaki boşlugu kaldırır.

    #input: string olarak girdi alır.
y = input("Please enter a city name: ")  #input method always takes string type. 
print(y)

x = print(input("Bir sayi giriniz: "))
type(x) #Out[107]: NoneType
z= input("Bir sayi giriniz: ")
type(z) #Out[109]: str
type(int(z)) #Out[110]: int

x = int(input("Please enter an integer: "))
print(x)

month = 12
day = 365
print('One year is ', month, 'months, and ', day, 'days.')
print('One year is ', month, 'months, and ', day, 'days.', sep =' ')
print('One year is ', month, 'months, and ', day, 'days.', sep =',')
#Tum partları virgul ile ayırır.
print('One year is', month, 'months, and', day, 'days.', sep ='')
print("One year is " + str(month) + " months, and " + str(day) + " days.")


'''Question:
Create a program will compute the tax and the tip for a meal ordered at a restaurant. 
You can compute the tax as 8 percent of the meal amount and the tip as 10 percent of the meal amount (without the tax). 
The output from your program should include the tax amount, the tip amount, 
and the grand total for the meal including both the tax and the tip.
a)Define the cost of the meal in the beginning of your program.
Some several example program runs:
Cost of the meal is 25 Eur.
Sample Run: The tax is 2.00 Eur and the tip is 2.50 Eur, making the total 29.50 Eur.
Cost of the meal is 68 Eur.
Sample Run: The tax is 5.44 Eur and the tip is 6.80000000000001 Eur, making the total 80.24 Eur.
b)Input the cost of the meal from the user.
Some several example program runs:
Please enter the cost of your meal: 100
Sample Run: The tax is 8.00 Eur and the tip is 10.00 Eur, making the total 118.00 Eur.
Please enter the cost of your meal: 68
Sample Run: The tax is 5.44 Eur and the tip is 6.80 Eur, making the total 80.24 Eur.'''

#Answer 1:
cost = 100
tax = cost*0.08
tips = cost*0.1
total = cost+tax+tips
print(f'Cost of the meal: {cost}')
print(f'The tax is {tax} Eur and the tip is  {tips} Eur,  \
      \nmaking the total {total} Eur.')
#\: koda alt satırda devam edebilmemizi sağlar. 

#Answer 2:
costUser = float(input("Please enter the cost of your meal: "))
tax = float(costUser*0.08)
tips = float(costUser*0.1)
total = float(cost+tax+tips)
print("The tax is {} Eur and the tip is  {} Eur,  \
      \nmaking the total {} Eur.".format(tax, tips,total))

#Answer 2.1: 

cost = float(input("Please enter the cost of your meal: "))
tax = cost * 0.08
tip = cost * 0.1
total = cost + tax + tip

print("The tax is " + str(tax) + " Eur and the tip is " + str(tip) + " Eur, making the total " + format(total, ".2f") + " Eur")


































    