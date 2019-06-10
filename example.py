def create():
    result = []
    row1 = list(range(1, 11))
    row2 = list(range(11, 21))
    row3 = list(range(21, 31))
    row4 = list(range(31, 41))
    row5 = list(range(41, 51))
    result.append(row1)
    result.append(row2)
    result.append(row3)
    result.append(row4)
    result.append(row5)
    return result


def trans(a):
    return tuple(zip(*a[::-1]))


matrix = create()
print(matrix)
b = trans(matrix)
print(b)

"""for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])"""

for j1 in range(len(matrix[0])):
    for i1 in range(len(matrix)):
        print(matrix[i1][j1])


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


nums = [4, 5, 6, 7, 8, 9, 0]
print(nums)
shift(nums, 1)
print(nums)

shift(nums, -2)
print(nums)

shift(nums, 3)
print(nums)
