# def add_binary(a, b):
#     result = ''
#     i, j , carry = len(a)-1, len(b)-1, 0
#     while i >= 0 or j >= 0:
#         sum = carry
#         if i >= 0:
#             sum += ord(a[i]) - ord('0')
#         if j >= 0:
#             sum += ord(b[j]) - ord('0')
#         i, j = i-1, j-1
#         carry = 1 if sum > 1 else 0
#         result += str(sum%2)
#     if carry != 0:
#         result ++ str(carry)
#     return result[::-1]

def f():
    x = 100
    print(x)

x+=1
f()


