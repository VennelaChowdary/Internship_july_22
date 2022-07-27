lst=[]
n = int(input())

for i in range(0, n):
    Y = [input(),float(input())]
    lst.append(Y)
lst = sorted(lst, key=lambda x: x[1]);
for x in range(1, n):
    if(lst[x][1] != lst[x-1][1]):
        score = lst[x][1]
        break
lst = sorted(lst);
for x in range(n):
    if(lst[x][1] == score):
        print(lst[x][0])