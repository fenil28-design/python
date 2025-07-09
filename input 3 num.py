a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))

if a==b==c:
    print("all sam")
elif a==b:
    print("a and b sam")
elif a>b and a>c:
    print("a is greatar")
#if a==b==c:
    #print("all sam")
elif b==c:
    print("b and c sam")
elif b>a and b>c:
    print("b is greatar")
#if a==b==c:
    #print("all sam")
elif a==c:
    print("a and c sam")
elif c>a and c>b:
    print("c is greatar")