s=input()
l=len(s)

q=0
res=0

total_q=0
for i in s:
    if i=='Q':
        total_q+=1
    
for i in s:
    if i=='Q':
        q+=1
    elif i=='A':
        res+=q*(total_q-q)

print(res)