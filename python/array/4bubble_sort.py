def bubble_sort(A):
    for i in range(len(A), 0, -1):
        for j in range(1, i):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]

    return A

print(bubble_sort([5, 2, 3, 1, 9, 0, 2]))


