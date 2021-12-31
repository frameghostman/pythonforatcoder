N = int(input())
mochi = []
for i in range(N):
    x = int(input())
    mochi.append(x)
mochi_count = list(set(mochi))
mochi_count.sort(reverse=True)
print(len(mochi_count))
