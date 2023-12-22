n = int(input())

max_location = 0
lst = [0] * 101
for _ in range(n):
    location, alphabet = input().split()
    location = int(location)
    lst[location] = alphabet
    max_location = max(max_location, location)

max_value = 0 
for i in range(max_location + 1):
    for j in range(i, max_location + 1):
        # 양끝점이 0이면 안됨
        if lst[i] !=0 and lst[j] !=0:

            tmp = lst[i:j+1]   
            
            g_cnt = tmp.count('G')
            h_cnt = tmp.count('H')
            
            if g_cnt != 0 and g_cnt == h_cnt:
                max_value = max(max_value, j-i)

print(max_value)