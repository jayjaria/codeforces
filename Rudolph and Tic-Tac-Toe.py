t = int(input())
for i in range(t):
    arr=[]
    for j in range(3):
        p = input()
        arr.append(p)

    if (arr[0][0]=='X' and arr[1][0]=='X' and arr[2][0]=='X') or (arr[0][1]=='X' and arr[1][1]=='X' and arr[2][1]=='X') or (arr[0][2]=='X' and arr[1][2]=='X' and arr[2][2]=='X') or (arr[0][0]=='X' and arr[0][1]=='X' and arr[0][2]=='X') or (arr[1][0]=='X' and arr[1][1]=='X' and arr[1][2]=='X') or (arr[2][0]=='X' and arr[2][1]=='X' and arr[2][2]=='X') or (arr[0][0]=='X' and arr[1][1]=='X' and arr[2][2]=='X') or (arr[2][0]=='X' and arr[1][1]=='X' and arr[0][2]=='X'):
        print('X')
    elif (arr[0][0]=='O' and arr[1][0]=='O' and arr[2][0]=='O') or (arr[0][1]=='O' and arr[1][1]=='O' and arr[2][1]=='O') or (arr[0][2]=='O' and arr[1][2]=='O' and arr[2][2]=='O') or (arr[0][0]=='O' and arr[0][1]=='O' and arr[0][2]=='O') or (arr[1][0]=='O' and arr[1][1]=='O' and arr[1][2]=='O') or (arr[2][0]=='O' and arr[2][1]=='O' and arr[2][2]=='O') or (arr[0][0]=='O' and arr[1][1]=='O' and arr[2][2]=='O') or (arr[2][0]=='O' and arr[1][1]=='O' and arr[0][2]=='O'):
        print('O')
    elif (arr[0][0]=='+' and arr[1][0]=='+' and arr[2][0]=='+') or (arr[0][1]=='+' and arr[1][1]=='+' and arr[2][1]=='+') or (arr[0][2]=='+' and arr[1][2]=='+' and arr[2][2]=='+') or (arr[0][0]=='+' and arr[0][1]=='+' and arr[0][2]=='+') or (arr[1][0]=='+' and arr[1][1]=='+' and arr[1][2]=='+') or (arr[2][0]=='+' and arr[2][1]=='+' and arr[2][2]=='+') or (arr[0][0]=='+' and arr[1][1]=='+' and arr[2][2]=='+') or (arr[2][0]=='+' and arr[1][1]=='+' and arr[0][2]=='+'):
        print('+')
    else:
        print('DRAW')
    