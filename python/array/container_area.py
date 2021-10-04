# brute force solution
# def container_area(A):
#     total_area = 0
#     for i in range(len(A)):
#         current_area = 0
#         for j in range(i+1, len(A)):
#             width = j-i
#             length = min(A[i], A[j])
#             current_area = max(current_area, width * length)
#         total_area = max(total_area, current_area)
#     return total_area

# print(container_area([2, 7, 9, 3, 1, 5]))
# print(container_area([7, 1, 2, 3, 9]))
# print(container_area([6, 9, 3, 4, 5, 8]))


# optimal solution
def container_area(A):
    if len(A) <= 1:
        return 0
    left, right, max_area = 0, len(A)-1, 0
    while left < right:
        height = min(A[left], A[right])
        width = right - left
        current_area = height * width
        max_area = max(max_area, current_area)
        if A[left] < A[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(container_area([2, 7, 9, 3, 1, 5]))
print(container_area([7, 1, 2, 3, 9]))
print(container_area([6, 9, 3, 4, 5, 8]))