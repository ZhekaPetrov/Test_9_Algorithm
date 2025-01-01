#Хэш таблица
setsize = 10
myset = [[] for _ in range(setsize)]    #Создание двумерного списка
  
def add(x):                             #Операция "Добавить элемент"
    myset[x % setsize].append(x)

def find(x):                            #Операция "Поиск элемента"
    for now in myset[x % setsize]:
        if now == x:
            return True
        return False


def delete(x):                          #Операция "Удаление элемента"
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return
        