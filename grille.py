import sys

def rotatePoint(x,y,n): # Receive a point of a matrix nxn and return the point with a rotation of 90
    (x,y) = (x, (n-1)-y)  # New position of the point int the case that if the row was reversed
    (x,y) = (y,x)  # Transpose the point in a matrix nxn
    return (x,y)

def rotateHoles(holes, n, clockwise): # n: size matrix, clockwise: true indicate rotate clockwise and false indicate rotate anticlockwise
    for i in xrange(len(holes)):  # Iterate for each hole
        if clockwise:
            (holes[i][0], holes[i][1]) = rotatePoint(holes[i][0], holes[i][1], n) # rotate clockwise hole
        else:
            (holes[i][1], holes[i][0]) = rotatePoint(holes[i][1], holes[i][0], n) # rotate anticlockwise hole
    holes = sorted(holes) # Sort the points
    return holes

def printMatrix(Matrix): # Function for print a matrix orderly and print the matriz as a phrase in line
    message = ""    # Variable that will contain the message in as a phrase in line
    print
    print "The cipher matrix is: "
    for x in Matrix:    # Loop over the matrix
        for y in x:
            print y,    # Print each element of the matrix
            message = message + y   # Acumulate all letters of the message
        print
    print
    print "The cipher message in line is: "
    print message  # Print the message

print "Insert the size of the grid: "
n = int(sys.stdin.readline().strip()) # get the size of the grid
print "Insert rotation: [0] clockwise - [1] anticlockwise: "
temp = int(sys.stdin.readline().strip()) # direction of rotation
clockwise = True
if temp == 1:
    clockwise = False
print "Insert procedure: [0] cipher - [1] decipher: "
cipher = int(sys.stdin.readline().strip()) # action, cipher or decipher
print "Insert the numbers where the holes will be: "
i = 0
for x in xrange(n):  # Print matrix to choose the holes
    for y in xrange(n):
        if i < 10:
            print str(i) + " ",
        else:
            print i,
        i += 1
    print
print
temp = map(int, sys.stdin.readline().split()) # get the holes in list
temp = list(set(temp))   # delete repeated
holes = []
for i in temp:
    holes.append([i/n, i%n])
holes = sorted(holes)
print "Insert the message: "
message = sys.stdin.readline().strip() # Get the message
print message
if cipher == 0:
    Matrix = [[" " for x in xrange(n)] for y in xrange(n)] # Create matrix nxn
    repeated = [[False for x in xrange(n)] for y in xrange(n)] # Matrix to avoid overwrite holes overlapped
    for z in xrange(len(message)):  # Loop each word in the message
        if z % len(holes) == 0 and z != 0: # chech if all holes for rotation have letters
            holes = rotateHoles(holes, n, clockwise)    # Rotate holes of the matrix
        if  not repeated[holes[z%len(holes)][0]][holes[z%len(holes)][1]]:
            repeated[holes[z%len(holes)][0]][holes[z%len(holes)][1]] = True
            Matrix[holes[z%len(holes)][0]][holes[z%len(holes)][1]] = message[z] # Put each letter on the holes of the matriz
    printMatrix(Matrix)     # Print the matrix
else:
    M = ""
    repeated = [[False for x in xrange(n)] for y in xrange(n)] # Matrix to avoid overwrite holes overlapped
    for z in xrange(4):  # Loop 4 times, each time is a rotation
        for w in holes:     # Loop the holes of the matrix
            if  not repeated[w[0]][w[1]]:
                M = M + message[w[0]*n+w[1]]    # Accumulate each letter per appropriate hole
                repeated[w[0]][w[1]] = True
        holes = rotateHoles(holes, n, clockwise)    # After loop all holes, do a rotation
    print "The original message is: ",M  # Print the original message