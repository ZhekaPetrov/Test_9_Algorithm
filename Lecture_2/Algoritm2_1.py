#Дана последовательность чисел длинной N
#Найти первое (левое) вхождение положительного числа X в нее или вывести -1, если число x не встречалось.
def left_num(N, x):
    ans = -1
    for i in range(len(N)):
        if ans == -1 and N[i] == x:
            ans = i
    return ans


result = left_num([1, 2, 3 , 1, 3, 4], 3)
print(f"Индекс числа x = {result}")