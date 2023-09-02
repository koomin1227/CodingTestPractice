string = input()
tot = 0
i = 0
string_len = len(string) - 1
while i < len(string):
    if string_len - i >= 1:
        alp2 = string[i:i+2]
    else:
        alp2 = string[i]
    if string_len - i >= 2:
        alp3 = string[i:i+3]
    else:
        alp3 = string[i]
    if alp2 == 'c=':
        tot+=1
        i += 2
    elif alp2 == 'c-':
        tot+=1
        i += 2
    elif alp2 == 'd-':
        tot+=1
        i += 2
    elif alp2 == 'lj':
        tot+=1
        i += 2
    elif alp2 == 'nj':
        tot+=1
        i += 2
    elif alp2 == 's=':
        tot+=1
        i += 2
    elif alp2 == 'z=':
        tot+=1
        i += 2
    elif alp3 == 'dz=':
        tot+=1
        i += 3
    else:
        i+=1
        tot+=1
print(tot)
