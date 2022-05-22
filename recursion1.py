def reducer(s):
    if len(s) == 1:
        return int(s)
    else:
        return reducer(str(sum(map(int, s))))


s = '123456'
print(reducer(s))
