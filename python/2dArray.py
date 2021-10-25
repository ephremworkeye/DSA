"""
rotate two d array 90 degree
input A = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10],
]

output = [
    [8, 5, 2],
    [9, 6, 3],
    [10, 7, 4]
]
"""

# brute force solution is to use extra space and copy first row to last column and row increased column decreased
# we need extra pointer for new space to track the column every time started from zero
def rotate_2d(A):
    space = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for i in range(len(A)):
        start_col = 0
        for j in range(len(A)-1, -1, -1):
            space[i][start_col] = A[j][i]
            start_col += 1

    return space

print(rotate_2d([[2, 3, 4], [5, 6, 7], [8, 9, 10]]))
print(rotate_2d([[2, 3], [4, 5]]))