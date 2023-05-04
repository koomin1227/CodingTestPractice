def solution(words, queries):
    answer = []
    words.sort()
    words.sort(key=lambda x:len(x))
    r_words=[]
    for i in words:
        r_words.append(i[::-1])
    r_words.sort()
    r_words.sort(key=lambda x:len(x))
    for i in queries:
        if i[0]=='?' and i[-1]=='?':
            l=llen_binary(words,0,len(words)-1,len(i))
            if l==None:
                answer.append(search(r_words,i))
            else:
                r=rlen_binary(words,0,len(words)-1,len(i))
                answer.append(r-l+1)
        elif i[0]=='?':
            answer.append(search(r_words,i))
        elif i[-1]=='?':
            answer.append(search(words,i))
    return answer
def llen_binary(words,start,end,target):
    if start>end:
        return None
    mid=(start+end)//2
    if len(words[mid])==target:
        if mid==0 or len(words[mid-1])<target:
            return mid
        else:
            return llen_binary(words,start,mid-1,target)
    elif len(words[mid])<target:
        return llen_binary(words,mid+1,end,target)
    elif len(words[mid])>target:
        return llen_binary(words,start,mid-1,target)
def rlen_binary(words,start,end,target):
    if start>end:
        return None
    mid=(start+end)//2
    if len(words[mid])==target:
        if mid==len(words)-1 or len(words[mid+1])>target:
            return mid
        else:
            return rlen_binary(words,mid+1,end,target)
    elif len(words[mid])<target:
        return rlen_binary(words,mid+1,end,target)
    elif len(words[mid])>target:
        return rlen_binary(words,start,mid-1,target)
def lbinary(words,start,end,target,le,st):
    if start>end:
        return None
    mid=(start+end)//2
    if words[mid].startswith(target):
        if mid==st or words[mid-1][:le]<target:
            return mid
        else:
            return lbinary(words,start,mid-1,target,le,st) 
    elif words[mid][:le]<target:
        return lbinary(words,mid+1,end,target,le,st)
    elif words[mid][:le]>target:
        return lbinary(words,start,mid-1,target,le,st) 
def rbinary(words,start,end,target,le,en):
    if start>end:
        return None
    mid=(start+end)//2
    if words[mid].startswith(target):
        if mid==en or words[mid+1][:le]>target:
            return mid
        else:
            return rbinary(words,mid+1,end,target,le,en)
    elif words[mid][:le]<target:
        return rbinary(words,mid+1,end,target,le,en)
    elif words[mid][:le]>target:
        return rbinary(words,start,mid-1,target,le,en) 
def del_que(a):
    ans=''
    if a[0]=='?':
        for i in range(0,len(a)):
            if a[i]!='?':
                ans=a[i:]
                break
    else:
        for i in range(0,len(a)):
            if a[i]=='?':
                ans=a[:i]
                break
    return ans
def search(words,que):
    llen=llen_binary(words,0,len(words)-1,len(que))
    if llen==None:
        return 0
    rlen=rlen_binary(words,0,len(words)-1,len(que))
    r_que=del_que(que)
    l=lbinary(words,llen,rlen,r_que,len(r_que),llen)
    if l==None:
        return 0
    r=rbinary(words,llen,rlen,r_que,len(r_que),rlen)
    return r-l+1
words=["frodo", "front", "frost", "frozen", "frame", "kakao",'a']
queries=['?',"fro??", "????o", "fr???", "fro???", "pro?"]
#words= ["banana", "apple", "melon","melen"]
#queries=["mel??","ap??","ap???"]
print(solution(words,queries))
#qw