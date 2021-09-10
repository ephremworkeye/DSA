def shortest_substring(s, arr):
    shortest = []
    for left in range(len(s)):
        current = []
        if s[left] in arr:
            current.append(s[left])
            if len(current) > len(arr):
                if len(shortest) < len(current):
                    shortest = current
        break
    return shortest

# shortest []   current = [x,] => should be greater than or equal to len(arr)
#      l
# s = 'xyzazxyc' arr = ['x', 'y', 'z'] 
#      r
#         l
# s = 'xyazxyc' arr = ['x', 'y', 'z'] 
#            r
# shortest_count = 0
# current_count = 3
# shortest = s[l:r]

