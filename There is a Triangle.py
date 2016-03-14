# There is a Triangle ???

a = int(input())
b = int(input())
c = int(input())

if a >= b >= c: #determination of the max side for each variant 
    maxside = a
    side1 = b
    side2 = c
    print maxside
    
elif a <= b >= c:
    maxside = b
    side1 = a
    side2 = c
    print maxside
    
elif a <= b <= c:
    maxside = c
    side1 = a
    side2 = b
    print maxside

elif a >= c:
    maxside = a
    side1 = b
    side2 = c
    print maxside

if maxside <= side1 + side2:
    print 'Yes, triangle exist'
else:
    print "No, triangle can't exist"
    
