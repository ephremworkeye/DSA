# # plus one problem
# # input = [2, 3, 9]
# # output = [2, 4, 0]
# # input = [9, 9, 9]
# # output = [1, 0, 0, 0]
# # input = []
# # output = []
# # input = [2, 3, 8]
# # output = [2, 3, 8]

# # parsing is not allowed
# # no additonal storage space complexity 0(1)
# # solve with 0(n) time complexity

# def plus_one(A):
#     # if empty return empty
#     if len(A) == 0:
#         return A
#     # add 1 to the last element
#     A[-1] += 1
#     # iterate through the array in reversed way and stop at position 0
#     for i in range(len(A)-1, 0, -1):
#         # if it is not 10 break the loop and return the array
#         if A[i] != 10:
#             break
#         # if 10 add make the current element 0 and add 1 to the previous elemenet as the normal addition method
#         else:
#             A[i] = 0
#             A[i-1] += 1
#     # in array insertion and deletion at the back side of the array is 0(1) so if sum of the first element is 10, 
#     # we append 0 to the last element and we put one to the first element
#     if A[0] == 10:
#         A.append(0)
#         A[0] = 1
#     return A  
# print(plus_one([]))
# print(plus_one([1, 3, 9]))
# print(plus_one([9, 9, 9]))

    

