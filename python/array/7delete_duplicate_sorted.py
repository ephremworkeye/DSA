# input = [2, 3, 5, 5, 5, 8, 8, 10]
# output = [2, 3, 5, 8, 10]

#           i
# [2, 3, 5, 8, 10, 8, 8, 10]
#            

def delete_duplicate(A):
    if len(A) <= 1:
        return A

    left, right, end = 1, 1, len(A)-1
    while right <= end:
        if A[right] != A[left -1]:
            A[left] = A[right]
            left += 1
        else:
            right += 1
    while end >= left:
        A.pop()
        end-=1
    return A

print(delete_duplicate([2, 3, 5, 5, 8, 8, 10]))


