def simple_bubble_sort(list):
    razk = len(list)
    for i in range(razk):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


list_1 = [2, 18 , 8, 5, 3, 14, 4, 6, 15, 7, 17, 1, 19, 10, 9, 16, 5, 11, 13, 8, 20]
simple_bubble_sort(list_1)
print(f'Sorted list: {list_1}')


def binary_search(list, value):
    n = len(list)
    result_ok = False
    first = 0
    last = n - 1
    while True:
        if first <= last and not result_ok:
            middle = (first + last) // 2
            if value == list[middle]:
                first = middle
                last = first
                result_ok = True
                pos = middle
            elif value > list[middle]:
                first = middle + 1
            else:
                last = middle - 1
        else:
            if result_ok == True:
                print(f'Item {value} found\nElement index: {pos}')
                break
            else:
                print(f'Item {value} not found')
                break


list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30]
print(f'-Search list:\n{list_2}')
value = int(input('Enter search list: '))
binary_search(list_2, value)
