# n - even
n = int(input())

list = []

i = 0

while n-i:
    a = []
    for j in range(n):
        
        a.append(n - i)

    for j in range(i):
        a[j] += i-j
        a[n-j-1] += i-j


    list.append(a)
    i += 1


for i in list:
    print(*i)
