t = int(input())
for i in range(t):
    arr = list(map(int,input().split()))

    if arr[0]+arr[1]>=10 or arr[0]+arr[2]>=10 or arr[2]+arr[1]>=10:
        print('YES')
    else:
        print("NO")

              

