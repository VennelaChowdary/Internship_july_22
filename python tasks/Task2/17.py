k = int(input())
arr = list(map(int, input().split()))
myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))