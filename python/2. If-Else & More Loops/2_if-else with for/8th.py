n = int(input("Enter a number: "))
for i in range (1,n+1):
    if(i%2==0):
        print("Square of " + str(i) + " = " + str(i**2) + " :: Even")
    else:
        print("Square of " + str(i) + " = " + str(i**2) + " :: Odd")