n=int(input())
m=n
cnt=0
while True:
    a=m//10
    b=m%10
    c=(a+b)%10
    m=(b*10)+c
    cnt+=1
    if n==m:
        break
print(cnt)
    
    
