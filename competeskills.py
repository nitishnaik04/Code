A = [4, 2, 7]
B = [2, 6, 3]
a1, b1 = 0, 0
for i in range(len(A)):
    if A[i]>B[i]:
        a1 = a1+1
    elif A[i]<B[i]:
        b1 = b1+1
    else:
        break
print(a1, b1)