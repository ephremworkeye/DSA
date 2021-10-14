from collections import deque

# input1 [2, 3, 4]
# input2 [-1, 2, 3] 
# result = [-2, 7, 7, 8, 2]

def multiply(A1, A2):
    # take care of multiple sign
    sign = -1 if A1[0] < 0 or A2[0] < 0 else 1
    # convert to positive incase negative
    A1[0], A2[0] = abs(A1[0]), abs(A2[0])

    # create empty array for result 
    result = deque([0] * (len(A1) + len(A2)))
    # do as normal multiplication
    for i in reversed(range(len(A1))):
        for j in reversed(range(len(A2))):
            result[i+j+1] += A1[i] * A2[j]
            result[i+j] += result[i+j+1] // 10 # integer value
            result[i+j+1] %= 10
    # we might left zero for the first element
    if result[0] == 0:
        result.popleft()
    sign * result[0]
    return result

print(multiply([-1, 2, 3], [2, 3, 4]))
print(multiply([9, 2, 3], [8, 3, 4]))
print(multiply([-9, 2, 3], [-8, 3, 4]))

# time comlexity is o(n*m)
# space complexity = o(n+m)

    
