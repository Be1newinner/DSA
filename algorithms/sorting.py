def bubble_sort(ls: list[int]):
    for _i in range(len(ls) - 1):
        for j in range(len(ls) - 1):
            if ls[j] > ls[j + 1]:
                (ls[j], ls[j + 1]) = (ls[j + 1], ls[j])
    return ls


# ls = [10, 2, 5, 99, 14, 154, 22, 1, 5, 3, 9, 14]
ls = [99,98,97,96,95,94,93,92,91,90]

print(bubble_sort(ls))