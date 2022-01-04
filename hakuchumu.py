import re

S = input()
T = S
match_lines = ["dream", "dreamer", "erase", "eraser"]
flag = True

while(flag):
    flag = False
    for i in range(4):
        if(T.endswith(match_lines[i])):
            slice_number = -1 * len(match_lines[i])
            T = T[:slice_number]
            flag = True
            break

if(T == ""):
    print("YES")
else:
    print("NO")
