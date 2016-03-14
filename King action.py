# King action

x1 = int(input('Input 1-8 figure: '))
y1 = int(input('Input 1-8 figure: '))
kletka1 = x1, y1
print 'Place of the first cell is: ', kletka1

x2 = int(input('Input 1-8 figure: '))
y2 = int(input('Input 1-8 figure: '))
kletka2 = x2, y2
print 'Place of the second cell is: ', kletka2

if x2 == x1: #Search for element in the same row
    if y2 == y1 - 1 or y2 == y1 + 1:
        print 'King can go here'
    else:
        print 'No, King can"t go there'

elif y2 == y1: #Search for element in the same column
    if x2 == x1 - 1 or x2 == x1 + 1:
        print 'King can go here'
    else:
        print 'King can"t go there'
        
elif x2 - x1 == 1 or x1 - x2 == 1: #Search for element in the near corner
    if y2 == y1 - 1 or y2 == y1 + 1:
        print 'OK, King can go here'
    else:
        print 'King can"t go there'
else:
    print 'King can"t go there'
        
