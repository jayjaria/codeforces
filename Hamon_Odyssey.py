t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    l = len(arr)
    c = 0
    j=0
    r=1
    for i in range(0,l-1):
        r = r &(arr[i]+arr[i+1])
        if arr[i]==0:
            c+=1
            if i<l-1:
                i+=1
            else:
                break
        elif r==0:
            c+=1
            i+=1
            if i<l-1:   
                r=arr[i]
            else:
                break
        
        else:
            i+=1
    print(c)