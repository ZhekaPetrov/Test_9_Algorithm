#Дана последовательность чисел длинной N
#Найти минимальное четное число в последовательности или вывести -1, если такого не существует.

def min_chetnoe(N):
    ans = -1
    for i in range(len(N)):
        if N[i] % 2 == 0 and (ans == -1 or N[i] < ans):
            ans = N[i]
        
    return ans


result = min_chetnoe([1, 5, 4, 3, 2])
print(result)