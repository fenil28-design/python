#1 to 100 without loop
def print_number(n):
    if n<=100:
        print(n)
        print_number(n+1)
print_number(1)
