#how to find prime number using python program.
#prime number in guj is avibhajy number
number=int(input("enter the number"))
flag=False
if(number==0 or number==1):
    print(number,"number,is not prime number")
elif(number>1):
    for i in range(2,number):
        if(number%i)==0:
            flag=True
            break
        if flag:
            print(number,"the number is prime")
        else:
            print(number,"the number is not prime")
            #this program is run but not work withoput error but problem
