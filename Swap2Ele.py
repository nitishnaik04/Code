List = [1, 2, 3, 4, 5]
pos1 = 2
pos2 = 5
List[pos1-1], List[pos2-1] = List[pos2-1], List[pos1-1]
print(List)