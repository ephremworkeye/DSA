# solve two sum problem with sorted array
# this solution can be easily solved by nesting but with cost of n^2
# and also can be solved using hash but with cost of o(n) time comlexity
# since it is sorted array, we can use window sliding technique by checking element in two sides
def two_num_sum(A, sum):
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    left, right = 0, len(A)-1
    while left < right:
        if A[left] + A[right] == sum:
            return left, right # returning the indexd
        # if sum of left and right > sum,  that means we need to find smaller element and decremnet 
        elif A[left] + A[right] > sum:
            right -= 1        
        # if sum of left and right > sum,  that means we need to find greater element and increment 
        else:
            left +=1
    # if not found 
    return None

print(two_num_sum([2, 4, 5,  7, 9, 14, 20], 12))
print(two_num_sum([2, 4, 5,  7, 9, 14, 20], 34))

    