n = 12
ff= 0
for i in range(1,9):
    a = n%i
    if (a==0):
        ff= ff+ 1
print("Count="+str(ff))