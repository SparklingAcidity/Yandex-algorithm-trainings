set1 = set(list(map(int, input().split())))
set2 = set(list(map(int, input().split())))
lst = list(set1 & set2)
lst.sort()
print(*lst)
