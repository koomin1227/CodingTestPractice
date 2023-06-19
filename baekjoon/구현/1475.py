n = input()
num = []
for i in range(len(n)):
    num.append(int(n[i]))
number = [0]*10
for i in num:
    if i == 6:
        number[9] +=1   
    else:
        number[i] +=1
number[9] = number[9]//2 + number[9]%2
answer = max(number)
print(answer)