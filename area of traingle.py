#write a python program to find area of triangle
a=int(input("enter the first side of traingle"))
b=int(input("enter the second side of triangle"))
c=int(input("enter the third side of triangle"))
semi=(a++b+c/2)
area=(semi*(semi-a)*(semi-b)*(semi-c))**0.5
print("area of triangle",area)

#w.p.p.to find area of triangle
base=float(input("enter the traingle base:"))
height=float(input("enter the traingle height"))
area=0.5*base*height
print("Area of traingle:",area)
