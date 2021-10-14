# input = [3, 3, 1, 0, 2, 0, 0] =True
# input = [3, 2, 0, 0, 2, 0, 1] =False

def can_reach(A):
    remaining, i = 0, 0
    while i < len(A)-1:
        remaining = max(remaining, A[i])
        if remaining == 0:
            return False
        i, remaining = i + 1, remaining -1
    return True

print(can_reach([3, 3, 1, 0, 2, 0, 0]))
print(can_reach([3, 2, 0, 0, 2, 0, 1]))


# time complexity 0(n)
# space complexity 0(1)



