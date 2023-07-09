t = int(input())
for i in range(t):
    n = int(input())
    c=0
    for j in range(n):
        a,b = map(int, input().split())
        if b<a:
            c+=1
        else:
            pass
    print(c)

