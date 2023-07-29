t=int(input())
for i in range(t):
    n=int(input())
    arr = list(map(int,input().split()))

    mini=min(arr)
    maxi=max(arr)

    l=len(arr)
    imax,imin=0,0
    for i in range(len(arr)):
        if arr[i]==maxi:
            imax = i
        elif arr[i]==mini:
            imin = i
        else:
            pass

    if imax<l//2 and imin<l//2:
        print(max(imax,imin)+1)
    elif imax>=l//2 and imin>=l//2:
        print(l-min(imin,imax))
    else:
        r=min(max(imax,imin),max(l-imax,l-imin))
        print(min(r+1,min(imax,imin)+1 + (l-max(imin,imax))))

# Not Correct