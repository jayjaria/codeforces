t=int(input())
for i in range(t):
    a,b  = map(int,input().split())

    if a>1:
        print(a-1)
    elif a==1 and b==2:
        print(3)
    elif a==1 and b%2==0:
        print(2)
    elif a==1 and b%2!=0:
        print(b+1)
    else:
        pass
