t=int(input())
for i in range(t):
    n=int(input())
    arr = list(map(int,input().split()))

    one=0
    two=0
    for i in arr:
        if i==2:
            two+=1
        else:
            one+=1
    if (two%2==0 and one%2==0) or (two%2==1 and one%2==0 and one>0):
        print("YES")
    else:
        print("NO")