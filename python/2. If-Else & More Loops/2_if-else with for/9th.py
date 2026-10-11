n = int(input("Enter a number: "))
s1 = ""
for i in range (1,n+1):
    if (i%2==1):
        s1 = s1 + "A"
    else:
        s1 = s1 + "B"
    print(s1)