l,t = map(int,input().split())
n=int(input())
v = list(map(int,input().split()))

c=0

if n==2:
    x=(2*l*v[0])/(v[0]+v[len(v)-1])
    s=x/v[0]
    c+=t//s


else:
    for i in range(len(v)-1):
        x=(2*l*v[i])/(v[i]+v[i+1])
        s=x/v[i]
        c+=t//s

    x=(2*l*v[0])/(v[0]+v[len(v)-1])
    s=x/v[0]
    c+=t//s


print(c)
