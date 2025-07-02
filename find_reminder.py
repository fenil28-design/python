#remider find

def find_reminder(num,z):
     return num%z
   
num=int(input("enter the num"))
z=int(input("enter the Z"))

if z==0:
  print("no reminder")
else:
  reminder=find_reminder(num,z)
  print(f"reminder when {num} divided by {z} then reminder is:",reminder)
