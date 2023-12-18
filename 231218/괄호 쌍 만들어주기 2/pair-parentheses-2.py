lst = list(input())

cnt = 0
for i in range(len(lst) - 1):
    if lst[i] == '(' and lst[i+1] == '(':

        for j in range(i+2, len(lst) - 1):
            if lst[j] == ')' and lst[j+1] == ')':
                cnt += 1

print(cnt)