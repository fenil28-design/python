#w.p.p to make simple calculator
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
operation=input("enter operation(+,-,*,/):")
if operation=='+':
    print("result:",num1+num2)
elif operation=='-':
    print("result:",num1-num2)
elif operation=='*':
    print("result:",num1*num2)
elif operation=='/':
    if num2!=0:
        print("result:",num1/num2)
    else:
        print("error:cannot divide by zero!")
else:
    print("invalid operation!")
