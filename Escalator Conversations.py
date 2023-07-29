t=int(input())
for i in range(t):
    n,m,k,H = map(int,input().split())
    arr = list(map(int,input().split()))

    l=len(arr)
    x=0
    c=0
    for i in range(l):
        if H>arr[i]:
            diff = (H-arr[i])
            x = diff/k

            if x.is_integer()==True and diff<=(k*(m-1)) and x>0:
                c+=1
            else:
                pass

        else:
            diff = (arr[i]-H)
            x = diff/k
            if x.is_integer()==True and diff<=(k*(m-1)) and x>0:
                c+=1
            else:
                pass
            

    print(c)
