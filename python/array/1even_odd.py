# # even odd problem
# # even first and odd
# # solve the problem with out allocating additional storage
# # time complexity o(n) becuase we need to scan the whole array

# def even_odd(A):
#     # we need to use window sliding technique
#     i, j = 0, len(A)-1
#     while i<j:
#         # if it is odd, swap and decrement right side by  1
#         if A[i] % 2 != 0:
#             A[i], A[j] = A[j], A[i]
#             j-=1
#         # else that means it is even go to the next element and increment by 1
#         else:
#             i+= 1
#     return A

# print(even_odd([2, 3, 9, 4, 5, 8]))

