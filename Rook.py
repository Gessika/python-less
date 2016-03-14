# Does Rook can to beat?

x1 = int(input('Input 1-8 figure: '))
y1 = int(input('Input 1-8 figure: '))
kletka1 = x1, y1
print 'Place of the first cell is: ', kletka1

x2 = int(input('Input 1-8 figure: '))
y2 = int(input('Input 1-8 figure: '))
kletka2 = x2, y2
print 'Place of the second cell is: ', kletka2

if kletka1 != kletka2:
    if x1 == x2 or y1 == y2:
        print 'Rook beats!'
    else:
        print "Rook can't to beat"

else:
    print "Cells are match! Please, re-Run program and choose another one."
