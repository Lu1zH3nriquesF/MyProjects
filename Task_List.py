
while True:
    option = input('Do you want create a task: [Y]es / [N]o \n').upper()
    task = {}
    task_list = []
    while option == 'Y':

        print(
            'What do you want?: \n 1: Create a task \n 2: Delete a task \n 3: See your tasks \n 4: End'
        )
        select_option = input('Select a option: \n')
        
        if select_option == '1':
            task_name = input('Type a task name: \n')
            description_task = input('Type the task: \n')
            task[task_name] = description_task
            task_list.append(task)
        
        elif select_option == '2':
            if len(task_list) >= 1:
                for tasks, tasks_description in task.items():
                    print('='*40)
                    print(tasks, tasks_description)
                option_delete = input('Do you really want to delete a task? \n [Y]es / [N]o: \n').upper()
                if option_delete == 'Y':
                    try:
                        del_task = (input('Which task do you wish to delete?: \n'))
                        del task[del_task]
                    except KeyError:
                        print('Invalid value.')
                elif option_delete == 'N':
                    continue
                
            else:
                print("You don't have task. ")
                
        elif select_option == '3':
            for tasks, tasks_description in task.items():
                print(f'{tasks}: {tasks_description}')
        
        elif select_option == '4':
            for tasks, tasks_description in task.items():
                print('='*40)
                print(f'{tasks}: {tasks_description}')
                print('='*40)
            print('Goodbye')
            break
        
        else:
            print('Invalid value.')

    if option == 'N':
        break
        

    elif option != 'Y' and 'N':
        print('Invalid value.')

