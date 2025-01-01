#Дана последовательность положительных чисел длинной N и число X.
#Нужно найти два различных числа А и В из последовательности, таких что А + В = Х или вернуть пару 0, 0, если такой пары чисел нет
#       Решение O(N)
def twotermswithsumx(nums, x):
    prevnums = set()
    for nownum in nums:
        if x - nownum in prevnums:
            return nownum, x - nownum
        prevnums.add(nownum)
    return 0, 0


a = twotermswithsumx([1, 2, 3, 4, 5, 6], 11)
print(a)
#Выведет (6, 5)

b = twotermswithsumx([1, 2, 3, 4, 5, 6], 18)
print(b)
#Выведет (0, 0)