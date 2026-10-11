n = 40
r = n % 4
if (r==0):
    print('In If')
    n = n + 15
else:
    print('In Else')
    n = n - 10
print(n)