# we can solve this problem by using nested but it's o(n^2)
# we can use hash map to check and we can copy the unique number to new array (that will take additional storage but still it is o(n) )
# but we can avoid additional storage  for storing instead we can do onplace using window sliding

def delete_duplicate(A):
    # if empty or one element in array return and we don't need to go the next
    if len(A) <=1:
        return A
    d = {}
    # we need empty dict and two pointers left and right
    left, right = 0, len(A)-1
    while left <= right:
        # if element not in dict, add to dict and go to next
        if A[left] not in d:
            d[A[left]] = left
            left += 1
        # if it is already in dict, that means it is duplicate and we can replace the last element to current and decrement
        #  the last element
        else:
            A[left] = A[right]
            right -= 1
    # if out of loop  we need to reset the last elment and iterate unitl the left index, remove element by poping(deleting the last element) which is constant in time
    right = len(A)-1
    while right >= left:
        A.pop()
        right -= 1
    return A
    return A

print(delete_duplicate([4, 2, 4, 1, 4, 5, 3, 5])) #[4, 2, 1, 5, 3]
print(delete_duplicate([1, 1, 1])) #[1]
print(delete_duplicate([1])) #[1]
print(delete_duplicate([])) #[1]

