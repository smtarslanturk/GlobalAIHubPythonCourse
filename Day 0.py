# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:49:04 2021

@author: samet.arslanturk
"""
    
    # Global AI Hub tarafında yapılan eğtimlerde kullanılan kodlarla alakalı olusturulmus bir repodur.
    # Kod parcalarının incelenmesi sonucu elde edilen cıktıların hepsi yorum satırları olarak eklenecektir. 
    # Github Page: 
    #     https://github.com/globalaihub/introduction-to-python/blob/master/Day0.ipynb

    # What is Python:
    # Python is an interpreted, high-level and general-purpose programming language.
    # object-oriented approach aim to help programmers write clear
    # dynamically typed and garbage-collected.
    # Python was created in the late 1980s by Guido van Rossum

print("Hello World")
print('Hello World')
# Print fonksiyonu icerisinde string degerleri tek veya cift tırnak icerisinde yazılabilir.

print("Samet Arslanturk Merhaba")
print("Samet Arslantürk Hoş Geldin")
# Türkce ingilizce karakter bakımından UTF formatında sıkıntı cıkmadıgı icin türkce karakterleride gorebiliyoruz.

    # print"samet Arslanturk"
    # invalid syntax hatası alıncaktır.
    # print(Hello)
    # name 'Hello' is not defined
    # Hatalara dikkat edilmelidir!!

    
    # Comments:
"""write something"""

''' Yorum satırı yazmak amacıyla 3x' veya 3x" yapısı kullanılabilecegi gibi 
# isaretini de kullanabilrisiniz. 
CTRL+1: Secili olan satırları kısa yoldan komut satırı yapar. '''

''' Samet Arslanturk ''' .replace("S", "A")
#.replace fonksiyonu ile yazılı olan karakterler yer degistirir. 

    #Declaring Variables:
n=1;
print(n)
p=n;
print(p)

    # Data Types:
        # Integer
        # Float
        # String
        # Boolean
        # Complex
        # Dictionary
        # Tuple
        # Set
#String
hello = "World"

print(hello) #print variable
print("World") #print value
print(n)  #Print int.

type(n)
type(hello)
#type(): Degiskenlerin turlerini gormemize yarayan fonksiyondur.
print(type(hello))
# print(type(Hello))

t=3.19; #Float: ondalıklı sayılar.
print(type(t))

#Boolean
#0 veya 1 den olusan veri turudur.
t, f = True, False
print(type(t))
print(t)
print(f)

#Swapping:
data1 = 7 
data2 = 12
data3 = 23
data4 = 33
print(data1, data2, data3, data4)

data11, data22, data33 , data44 = data2 , data1, data4, data3
print(data1, data2, data3, data4)

print("Data1: ", data1, " Data2: ", data2)
#String-int ifadeleri print fonk. İçerisinde kullanabiliriz.

#length ifadesi bir string değerin uzunluğunu bulmamıza yarar.
len("Pythoneer")
Samet = "Samet Arslanturk"
print(len(Samet)) #16 karaktere sahip oldugunu goruruz. 
type(len("Pythoneer")) #Int
type(print(len(Samet))) #NoneType
# 16
# Out[79]: NoneType
len(14) #object of type 'int' has no len()

#F-string
name = "Turkey"
print(f'hello {name}')
print(f'hello name')
print(f'hello {name}')
print("Hello", name)
print("Helo"+name)
# print("Helo" name) invalid syntax
print("hello", name, 61)

name2 = "Ankara";
print("Türkiyenin Başkenti: {}".format(name2))
print("Dogum Tarihi: {}, Yıl: {}".format(2005, 2021))
print(f'Dogum Tarihi: {2005}, Yıl: {2021}')

dogum = 2005
yil = 2021
print(f'Dogum: {dogum}, Yil: {yil}')
print("Dogum: {}, Yil: {}".format(dogum, yil))

# print("Dogum: "+ dogum)
# TypeError: can only concatenate str (not "int") to str
print("Dogum: "+ str(yil), "Yil: "+ str(yil))
print("Dogum:", dogum, "Yil:", yil)

a = 50
type(a) #int deger
type(str(a)) #string deger

    # Aritmetic Operations:
5*2 #Carpma
5**2 #Ust alma
"35"+"32"
type("35"+"32")  
a= 35+32
# type(a)
# TypeError: can only concatenate str (not "int") to str
"3"*3
type("3"*2)

x = 10
print(x+2)
print(x-2)
print(x*2)
print(x**2) #ust alma
print(x**4)
print(x/2) #Bolme
print(x//2) #Virgulden sonra gosterme
print(x%2)

y = 5.2 #Float
print(y/2) #Float formatında virgulden sonra gosterir.
print(y//2) #Float formatında virgulden sonra gostermez.

z = 5
z+=1 # z= z+1.
z

z*=2 # z= z*2
z


























