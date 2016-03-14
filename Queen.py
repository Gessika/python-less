# Queen's walk - on a goriz diag vertik

x1 = int(input('Input 1-8 figure: '))
y1 = int(input('Input 1-8 figure: '))
kletka1 = x1, y1
print 'Place of the first cell is: ', kletka1

x2 = int(input('Input 1-8 figure: '))
y2 = int(input('Input 1-8 figure: '))
kletka2 = x2, y2
print 'Place of the second cell is: ', kletka2

if x1 - x2 == y1 - y2: # 3 quarter
    print 'Yes, Elephan come to you'
elif x2 - x1 == - (y2 - y1): # 2 quarter
    print 'Yes, Elephan come to you'
elif x2 - x1 == y2 - y1: # 1 quarter
    print 'Yes, Elephan come to you'
elif x1 - x2 == - (y1 - y2): # 4 quarter
    print 'Yes, Elephan come to you'
else:
    print "Elephan can't go there"
