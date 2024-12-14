#Дана последовательность чисел длинной N
#Найти последнее (правое) вхождение числа x в нее или вывести -1, если число x не встречалось.
def right_num(N, x):
    ans = -1
    for i in range(len(N)):
        if N[i] == x:
            ans = i
    return ans


result = right_num([1, 2, 3, 3, 2], 2)
print(f"Индекс числа x = {result}")
