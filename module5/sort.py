data = [6, 3, 2, 5, 1, 9]

def selection_sort(ls):
    for i in range(len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[min_index] > ls[j]:
                #min_index = j            # эта строка лишняя
                ls[min_index], ls[j] = ls[j], ls[min_index]
                #min_index = j  # эта строка лишняя
    return ls


print(selection_sort(data))