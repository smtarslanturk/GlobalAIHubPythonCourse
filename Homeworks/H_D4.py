# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:32:32 2021
@author: samet.arslanturk

Qestion:
Create 5 students. Ask these students from the user.
Each of these students should have a midterm grade, project grade and final grade.
Each students will have a course passing grade.
passingGrade = midterm*(0.3)+project*(0.3)+final*(0.4) passing grade should be determined like this.
Create a dictionary that keeps these students' information.
Calculate the students' grades and transfer them to the list with the help of indexing.
Finally, set the student with the highest grade to be in the first index and the student
 with the lowest grade to be in the last index of the list.
"""

def Grade(grades):
    passingGrade = int(grades[0] * (0.3) + grades[1] * (0.3) + grades[2] * (0.4))
    return passingGrade
    
students = {} 
for i in range(5):
    name = input("Please enter {}. student's name: ".format(i+1))
    midterm = int(input("Please enter {}. student's midterm grade: ".format(i+1)))
    project = int(input("Please enter {}. student's project grade: ".format(i+1)))
    final = int(input("Please enter {}. student's final grade: ".format(i+1)))
    students[name] = [midterm,project,final] # to put informations in the studnets dictionary
    
final_grades1 = {} 
for stname in students:
    final_grades1[stname] = Grade(students[stname]) # put students final grades and their names into the dictionary

final_grades = {}
final_grades = dict(sorted(final_grades1.items(), key=lambda item: item[1])) #sort by value.
num_val = list(final_grades.values())
num_key = list(final_grades.keys())
# position = val_num.index(max(val_num))
# firstStudent = key_num[position]
# position1 = val_num.index(min(val_num))
# lastStudent = key_num[position1]
# print(f'Firsst Student: {firstStudent} and final grade is {max(val_num)}')
# print(f'Firsst Student: {lastStudent} and final grade is {min(val_num)}')

num_val = num_val[::-1] #buyukten kucuge sıralamak icin ters cevirdik.
num_key = num_key[::-1] 
i=0;  
for i in range(len(final_grades)):
    print(f'{i+1}. Student is {num_key[i]} and point is {num_val[i]}')
