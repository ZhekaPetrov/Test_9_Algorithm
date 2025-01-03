#Дана последовательность положительных чисел длинной N и число X.
#Нужно найти два различных числа А и В из последовательности, таких что А + В = Х или вернуть пару 0, 0, если такой пары чисел нет
#       Решение O(N^2)
def twotermswithsumx(nums, x):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == x:
                return nums[i], nums[j]
    return 0, 0


a = twotermswithsumx([1, 2, 3, 4, 5, 6], 10)
print(a)
#Выводит (4, 6)

b = twotermswithsumx([1, 2, 3, 4, 5, 6], 13)
print(b)
#Выводит (0, 0)