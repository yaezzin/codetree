def decimal(lst):
    s = 0
    for i in range(len(lst)):
        s = (s * 2 + int(lst[i]))
   
    return s

# main

s = list(map(int, list(input())))

answer = 0
for i in range(len(s)):
    s[i] = 1 - s[i] # 1이면 0이 되고, 0이면 1이 됨
    
    tmp = decimal(s)

    answer = max(tmp, answer)

    s[i] = 1 - s[i]
    
print(answer)