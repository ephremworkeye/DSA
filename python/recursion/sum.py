def sum(A, end):
    if len(A) == 1:
        return A[0]
    else:
        return A[0] + sum(A[1:], end)

A = [2, 3, 4, 5, 6]
end = len(A)
print(sum(A, end))

