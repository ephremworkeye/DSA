# find the longest substring with out repeated characters
# question
    # is contigious or subsequence 
        # contigious
    # is case sensitive
        # no
# test cases
    # "abcdcde" 4
    # "bbbbbb" 1
    # "" 0
# brute force solution
# longest_substring = 0
# current_longest = 0
# seen = {
#    a: 0
#    b: 1
#    c: 2 
# }

# time complexity O(N^2)
# space complexity O(N)
# def longest_substring(s):
#     longest = 0
#     for left in range(len(s)):
#         current_longest = 0
#         seen = {}
#         if len(s) - left < longest:
#             break
#         for right in range(left, len(s)):
#             if s[right] not in seen:
#                 seen[s[right]] = right
#                 current_longest += 1
#                 longest = max(current_longest, longest)
#             else:
#                 break
#     return longest

# print(longest_substring('abccdefa'))
# print(longest_substring('ccccc'))
# print(longest_substring(''))
        

# optimal solution for this one is using window sliding technique
# # Form a window over some portion of sequential data, then move that window throught the data to capture different parts of it

# time complexity O(N)
# space complexity O(N)

# def longest_substring(s):
#     # we need left pointer to keep the left boundaries
#     # we need hashmap to track elements
#     # we need to accumalate longest substring so far
#     longest, left, seen = 0, 0, {}
#     for right in range(len(s)):
#         # initializing the current character based on the right index
#         current_char = s[right]
#         # checking wheather the current character in dictionary
#         if current_char not in seen:
#             # storing the current characters with its index
#             seen[current_char] = right
#             # updating the longest substring so far 
#             longest = max(longest, right - left + 1)
#         # if current character exists 
#         else:
#             # but the current character index is outside the current portion of stiring
#             # update the current characters with its current character index
#             if seen[current_char] <= left:
#                 seen[current_char] = right
#             # update the left boundaries of characters seen index + 1
#             else:
#                 left = seen[current_char] + 1
#     return longest

# acbcdefa
# def longest_substring(s):
#     longest = 0
#     for left in range(len(s)):
#         seen = {}
#         current = 0
#         if longest > len(s)-left:
#             break
#         for right in range(left, len(s)):
#             current_charcter = s[right]
#             if current_charcter not in seen:
#                 seen[current_charcter]= right
#                 current += 1
#                 longest = max(current, longest)
#             else:
#                 break
#     return longest



# print(longest_substring('abccdefa'))
# print(longest_substring('ccccc'))
# print(longest_substring(''))


# s = ''
#      l  
# s = 'abacadef'
#        r      
# s = 'a'
# seen = {a:3, b:1, c:3, d:5, d:6, e:7, f:8}
# longest = max(longest, r-l + 1) = 5




def longest_substring(s):
    if len(s) <= 1:
        return len(s)
    longest, left = 0, 0
    seen = {}
    for right in range(len(s)):
        current_char = s[right]
        if current_char not in seen:
            seen[current_char] = right
            longest = max(longest, (right -left) +1)
        else:
            # we need two condition here
            # if we haven't seen char in seen but checking the character in current left and right boundaries
            if seen[current_char] <= left:
                seen[current_char] = right
            else:
                # reset the left boundaries for new longest substring
                left = seen[current_char] + 1
    return longest

print(longest_substring('abccdefa'))
print(longest_substring('ccccc'))
print(longest_substring(''))