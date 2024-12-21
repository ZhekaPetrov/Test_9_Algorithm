#Дана последовательность слов
#Вывести все самые короткие слова через пробел
#Решаем через два прохода:
def shortwords(words):
    minlen = len(words[0])
    for word in words:           #На первом проходе ищем самое короткое слово
        if len(word) < minlen:
            minlen = len(words)
    ans = ''
    for word in words:           #На втором проходе ищем такие же короткие слова и записываем через пробел
        if len(word) == minlen:
            ans += word + ' '    #Медленно потому что каждый раз копируется все накопленное
    return ans


a = shortwords(['car', 'apple', 'dogs', 'cat', 'banana', 'mountens'])
print(a)

#Более быстрое решение
def shortwords(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(words)
    ans = []
    for word in words:
        if len(word) == minlen:
            ans.append(word)
    return ' '.join(ans)


a = shortwords(['car', 'apple', 'dogs', 'cat', 'banana', 'mountens'])
print(a)