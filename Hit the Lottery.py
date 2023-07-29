n=int(input())
arr = [100,20,10,5,1]
l = len(arr)
c,r,i=0,0,0

if n>=100:
    r=int(n//100)
    n=int(n%100)

while(n>0):
    if n>=arr[i]:
        while(n>=arr[i]):
            n=n-arr[i]
            c+=1
    else:
        i+=1

print(r+c)