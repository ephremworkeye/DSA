# two sum array which is not sorted
# we can solve this by nesting which will take o(n^2)
# we can sort first which will take o(n^2) and scan from sorted array which takes o(n)
# we can reduce from o(n^2) time complexity to o(n) time complexity but on the cost of o(n) space complexity
# we need other storage to store revisited elements from array best candidate for this hashing 
# because searching element using key is constant

def two_num_sum(A, sum): 
     if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    d = {}
    for i in range(len(A)):
        # we need to store the difference of sum and current element for later checking
        diff = sum - A[i]
        # if we don't find the difference in d, we need to store the element with its index to the dictionary
        if diff not in d:
            d[A[i]] = i
        else:
            # else we found the the difference, so we return the index of previous element and currnet index
            return d[diff], i
    # if not found 
    return None

print(two_num_sum([4, 1, 6, 3, 7 ,8, 2, 24], 100))
print(two_num_sum([4, 1, 6, 3, 7 ,8, 2, 24], 10))


    