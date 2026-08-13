from time import sleep

lista = ['Manga', 'Uva', 'Pêra', 'Limão']
for lista in lista:
    print(lista)
numbers = []
triple_numbers = []
quant = int(input('Quantos números você quer digitar?: '))
for quant in range(quant + 1):
    number = int(input('Digite um número: '))
    numbers.append(number)
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 3
    triple_numbers.append(numbers[i])
print('OS NUMEROS TRIPLICADOS:')
print(triple_numbers)