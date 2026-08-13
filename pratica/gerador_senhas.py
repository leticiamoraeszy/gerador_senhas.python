import random
import string
from time import sleep
caracteres = string.ascii_letters 
simbolos = string.punctuation
numeros = random.randint(1,1000)
resultado_final = ''
sorteados = ''

while True:
    print('-=-'*10)
    print('\033[1;36mGERADOR DE SENHAS\033[0m\n')
    print('-=-'*10)
    try:
        tamanho = int(input('Tamanho da senha: '))
        num = str(input('Você quer números na sua senha?[S/N]: ')).upper().strip()[0]
        if num in 'S':
            sorteados = sorteados + str(numeros)
        caract = str(input('Você quer letras na sua senha?[S/N]: ')).upper().strip()[0]
        if caract in 'S':
            sorteados = sorteados + caracteres
        simb = str(input('Você quer simbolos na sua senha?[S/N]: ')).upper().strip()[0]
        if simb in 'S':
            sorteados = sorteados + simbolos
    except ValueError:
        print('Ops! Tente novamente.')

    resultado_final = sorteados
    juntar_elementos = random.choices(resultado_final, k=tamanho)
    mix = ''.join(juntar_elementos)
    print('\033[1;31m==\033[0m'*17)
    print(f'SENHA GERADA: {mix}')
    print('\033[1;31m==\033[0m'*17)
    choice = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if choice in 'N':
        print('Encerrando...', flush=True)
        print('Até a próxima!')
        sleep(1)
        break
        
