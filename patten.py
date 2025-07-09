
    #normal patten of 1 to5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
    
    # to change number of patten to use a easy trick to change j value or add 
    # number what you want to in print statement to set a new pattern
    
    
for i in range(1,6):
    for j in range(1,i+1):
        print(j+4,end="")
    print()    

#another pattern like 1 3 5 7  to assign

for i in range(1,6):
    k=1
    for j in range(1,i+1):
        print(k,end="")
        k=k+3
    print()

