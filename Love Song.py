n,q = map(int,input().split())
s=input()
for i in range(q):
    l,r=map(int,input().split())
    z=""
    res=0
    for j in range(l-1,r):
        res+=(ord(s[j])-96)

    print(res)

# Time Limit Exceeded