# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def output(data_path):
    with open(data_path, 'r', encoding='UTF8') as f:
        for line in f:
            print(line)
        


def add_contact(data_path):
    list_1 = []
    name_1 = input('Введите имя: ')
    list_1.append(name_1)
    name_2 = input('Введите фамилию: ')
    list_1.append(name_2)
    name_3 = input('Введите отчество: ')
    list_1.append(name_3)
    name_4 = input('Введите номер телефона: ')
    if len(name_4) != 11:
        print('В номере телефона должно быть 11 цифр.')
        name_4 = input('Введите повторно номер телефона: ')
    else:
        list_1.append(name_4)
    with open(data_path, 'a', encoding='UTF8') as data:
        data.write(f'\n{list_1[0]} {list_1[1]} {list_1[2]} {list_1[3]}')
        data.close



def search(data_path):
    search_by = input('Введите информацию для поиска: ')
    print()
    with open(data_path, 'r', encoding='UTF8') as f:
        for line in f:
            if search_by in line:
                return print(line)
        else:
            print("Некорректный ввод")



def change_contact(data_path):
    with open(data_path, 'r+', encoding="utf-8") as f:
        x = input('Введите Имя, Фамилию либо телефон для изменения: ')
        y = input('Введите на что изменить: ')
        old_data = f.read()
        new_data = old_data.replace(x, y)
        with open(data_path, 'w', encoding="utf-8") as f:
            f.write(new_data)



def remove_contact(data_path):
    with open(data_path, 'r', encoding="utf-8") as f:
        x = input('Введите Имя или Фамилию для удаления: ')
        lines = f.readlines()
        with open(data_path, 'w', encoding="utf-8") as f:
            for line in lines:
                if x in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    f.write(line)



def user_action():
    print ('Добро пожаловать! \n1) Вывести весь справочник \n2) Добавить контакт \n3) Найти контакт \n4) Изменить контакт \n5) Удалить контакт')
    while (input1:= int(input('Выберите действие со справочником (0 = выход): '))) != 0:
        if input1 == 1:
            output(data_path)
        elif input1 == 2:
            add(data_path)
        elif input1 == 3:
            search(data_path)
        elif input1 == 4:
            change_contact(data_path)
        elif input1 == 5:
            remove_contact(data_path)
        else:
            print("Некорректный ввод")



data_path = r'C:\Users\ev_ba\Desktop\гикбрейнс\VisualStudia\PYTHON_COURSE\homework 8\phonebookHW.txt'
user_action()



   

