import sys
import numpy
import fractions

def adj(A): # Find the adjucate matrix of A
    (A[0,0], A[0,1], A[1,0], A[1,1]) = (A[1,1], -A[0,1], -A[1,0], A[0,0])
    return A

def EEA(a,b): # Extended Euclidean Algorithm where b = 26 (the modulo), a = determinant of the matrix
              # and x is the modular inverse of a
    if b == 0:
        return (a, 1, 0)
    (d1, x1, y1) = EEA(b, a%b)
    (d, x, y) = (d1, y1, x1 - (int(a/b))*y1)
    return (d, x, y) # return result where ax + by = d

def inverse(m, modulo): # Find the inverse the matrix m in the respective modulo
    modInverse = EEA(int(numpy.linalg.det(m)), modulo)[1] # Find the modular inverse of the determinant of m
    return (modInverse*adj(m))%26   # return the inverse the matrix m

print "Options [1] cipher, [2] decipher : "
option = int(sys.stdin.readline().strip()) # get the option
if option == 1:         # if it's a plaintext
    print "Insert the message: "
else:                   # if it's a encrypted message
    print "Insert the encrypted message: "
mess = sys.stdin.readline().strip().upper()
if len(mess) % 2 == 1: # if the lenght of the message is odd, add a letter (x) to avoid errors
    mess += "X"
print mess          # print the message include changes, (if have a letter at the end)
incorrectMatrix = True      # Control variable in case of non-invertible matrix
while incorrectMatrix:
    print "Insert the key (the matrix): "
    m = []
    m.append(map(int, sys.stdin.readline().split())) # get the matrix
    m.append(map(int, sys.stdin.readline().split()))
    detM = int(numpy.linalg.det(numpy.matrix(m)))
    if fractions.gcd(detM,26) != 1: # in case of the matrix is non-invertible
        print "The matrix (key) is non-invertible, try again"
    else:
        incorrectMatrix = False # in case of the matrix is invertible

m = numpy.matrix(m)  # transform the matrix to operate
temp = 1        # Control variable to split the message (encrypted or not) in groups of two
messTwo = []    # Control variable to split the message (encrypted or not) in groups of two
messAllTwo = []  # It will contain the array with the message in groups of two
for char in mess:
    messTwo.append(ord(char)-65) # transform the letters from ascii code to number from 0 to 25
    if temp % 2 == 0:
        messAllTwo.append(messTwo)
        messTwo = []
    temp += 1
convertMess = "" # It will contain the encrypted message if the case is encrypt or vice versa
if option == 2:   # In case of Decrypt find the inverse of the matrix
    m = inverse(m, 26)  # Convert m (original matrix) in the inverse matrix
for i in messAllTwo:    #Loop each group of two of the message
    i = numpy.squeeze(numpy.asarray(i*m)) # Multiply the matrix with each group of two of the message
    for j in i: #Loop the two number of the i-th
        convertMess += chr((j%26)+65)   #convert the number in letter
# Show results
if option == 1:
    print "The encrypted message is:", convertMess
else:
    print "The original message is:", convertMess
    print "The inverse matrix of the key is:"
    print m