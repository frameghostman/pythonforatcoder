N, Y = (int(x) for x in input().split())
ansX, ansY, ansZ = -1, -1, -1
for x in range(N + 1):
    money_sum1 = 0
    money_sum1 = 10000 * x
    for y in range(N + 1 - x):
        money_sum2 = money_sum1
        money_sum2 = money_sum2 + 5000 * y + 1000 * (N - x - y)

        if(money_sum2 == Y):
            ansX, ansY, ansZ = x, y, N - x - y
            break
    else:
        continue
    break

print(ansX, ansY, ansZ)