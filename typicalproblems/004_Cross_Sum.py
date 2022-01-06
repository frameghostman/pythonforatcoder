H, W = (int(x) for x in input().split())
A = []

for i in range(H):
    array = (int(x) for x in input().split())
    array = list(array)
    A.append(array)

yoko = []
for i in range(H):
    tmp = 0
    for j in range(W):
        tmp += A[i][j]
    yoko.append(tmp)

tate = []
for i in range(W):
    tmp = 0
    for j in range(H):
        tmp += A[j][i]
    tate.append(tmp)

ANS = []
for i in range(H):
    tmp_list = []
    for j in range(W):
        tmp_list.append(yoko[i] + tate[j] - A[i][j])
    ANS.append(tmp_list)

for i in range(H):
    print(*ANS[i])
