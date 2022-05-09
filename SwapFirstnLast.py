lis = [1,2,3,4,5,6]
# temp = lis[0]
# lis[0] = lis[-1]
# lis[-1] = temp
lis[0], lis[-1] = lis[-1], lis[0]
print(lis)