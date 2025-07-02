#Types of loop
#1.for loop
#2.while loop


#python code which help's you can create multiplication table using user input.

#while loop
n=int(input("Enter The Number"))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i=i+1

#for loop
n=int(input("Enter The Number"))
for i in range(1,11): 
    print(n,"x",i,"=",n*i)
    
#print 1 to 100.

#for loop
print("1 to 100")
for i in range(1,101):
    print(i)
    
#while loop
print("1 to 100")
i=1
while i<=100:
    print(i)
    i=i+1
    
#print 100 to 1.
#while loop
print("100 to 1")
i=100
while i>=1:
    print(i)
    i=i-1
    
#Break Statement in loop
print("break statement in loop")
i=1
while i<=5:
    print(i)
    i=i+1
    if(i==3):
        break


#continue statement in loop
print("continue statment in loop")
i=1
while i<=5:
    print(i)
    i=i+1
    if (i==3):
        i+=1
        continue
        
#string in loop
print("string find using loop and conditional statment")
str="fenildesai"
for char in str:
    if(char=="d"):
        print("d is found")
        
#first 10 natural number total using loop
print("sum of first 10 natural number")
n=10
sum=0
for i in range(n+1):
    sum+=i
    print(sum)
        
  
#loop pattern
row=10
for i in range(1,row+1):
    for j in range(i):
        print("`",end="")
    print()