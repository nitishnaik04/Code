n = list(input())
sum, mul = 0, 1
for i in n:
    i = int(i)
    for _ in range(len(n)):
        mul *= i
    sum += mul
    mul = 1
print("Yes" if sum == int(''.join(n)) else "No")
