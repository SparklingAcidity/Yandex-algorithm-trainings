buttons = set(map(int, input().split()))
n = int(input())
num = set(int(a) for a in str(n))
dif = num.difference(buttons)
print(len(dif))