# # input = [2, 3, 5, 5, 5, 8, 8, 10]
# # output = [2, 3, 5, 8, 10]


# # using extra space

# # def delete_dup(alist):
# #     if len(alist) <=1:
# #         return alist
# #     res = []
# #     res.append(alist[0])
# #     for i in range(1, len(alist)):
# #         if alist[i] != alist[i-1]:
# #             res.append(alist[i])
# #     return res

# # print(delete_dup([2, 2, 3, 5, 5, 8, 8, 8, 10]))


# def delete_dup(alist):
#     if len(alist) <=1:
#         return alist
#     res = []
#     for i in range(len(alist)-1):
#         if alist[i] != alist[i+1]:
#             res.append(alist[i])
#     return res

# print(delete_dup([2, 2, 3, 5, 5, 8, 8, 8, 10]))



#        l
# [2, 3, 5, 5, 8, 8, 8, 10]
#     r         

# def delete_duplicate(A):
#     if len(A) <= 1:
#         return A

#     left, right, end = 1, 1, len(A)-1
#     while right <= end:
#         if A[right] != A[left -1]:
#             A[left] = A[right]
#             left += 1
#         else:
#             right += 1
#     while end >= left:
#         A.pop()
#         end-=1
#     return A

# print(delete_duplicate([2, 3, 5, 5, 8, 8, 10]))



#           r               
# a  = [2, 3, 4, 4, 4, 5, 5]
#       l         

def del_dup(alist):
    right = 1
    for left in range(len(alist)):
        if alist[left] != alist[right-1]:
            alist[right] = alist[left]
            right += 1


    return right

print(del_dup([2, 5, 5, 5, 8, 8, 10]))




