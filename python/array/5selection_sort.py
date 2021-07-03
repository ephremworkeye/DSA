# input =  [5, 2, 6, 9, 1]
# output =  [1, 2, 5, 6, 9]

def selection_sort(A):
    # set the number of passes
    for passNum in range(len(A)-1, 0, -1):
        # select the max position for the first time
        max_num_pos = 0
        for current in range(1, passNum+1):
            # if current value which starts from the pos 1 is greater than max_num_pos
            if A[current] > A[max_num_pos]:
                # update the max_num_pos
                max_num_pos = current
        # swap the the last element and the updated max_num_pos
        A[passNum], A[max_num_pos] = A[max_num_pos], A[passNum]
    return A

print(selection_sort([5, 2, 6, 9, 1]))