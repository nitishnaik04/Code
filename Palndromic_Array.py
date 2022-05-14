arr = [1,1,1,1]
rev = []
for i in range(len(arr)):
    rev = arr[::-1]

if arr == rev:
    print('Palindrom')
else:
    print('not a palindrome')