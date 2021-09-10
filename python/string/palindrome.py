# testing a palidrome
    # constraint
        # is case sensitive
        # is space matters
        # case for empty string
        # does the string have alphanumeric


# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     left, right = 0, len(s) - 1
#     s = s.lower()
#     while left < right:
#         # if spaces
#         if s[left] == ' ':
#             left += 1
#         elif s[right] == ' ':
#             right -= 1
        
#         # if other than alpha
#         if not s[left].isalnum():
#             left += 1
#         elif not s[left].isalnum():
#             right -= 1

#         elif s[left] != s[right]:
#             return False
#         else:
#             left += 1
#             right -=1
#     return True
# if __name__ == '__main__':
#     print(is_palindrome('aabbaa')) # even string
#     print(is_palindrome('aabaa')) # odd string
#     print(is_palindrome('A abaa'))
#     print(is_palindrome('a'))
#     print(is_palindrome(''))
#     print(is_palindrome('abc'))

# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     s = s.lower()
#     left, right = 0, len(s) - 1
#     while left < right:
#         if not s[left].isalpha():
#             left += 1
#         elif not s[right].isalpha():
#             right -= 1
#         elif s[right] != s[left]:
#             return False
#         else:
#             left += 1
#             right -= 1
#     return True

# if __name__ == '__main__':
#     print(is_palindrome('aabbaa')) # even string
#     print(is_palindrome('aabaa')) # odd string
#     print(is_palindrome('A abaa'))
#     print(is_palindrome('a'))
#     print(is_palindrome(''))
#     print(is_palindrome('abc'))


# testing an almost palidrome
    # constraint
        # is case sensitive
        # is space matters
        # case for empty string
        # does the string have alphanumeric
        # do we consider a palindrome as almost palindrome
    # test case 
        # "raceacar": True
        # "abccdba" : True
        # "abcdefdba": False
        # "", "a", "ab" all True
# def almost_palindrome(s):
#     if len(s) <= 2:
#         return True
#     s = s.lower()
#     left, right, counter = 0, len(s)-1, 0
#     while left < right:
#         if s[left] != s[right]:
#             if s[left + 1] == s[right]:
#                 left += 1
#                 counter += 1
#                 if counter > 1:
#                     return False
#             elif s[left] == s[right - 1]:
#                 right -= 1
#                 counter += 1
#                 if counter > 1:
#                     return False
#         else:
#             left += 1
#             right -= 1
#     return True

# if __name__ == '__main__':
#     print(almost_palindrome('raceacar'))
#     print(almost_palindrome('abccdba'))
#     print(almost_palindrome('abcdefdba'))
#     print(almost_palindrome(''))
#     print(almost_palindrome('a'))
#     print(almost_palindrome('ab'))


