"Задача №3"

# Исходный массив из 10 элементов
list = [64, 34, 25, 12, 22, 11, 90, 87, 76, 53]


def bubble_sort(list):
    n = len(list)
    comparisons = 0

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            comparisons += 1
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True

        if not swapped:
            break

    return comparisons


print("Исходный массив:", list)
comparisons = bubble_sort(list)

print("Отсортированный массив:", list)
print("Количество сравнений:", comparisons)
