input_string = list(input())


answer = 0
for i in range(len(input_string)):
    if input_string[i] == '(':

        for j in range(i + 1, len(input_string)):
            if input_string[j] == ')':
                answer += 1

print(answer)