lis=[1,2,3,4,5,6,7,8]
k = 3
lis[k-1],lis[-k] = lis[-k], lis[k-1]
print(lis)