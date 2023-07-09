t = int(input())
for i in range(t):
    n,d,h = map(int, input().split())
    arr = list(map(int, input().split()))

    area = 0
    if len(arr)==1:
        area+=(1/2)*(d)*(h)
    else:
        j=0
        for j in range(len(arr)-1):
            diff = arr[j+1]-arr[j]
            x = (d*diff)/(2*h)

            if diff < h:
                area+=(d-x)*diff

            else:
                area+=(1/2)*(d)*(h)
            i+=1
        area+=(1/2)*(d)*(h)

    print(area)

    