N = int(input())
input_list_final = []

for x in range(N):
    input_list_temp = []
    for y in input().split():
        y = int(y)
        input_list_temp.append(y)
    input_list_final.append(input_list_temp) 

#print(N)
#print(input_list_final)

for i in range(N):
    flag = False
    t_i = input_list_final[i][0]
    x_i = input_list_final[i][1]
    y_i = input_list_final[i][2]
    if(i == 0):
        flag_temp = False
        move_x = x_i
        move_y = y_i
        move_total = move_x + move_y
        for j in range(t_i // 2 + 1):
            if(move_total == t_i - (2 * j)):
                flag_temp = True
                #print("OK")
                break
        if(flag_temp == False):
            break
            
    else:
        flag_temp = False
        t_diff = t_i - input_list_final[i-1][0]
        move_x = abs(x_i - input_list_final[i-1][1])
        move_y = abs(y_i - input_list_final[i-1][2])
        move_total = move_x + move_y
        for j in range(t_diff // 2 + 1):
            if(move_total == t_diff - (2 * j)):
                flag_temp = True
                #print("OK")
                break
        if(flag_temp == False):
            break
    flag = True

if flag:
    print("Yes")
else:
    print("No")
