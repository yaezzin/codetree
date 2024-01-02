import sys

n = int(input())
lst = list(input())

answer = 0
for i in range(len(lst)):
    for j in range(i+1, len(lst)):    
        if lst[i] == '0' and lst[j] == '0':
            lst[i] = '1'
            lst[j] = '1'

            length = []
            for k in range(len(lst)):
                for l in range(k+1, len(lst)):
                    if lst[k] == '1' and lst[l] == '1':
                        length.append(l-k)
        
            min_length = min(length)
            lst[i] = '0'
            lst[j] = '0'
        
            answer = max(answer, min_length)

        

print(answer)