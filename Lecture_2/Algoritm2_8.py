#Дана строка (возможно пустая), состоящая из букв A-Z: AAAABBBCCCXYZDDDDEEEFFFAAAAAAAAAAABBBBBBBBBBBBBBBBBBBB
#Нужно написать функцию, которая на выходе даст строку вида: ABCXYZDEFAB.

def easy(s):
    lastsym = s[0]
    ans = []
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(lastsym)
            lastsym = s[i]
    ans.append(lastsym)
    return ''.join(ans)


a = easy('AAABBBCCCDDXZZZYYEEDDGG')
print(a)