def find_1(lst, minimum, maximum):
    ind = []
    for index, val in enumerate(lst):
        if minimum <= val <= maximum:
            ind.append(index)
    return ind

list1 = [5, 10, 15, 20, 25, 30, 35]
minva = 10
maxva = 25
res = find_1(list1, minva, maxva)
print(res) 