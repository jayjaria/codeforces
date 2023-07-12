t=int(input())
for i in range(t):
    n=int(input())
    arr = list(map(int,input().split()))

    l=len(arr)
    if l==1 or l==2:
        print(max(arr))
        break
    #remove negative numbers from both ends of the array
    while(arr[0]<0):
        if len(arr)==1:
            break
        arr.pop(0)

    while(arr[-1]<0):
        if len(arr)==1:
            break
        arr.pop(-1)

    if len(arr)==1:
        print(arr[0])
        break

    r=min(arr)
    while(r<0):

        ind=0
        while(arr[ind]!=r):
            ind+=1
        arr[ind-1]+=arr[ind+1]
        arr.pop(ind)
        arr.pop(ind)

        r = min(arr)
    
    s1,s2,j=0,0,0
    l=len(arr)
    for j in range(l):
        if j%2==0:
            s1+=arr[j]
        else:
            s2+=arr[j]
        j+=1

    if s1>s2:
        print(s1)
    else:
        print(s2)
