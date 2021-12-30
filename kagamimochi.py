N = int(input())
list_a = []
for i in range(N):
    x = int(input())
    list_a.append(x)
list_b = list(set(list_a))
list_b.sort(reverse=True)
print(len(list_b))
