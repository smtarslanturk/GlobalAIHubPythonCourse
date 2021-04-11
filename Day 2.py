# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 07:50:01 2021

@author: samet.arslanturk
"""
    # Lists:
myList = [2,3,4,5,6]
print(myList)
type(myList)

print(myList[0]) #index sıfırdan baslamaktadır.
print(myList[4])
# print(myList[7])
# IndexError: list index out of range

print(myList[-2]) #İndex boyutu kadar - ye gidilebilmektedir. 

myList[2] = "python"   # lists can be taken different types of data
print(myList)

myList.append('course')  # append(): adding some items end of the list 
print(myList)
print(myList[2:]) #2den sonra kadar yazar.
print(myList[2::2]) #2den sonra kadar 2 atlayarak yazar.

myList.append('course')
myList.append('course') #append() surekli kullanılabilen fonksiyondur.
print(myList)

thelast = myList.pop()  # pop(): removing the last item of the list 
print(thelast)

print(myList)
z = myList.pop(0)  #Eger index yazılırsa o indexi kaldırmaktadır. 
print(myList)
# myList.index()
# TypeError: index expected at least 1 argument, got 0
myList.index("course")
#Coursenin 2. indexte tutuldugunu söyler.
# myList.index(2)
# ValueError: 2 is not in list -> Listede olmayan bir deger oldugunu soyler.
    #count(): kac tane isaretlenen degerden oldugunu soyler.
list2 = ["Python","Java","R","JavaScript","Ruby","Python","Python"]
list2.count("Python")  #-> 3
list2.count("python")  #-> 0
#Python buyuk-kucuk harf ayrımı vardir. 

    #remove(): Sırayla istenen degiskeni kaldıracaktır.
print(list2)
list2.remove("Python") #İlk gordugu pythonu kaldırdı.
print(list2)
list2.remove("Python")
print(list2)
# list2.remove("Python")
# ValueError: list.remove(x): x not in list -> listede olmayan eleman oldugu icin hata aldik.

    #sort(): int/float listeyi sıralamaya yarar.
list4 = [100, 50 , 20, 2021]
list4.sort() 
print(list4)
list5 = [100.2, 23.4, 1.2, 3]
type(list5)
list5.sort()
print(list5)
type(list5[3]) #->float
list5 = [100.2, 23.4, 1.2, int(3)]
type(list5[3]) #->int
list5.sort()
print(list5)
# list5.remove()
# TypeError: remove() takes exactly one argument (0 given)

list6 = [41,23,78,99,37,'python']
# list6.sort()
#TypeError: '<' not supported between instances of 'str' and 'int'
list6[0]
list6[0]
list6[0]

# i=0;
for i in list6:
    print("Type of array element: {}".format(i))
#i degiskeninde sırasıyla index degerlerini tutuyor.

# list6.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'

    # reverse: Listeyi ters cevirir.
mylist = [3,4,5,6,7]
mylist.reverse()
mylist
# Out[219]: [7, 6, 5, 4, 3]
mylist1 = [3,4,5,6,7]
mylist1[::-1] #reverse etmenin baska bir yolu.

mylist2 = ["python", "course", "hello"]
mylist2.sort()  #String oldugu icin alfabetik olarak sıralama yapar.
mylist2
    
    #extend(): you want to add multiple elements to the list, you can use this method.
    #extend(): Liste eklemek icin kullanılabilir. Yeni indisler ekler.
    #append(): Son satıra tek bir indis ekler.
a = [1, 11, 111, 1111]
a.extend(a) #aynı listeyi yan yana ekledi.
a

x = [1, 2, 3]
x.extend([4, 5])
x

y= [1, 2, 3]
y.extend([1,2, "element"]) 
y

y= [1, 2, 3]
y.append([1,2, "element"]) 
y

    #append(): The append() method adds a single element towards the end of a list.
    #Sadece 1 arguman alır. 
b = [10, 110, 1110, 11110]
b.append(12)
print(b)

# c = [10, 110, 1110, 11110]
# c.append[41]
# TypeError: 'builtin_function_or_method' object is not subscriptable

months = ['January', 'February', 'March']
months.append('April')
print(months)

list_in_list = ["python","Java",3.2, 4, 11, [5,65,7,8,9]]
print(list_in_list[5])
list_in_list[-1]




    # For Loop Structure:
    # for "repeated value" in "list":
    # "true statement"
    # It takes the items as in sequence and processes them in a loop.

a=[1,2,32]
for i in a:
    print(i)





















#Input fonk. herzaman string deger dondurur. 
# append() herhangi bir deger dondurmez. Arguman almak zorundadır.
# pop() islemi yaptıktan sonra deger dondurur. pop() arguman aladabılır almayadabilir.
#reverse() kalıcı degısıklık yapar. 
# [::-1] ise kalıcı degısıklık yapmaz. Kalıcı olmasını ıstıyorsan atama yapmalısın.
# Fonk. tekrar tekrar calıstırılma ozellıgı vardır ama hepsi sahip degildir. 
