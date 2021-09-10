# # sum
# def sum_array(A):
#     total = 0
#     for num in A:
#         total += num
#     return total
# print(sum_array([2, 3, 4 , 5]))

# # find min

# def min_value(A):
#     min = A[0]
#     for num in A:
#         if num < min:
#             min = num
#     return min

# print(min_value([5, 2, 4, 1, 9]))

# # find max
# def max_value(A):
#     max = A[0]
#     for num in A:
#         if num >max:
#             max = num
#     return max

# print(max_value([5, 2, 4, 1, 9]))

# # find average
# def average(A):
#     total = 0
#     for num in A:
#         total += num
#     return total / (len(A)-1)

# print(average([5, 2, 4, 1, 9]))

# L = ['a', 'b', 'c', 'd', 'e', 'f']
# # print(L[::-1])
# # L.reverse()
# # print(L)
# another = [char for char in reversed(L)]
# print(another)


# Suppose you want to generate a list of integers from 1 to 100, but excluding all square numbers, 
# such as 1, 4, 9, ..., 100. You will fill the loop and condition to check whether n is a square number. 
# hint: if n is a square number, then we can always find an integer i as the square root of n. You don't need 
# to import any math package.

def square_numbers_exclude(n):
    L = []
    numbers = int(n**0.5)
    for n in range(1, n+1):
        for i in range(1, numbers + 1):
            if i ** 2 == n:
                break
        else:
            L.append(n)
    return L

print(square_numbers_exclude(100))


# def sqrt_res(n):
#     d = {}
#     res = []
#     for num in range(1, int(n**0.5) + 1):
#         d[num**2] = num
#     for i in range(1, n+1):
#         if i not in d:
#             res.append(i)
#     return res

# print(sqrt_res(100))



# Write down your code to fill the [loop] and [condition]. Please don't change any other part of the code.

# Write a function to take arbitrary number (>0) of positive integers,
# and return the maximum value. You can assume the arguments are always valid.


