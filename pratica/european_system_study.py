import math
from time import sleep
scores = {}
subjects = ['Matemática', 'Inglês', 'Geografia', 'Francês', 'História']
reprovado = False
media_final = 0
while True:

    print('-=-'*10)
    print('ACADEMY GENIUS\n')
    print('-=-'*10)
    print('1. Cadrastar\n2. Resultados\n3. Cursos disponiveis\n4. Sair')
    try:
        option = int(input('Selecione sua opção: '))
    except ValueError:
        print('Ops! Digite uma das opções.')
    if option == 1:
         student = str(input('Nome do Aluno: ')).strip().capitalize()
         for sub in subjects:
            while True:  
                try:
                    score = int(input(f'{sub} ( 0 à 20 ): '))
                    if 0 <= score <= 20:
                        scores[sub] = score
                        break  
                    else:
                        print('Valor inválido! Apenas 0 à 20.')
                except ValueError:
                    print('ops! Nota inválida. Tente novamente.')

    elif option == 2:
            while True:
                    student = str(input('Nome: ')).strip().capitalize()
                    for sub, score in scores.items():
                        if score < 10:
                            reprovado = True
                            print(f'[x] {student} REPROVADO por nota baixa em {sub}' )
                    if not reprovado:
                         media_final = sum(scores.values()) / len(subjects)
                    choose = str(input('deseja ver sua média e suas notas?[S/N]: ')).strip().upper()[0]
                    if choose in 'S':
                         print('-=-'*10)
                         print(f'MÉDIA: {media_final}')
                         for k, v in scores.items():
                              print(f'{k}: {v}')
                         break
                    else:
                         break
    if option == 3:
         media_final = sum(scores.values()) / len(subjects)
         if media_final >= 18.5:
              print(f'Parabéns {student}! Você atingiu uma média alta!') 
              print('=='*10)
              print('CURSOS DISPONIVEIS: MEDICINAN\nAEROESPACIAL\nDIREITO\nENFERMAGEM\nADMISTRAÇÃO\nFILOSOFIA')
              break
         elif 13.5 <= media_final <= 17.5:
              print(f'Parabéns {student}! Você atingiu uma média boa!') 
              print('=='*10)
              print('CURSOS DISPONIVEIS: AEROESPACIAL\nDIREITO\nENFERMAGEM\nADMISTRAÇÃO\nFILOSOFIA')
              break
         elif 10 <= media_final <= 12.0:
              print(f'Não foi uma média excelente, mas você ainda tem direito a varios cursos! Confira!')
              print('=='*10)
              print('CURSOS DISPONIVEIS: ADMISTRAÇÃO\nFILOSOFIA')
              break
            
    elif option == 4:
         print('-=-'*10)
         print('OBRIGADA POR ENTRAR NO SISTEMA')
         sleep(1)
         print('-=-'*10)
         break
    