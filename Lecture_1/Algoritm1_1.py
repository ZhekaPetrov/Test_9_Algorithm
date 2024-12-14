#Время: O(N^2)
#Память: O(N)
print("Данная программа считает и выводит самый частый символ. Введите любой порядок символов: ")
a = input('Введите текст: ') 
simvol = []      
p1 = 0
for i in range(len(a)):
    p2 = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            p2 += 1
    if p1 < p2:
        p1 = p2
        simvol = a[i]
print(simvol) 


