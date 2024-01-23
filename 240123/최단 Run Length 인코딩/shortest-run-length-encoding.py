import sys

def move_right(s):
    tmp = s[-1]

    for i in range(len(s) - 1, 0, -1):
        s[i] = s[i-1]

    s[0] = tmp
    return s
    
def encoding(s):
    seq = 1
    tmp_str = ""
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            seq += 1
        
        else:
            tmp_str += s[i]
            tmp_str += str(seq)
            seq = 1
    
    tmp_str += s[-1]
    tmp_str += str(seq)
    
    #print(tmp_str)
    return len(tmp_str)
            
s = list(input())
min_length = sys.maxsize
for i in range(len(s)):
    result = move_right(s)
    min_length = min(min_length, encoding(result))

print(min_length)