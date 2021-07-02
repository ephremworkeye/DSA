# sum
def sum_array(A):
    total = 0
    for num in A:
        total += num
    return total
print(sum_array([2, 3, 4 , 5]))

# find min

def min_value(A):
    min = A[0]
    for num in A:
        if num < min:
            min = num
    return min

print(min_value([5, 2, 4, 1, 9]))

# find max
def max_value(A):
    max = A[0]
    for num in A:
        if num >max:
            max = num
    return max

print(max_value([5, 2, 4, 1, 9]))

# find average
def average(A):
    total = 0
    for num in A:
        total += num
    return total / (len(A)-1)

print(average([5, 2, 4, 1, 9]))