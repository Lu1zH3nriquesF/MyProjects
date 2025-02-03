import json
import os
def delete_task(task, delete_list):
    if not task:
        print("You don't have tasks to delete")
        return
    
    n = input('What task do you want to delete: \n')    
    task_deleted_list = task.pop(task.index(n))
    delete_list.append(task_deleted_list)


def remake_task(task, remake_task_list):
    if not task:
        print("You don't have tasks")
        return
    
    remake_list = remake_task_list.pop()
    task.append(remake_list)
    
def read(tasks, file_way):
    datas = []
    try:
        with open(file_way, 'r', encoding='utf-8') as file:
            datas = json.load(file)
    except FileNotFoundError:
        print('File not found.')
        save(tasks, file_way)
    return datas

def save(task, file_way):
    # datas = task
    with open(file_way, 'w+', encoding='utf-8') as file:
        datas = json.dump(task, file, indent=4, ensure_ascii=False)
    return datas  

def list_tasks(tasks):
    for task in tasks:
        print('-'*20)
        print(task)
        print('-'*20)
    return
 
tasks_list = []
FILE_WAY = 'Tasks.json'
second_list_tasks = []
tasks_save = read(tasks_list, FILE_WAY)

while True:
    option = input('What do you want to do?\
        \n-1. Create a task\
        \n-2. Delete a task\
        \n-3. Remade a task\
        \n-4. See all tasks\
        \n-5. Exit\
        \nChoice one between this options: \n').capitalize()

    if option == '1':
        os.system('cls')
        task = input('Typed your task: \n')
        tasks_list.append(task)
        list_tasks(tasks_list)
        print('Your task was created.')
    
    elif option == '2':
        os.system('cls')
        try:   
            delete_task(tasks_list, second_list_tasks)
            print()
            print('Your task was deleted.')
            list_tasks(tasks_list)
        except IndexError:
            print('There are no tasks to delete.')
        
    elif option == '3':
        os.system('cls')
        try:   
            remake_task(tasks_list, second_list_tasks)
            print()
            print('Your task was remade.')
            list_tasks(tasks_list)
        except IndexError:
            print('You don\'t have tasks to remade.')
        
    elif option == '4':
        os.system('cls')
        list_tasks(tasks_list)
    
    elif option == '5':
        os.system('cls')
        list_tasks(tasks_list)
        print()
        print('Thanks for the visit.')
        break
    
    else:
        os.system('cls')
        print()
        print('Invalid value!')
    
    save(tasks_list, FILE_WAY)

