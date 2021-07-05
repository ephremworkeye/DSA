'''
    input: [5, 2, 9, 1, 4]
    output:[1, 2, 4, 5, 9]
    solve the problem using insertion sort

    asume first position is sorted and start from the position 1
    take out current value and compare with the previous element until pos > 0 while decrementing pos
    if previous of current pos > current value shift element to the right 
    
'''


def insertion_sort(A):
    for pass_num in range(1, len(A)):
       
        current_value = A[pass_num]
        position = pass_num
        while position > 0 and A[position-1] > current_value:
            A[position] = A[position-1]
            position -= 1
        A[position] = current_value

    return A

print(insertion_sort([5, 2, 9, 1, 4]))
