#list and tuple
#print list using user input

fruits=[]
for i in range(4):
  fruit=input(f"Enter The Fruits Name:{i+1}")
  fruits.append(fruit)
print(fruits)


#print sum of list using user input
number=[]
for i in range(3):
    num=int(input(f"Enter the number{i+1}"))
    number.append(num)
total=sum(number)
print(f"number is{number}")
print("sum of number",total)


#Write a program to count the number of zeros in the following tuple

a = (7, 0, 8, 0, 0, 9) 
print(f"list:{a}")
zero_count=a.count(0)
print(f"Number of zeros in list is:{zero_count}")
  
#Write a program to accept marks of 6 students and display them in a sorted manner.

Marks=[]
for i in range(5):
  mark=int(input("Enter The marks of Students:"))
  Marks.append(mark)
print("marks of students is:",Marks)
Marks.sort()
print(Marks)