#Дана стока (возможно пустая), состоящая из букв A-Z: AAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBB
#Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28. И сгенерирует ошибку, если на вход пришла невалидная строка.
#Пояснение: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений.

def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s
    lastsym = s[0]
    lastpos = 0
    ans = []
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ''.join(ans)


a = rle('AAABBBCCCDDXZZZYYEEDDGG')
print(a)