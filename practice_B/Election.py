N = int(input())
input_list = []
vote_number_list = []
i = 0
j = 0
ans_number = 0

for x in range(N):
    input_list.append(input())
unique_list = set(input_list)
unique_list = list(unique_list)

for x in unique_list:
    vote_number_list.append(0)

for x in unique_list:
    for y in input_list:
        if(x == y):
            vote_number_list[i] += 1
    i += 1

max_vote_number_list = max(vote_number_list)
for x in vote_number_list:
    if(x == max_vote_number_list):
        ans_number = j
    j += 1

print(unique_list[ans_number])
