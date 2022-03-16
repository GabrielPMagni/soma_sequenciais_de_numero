valor = int(input('Digite o valor: '))
valores = []
for y in range(1, valor):
    val_list = []
    somador = 0
    for i in range(y, valor):
        val_list.append(i)
        somador += i
        if somador >= valor:
            if somador == valor: valores.append(val_list)
            val_list = []
            continue
valores.append([valor])

for i in valores:
    for index, j in enumerate(i):
        if index > 0:
            print('+', end='')
        print(j, end='')
    print('\n')

print('Número de sequências: \n', len(valores))
