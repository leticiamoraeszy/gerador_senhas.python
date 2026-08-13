tasks = []
finished_tasks = []
pending_tasks = []
while True:
        print('='*10)
        print(f'TO DO LIST{"":>7}')
        print('='*10)
        print('1. Add Taskn\n2. Show tasks\n3. Remove task\n4. Status\n 5. Exit')
        option = int(input('Which one will you choose?:  '))

        if option == 1:
            task = str(input('Type your task: ')).capitalize().strip()
            tasks.append(task)
            print('Task added!')
            choice = str(input('Do you wanna another task?[Y/N]: ')).upper().strip()[0]
            while True:
                    if choice in 'Y':
                        task = str(input('Type your task: ')).capitalize().strip()
                        tasks.append(task)
                        print('Task added!')
                        choice = str(input('Do you wanna another task?[Y/N]: ')).upper().strip()[0]
                    else:
                         break
        if option == 2:
                while True:
                    if not tasks:
                        print('\nYour to do list is empty!\n')
                        break
                    else:
                        for t in tasks:
                            print(f'□ {t}\n')
                        print('-='*7)
                        break
        if option == 3:
             select = str(input('Which one you wanna delete?: ')).capitalize().strip()
             if select in tasks:
                  tasks.remove(select)
                  print('Removed')
                  alterative = str(input('Do you wanna remove more tasks?[Y/N]: ')).strip().upper()[0]
                  while True:
                    if alterative in 'Y':
                            select = str(input('Which one you wanna delete?: ')).capitalize().strip()
                            if select in tasks:
                                tasks.remove(select)
                                print('Removed')
                    else:
                            break
                     
        if option == 4:
             print('-='*10)
             decision = str(input('Which task has a update?: ')).capitalize().strip()
             status = str(input('Is it finished? [Y/N]: ')).strip().upper()[0]
             if status in 'Y':
                  finished_tasks.append(decision)
             else:
                  pending_tasks.append(task)
             while True:
                op = str(input('Do you uptade more? [Y/N]: ')).strip().upper()[0]
                if op in 'Y':
                    decision = str(input('Which task has a update?: ')).capitalize().strip()
                    status = str(input('Is it finished? [Y/N]: ')).strip().upper()[0]
                    if status in 'Y':
                            finished_tasks.append(decision)
                    else:
                            pending_tasks.append(decision)
                else:
                     pick = str(input('Do you wanna see your incomplete and complete tasks?[Y/N]: ')).strip().upper()[0]
                     if pick in 'Y':
                          print('-=-'*10)
                          print('COMPLETE TASKS: ')
                          for f in finished_tasks:
                               print(f' ◼︎  {f}')
                          print('-=-'*10)
                          print('INCOMPLETE TASKS: ')
                          for p in pending_tasks:
                                print(f' ◻︎  {f}')
                     break     
                         
        if option == 5:
             print('-=-'*10)
             print('SEE YOU <3\n')
             print('-=-'*10)
             break