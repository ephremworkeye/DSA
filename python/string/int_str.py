# num = 123 => '123'
# we can't use str conversion
# 123 % 10 = 3
# 123 // 10 = 12 we need integer value
# 12 % 10 = 2
# 12 // 10 = 1
# 1 % 10 = 1
# 1 // 10 = 0
# then break




def int_to_str(num):
    is_negative = False
    if num < 0:
        num, is_negative = -num,  True

    s = []
    while True:
        s.append(chr(ord('0') + num % 10)) # find remainder and add to zero
        num = num // 10
        if num == 0:
            break
    return ('-' if is_negative else '') + ''.join(reversed(s))

print(int_to_str(123))
print(int_to_str(0))
print(int_to_str(-123))
