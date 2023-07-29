t=int(input())
for i in range(t):
    n=int(input())
    arr = list(map(int,input().split()))
    l=len(arr)
    x=1

    mini = min(arr)
    maxi = max(arr)

    while(l>1):
        imin,imax=0,0
        for i in range(l):
            if arr[i]==min(arr):
                imin=i
                break
        i=0
        for i in range(l):
            if arr[i]==max(arr):
                imax=i
                break

        if (min(arr)%2==1 and arr[0]%2==1) and ((max(arr)%2==1 and arr[l-1]%2==1) or (max(arr)%2==0 and arr[l-1]%2==0)):
            arr[imin],arr[0]   = arr[0],  arr[imin]
            arr[imax],arr[l-1] = arr[l-1],arr[imax]
            arr.remove(arr[l-1])
            arr.remove(arr[0])

        elif (min(arr)%2==0 and arr[0]%2==0) and ((max(arr)%2==1 and arr[l-1]%2==1) or (max(arr)%2==0 and arr[l-1]%2==0)):
            arr[imin],arr[0]   = arr[0],  arr[imin]
            arr[imax],arr[l-1] = arr[l-1],arr[imax]
            arr.remove(arr[l-1])
            arr.remove(arr[0])

        else:
            x=-1
            print("NO")
            break

        l=len(arr)

    if x==1:
        print("YES")

# Dont know where it went wrong
