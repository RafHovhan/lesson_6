a1 = int(input())
d = int(input())
n = int(input())

prog = list(map(lambda i: a1 + (i * d), range(n)))

for num in prog:
    print(num)