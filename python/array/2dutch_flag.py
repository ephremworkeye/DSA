# # dutch national flag problem
# # input  = [1, 0, 2, 0, 2, 1, 0, 2, 1]
# # output = [0, 0, 0, 1, 1, 1, 2, 2, 2]
# # we can use sorting method that will be 0(n^2) or n(log(n)) by using quick sort method
# # but for this is specifc problem we can use window sliding 
# # method with time complexity o(n) space complexity o(1)

# def dutch_national(A):
#     # we need three variables
#     left, middle, right = 0, 0, len(A)-1
#     # we do swapping, moving  while slider is less than or equal to 
#     while middle <= right:
#         # if middle element is 0, swap with the left slider and we are user that left element is 0 so we can go to the next element
#         if A[middle] == 0:
#             A[middle], A[left] = A[left], A[middle]
#             left += 1
#             middle += 1
#         # if 1, may be it is the on the right postiton or we need to next element element, which is not on the right position
#         elif A[middle] == 1:
#             middle += 1
#         #if other, that means 2, so swap the right slider with the right and decrement right by 1 and 
#         else:
#             A[middle], A[right] = A[right], A[middle]
#             right -= 1
#     return A
# print(dutch_national([1, 0, 2, 0, 2, 1, 0, 2, 1]))



# a = [1, 2, 2, 1, 0, 1, 0, 2, 0]
#               l        r
# a = [0, 0, 0, 1, 1, 1, 2, 2, 2]
#                        m

