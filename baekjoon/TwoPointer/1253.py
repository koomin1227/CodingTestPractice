n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
num_dic = dict()

for number in numbers:
    if number in num_dic:
        num_dic[number] += 1
    else:
        num_dic[number] = 0

answer = 0
for i in range(0, len(numbers)):
    number = numbers[i]
    for j in range(0, len(numbers)):
        if i != j:
            a = numbers[j]
            b = number - a
            if b in num_dic:
                if a == b and num_dic[b] < 2:
                    c= 1
                elif b == number and num_dic[b] < 2:
                    c = 1
                else:
                    answer += 1
                    break
print(answer)
    