import numpy as np
from numpy import int64

# aisle --> a, window --> w, center --> c, else --> X

# Input from the user
sub_list=int(input ("enter the size of list: "))
x=[]
input_array=[]
for i in range(0,sub_list):
    x.append(int(input()))
    x.append(int(input()))
    input_array.append(x)
    x = []
print(input_array)

passengers=int(input("Enter number of passengers :"))

# Finding the maximum number of rows
max_row=0
for i,j in input_array:
    max_row=max(max_row,j)

# Converting each row and column into a matrix
def convertmatrix(i,j):
    matrix=[[-1 for _ in range(i)] for _ in range(j)]
    return matrix

def resizeMat(input_array):
    res=[]
    for i,j in input_array:
        m=convertmatrix(i,j)
        for x in range(len(m)):
            for b in range(len(m[0])):
                if b==0 or b==len(m[0])-1:
                    m[x][b]='a'
                else:
                    m[x][b]='c'
        m=np.array(m)
        m.resize(max_row*i)
        m = m.reshape(max_row,i)
        if len(m[0])!=max_row:
            z = np.zeros((max_row,max_row-len(m[0])), dtype=int64)
            m=np.append(m, z, axis=1)
        res.append(m)
    return res

# Concating all the individual matrices
def concatMat():
    ans=resizeMat(input_array)
    new_matrix=ans[0]
    for i in range(1,len(ans)):
        new_matrix=np.concatenate((new_matrix, ans[i]), axis=1)
    return new_matrix

# Replacing values for better understanding
def replaceValues(new_matrix):
    for i in range(len(new_matrix)):
        if new_matrix[i][0]=='a':
            new_matrix[i][0]='w'

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])-1,-1,-1):
            if new_matrix[i][j]=='0':
                new_matrix[i][j]='X'
            if new_matrix[i][j]=='a':
                new_matrix[i][j]='w'
                break

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            if new_matrix[i][j]=='' or new_matrix[i][j]=='0':
                new_matrix[i][j]='X'
    return new_matrix

# Counting the number of seats available for passengers
def count_seats(matrix):
    c=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='c' or matrix[i][j]=='w' or matrix[i][j]=='a':
                c+=1
    return c

# Replacing the values based on rule
def replace(matrix,passengers):
    c=0
    while c!=passengers:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if c!=passengers and matrix[i][j]=='a':
                    c+=1
                    matrix[i][j]=int(c)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if c!=passengers and matrix[i][j]=='w':
                    c+=1
                    matrix[i][j]=int(c)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if c!=passengers and matrix[i][j]=='c':
                    c+=1
                    matrix[i][j]=int(c)

    return matrix

# replacing X to space for better visialization
def replaceX(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='X':
                matrix[i][j]=' '
    return matrix
new_matrix=concatMat()
final_matrix=replaceValues(new_matrix)
count=count_seats(final_matrix)

if count>=passengers:
    print("Welcome")
    matrix=replace(final_matrix,passengers)
    print(replaceX(matrix))
else:
    passengers-=(passengers-count)
    print("No more passengers allowed")
    matrix=replace(final_matrix,passengers)
    print(replaceX(matrix))






