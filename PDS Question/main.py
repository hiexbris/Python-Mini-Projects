numbers = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]


answer = []
i = 0
sum_1 = 0
sum_2 = 0

while i < 10:
    sum_2 = sum_1 + numbers[i]
    if sum_2 < sum_1:
        answer.append(sum_1)

    if sum_2 < 0:
        i = i+1
        sum_1 = 0
        sum_2 = 0
    else:
        sum_1 = sum_2
        sum_2 = 0
        i = i+1

answer.sort()
print(answer[-1])