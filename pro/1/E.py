n = int(input())
a = list(map(int, input().split()))

summ = a[0]
start = 0
best_sum = a[0]
best_start = 0
best_end = 0

for i in range(1, n):
    c = summ + a[i]
    if c < a[i]:
        summ = a[i]
        start = i
    elif c == a[i]:
        summ = a[i]
        start = i
    else:
        summ = c
    if summ > best_sum:
        best_sum = summ
        best_start = start
        best_end = i

print(best_start, best_end)
