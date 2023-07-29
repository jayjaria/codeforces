n=int(input())
arr = list(map(int,input().split()))

c=1
res=[]
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        c+=1
    else:
        res.append(c)
        c=1

res.append(c)
print(max(res))
        