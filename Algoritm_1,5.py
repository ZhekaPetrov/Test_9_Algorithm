#Сумма последовательности
seq = list(map(int, input('Введите последовательность цифр: ').split()))
seqsum = 0
for i in range(len(seq)):
    seqsum += seq[i]
print(seqsum)