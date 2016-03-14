# Maximum of 3 input numbers, est' li treugol'nik

a = int(input())
b = int(input())
c = int(input())

if a >= b >= c:
    maxnumber = a
    print maxnumber
    
elif a <= b >= c:
    maxnumber = b
    print maxnumber
    
elif a <= b <= c:
    maxnumber = c
    print maxnumber
    
elif a >= c:
    maxnumber = a
    print maxnumber
