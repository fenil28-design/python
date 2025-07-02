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
