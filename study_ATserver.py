# Visokosnij GOD - calculation HI year

x = int(input())

if x % 4 == 0 and x % 100 == 0:
    if x % 400 == 0:
        print 'YES'
    else:
        print "NO"
        
elif x % 4 != 0:
    print "NO"
elif x % 4 == 0:
    print 'YES'
