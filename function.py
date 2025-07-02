#fuction types
#1.built in function
"""
1.print()
2.len()
3.type()
4.range()
"""
#2.user-define function

#programs

#basic function with parameter and argument
def avg(a,b,c):
    sum=a+b+c
    av=sum/3
    print(av)
avg(5,5,6)

#print the length of list using function
list=["python","java","c++"]
def print_len(list):
    print(len(list))
print_len(list)

#factoraial

num=int(input("enter the number:"))
def fact(num):
    if num<=1:
        return 1
    else:
        return num*fact(num-1)
print(fact(num))

#convert usd to inr


def convert(usd):
    inr=usd*83
    print("usd to inr is:",inr)
usd=int(input("enter the number:"))
convert(usd)