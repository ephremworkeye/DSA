# import time, sys
# indent = 0
# indent_increasing = True

# try:
#     while True:
#         print(' '* indent, end='')
#         print('*********')
#         time.sleep(0.1)
#         if indent_increasing:
#             indent += 1
#             if indent == 20:
#                 indent_increasing = False
#         else:
#             indent -= 1
#             if indent == 0:
#                 indent_increasing = True
# except KeyboardInterrupt:
#     sys.exit()


def zigzag(s, rows):
    output  = [''] * rows 
    increasing = True
    row = 0
    for char in s:
        output[row] += char
        if increasing:
            row += 1
            if row == rows - 1:
                increasing = False
        else:
            row -= 1
            if row == 0:
                increasing = True
    return ''.join(output)

print(zigzag('YELLOWPINK', 4)) # "YPEWILONLK"

        
