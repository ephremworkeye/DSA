def del_dup(alist):
    right = 1
    for left in range(alist):
        if alist[right] != alist[right-1]:
            alist[left] = alist[right]
            right += 1


    return right

print(del_dup([2, 5, 5, 5, 8, 8, 10]))