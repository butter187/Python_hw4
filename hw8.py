# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления
# данных. Пользователь также может ввести имя или фамилию, и Вы должны
# реализовать функционал для изменения и удаления данных

phone_book = {}
PATH = 'phones.txt'


def open_file(book: list):
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        book[i] = contact


def save_file(book: dict):
    all_contacts = []
    for contact in book.values():
        all_contacts.append(';'.join(contact))
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(all_contacts))


def show_contacts(book: dict, message: str):
    print('\n' + '=' * 67)
    if book:
        for i, contact in book.items():
            print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
    else:
        print(message)
    print('=' * 67 + '\n')


def add_new_contact(book: dict, new: list):
    cur_id = max(book.keys()) + 1
    book[cur_id] = new


def find_contact(book: dict, search: str):
    resault = {}
    for i, contact in book.items():
        for field in contact:
            if search.lower() in field.lower():
                resault[i] = contact
                break
    return resault


def func_search(book: dict):
    search = input('Что будем искать? ')
    resault = find_contact(phone_book, search)
    show_contacts(resault, f'Контакт содержащий {search} не найден!')


def change_contact(book: dict, cid: int):
    name, phone, comment = book.get(cid)
    ch = []
    for item in ['Введите новое имя (или оставьте пустым чтобы не изменять): ',
                 'Введите новый телефон (или оставьте пустым чтобы не изменять):',
                 'Введите новый комментарий (или оставьте пустым чтобы не изменять):']:
        ch.append(input(item))
    book[cid] = [ch[0] if ch[0] else name, ch[1] if ch[1] else phone, ch[2] if ch[2] else comment]
    return ch[0] if ch[0] else name


def delete_contact(book: dict, cid: int):
    name = book.pop(cid)
    return name[0]


def menu():
    menu_points = ['Открыть файл',
                   'Сохронить файл',
                   'Посмотреть все контакты',
                   'Добавить контакты',
                   'Найти контакт',
                   'Изменить контакт',
                   'Удалить контакт',
                   'Выход']
    print('Главное меню')
    [print(f'\t{i}. {item}') for i, item in enumerate(menu_points, 1)]
    choice = int(input('Выберите пункт: '))
    return choice


while True:
    choice = menu()
    match choice:
        case 1:
            open_file(phone_book)
            print('\Телефонная книга успешно открыта!\n')
        case 2:
            save_file(phone_book)
            print(f'\nТелефонная книга успешно сохранена!\n')
        case 3:
            show_contacts(phone_book, 'Телефонная книга пуста или не открыта')
        case 4:
            new = []
            for item in ['Введите имя: ', 'Введите номер: ', 'Введите комент: ']:
                new.append(input(item))
            add_new_contact(phone_book, new)
            print(f'\nКонтакт {new[0]} успешно добавлен!\n')
        case 5:
            func_search(phone_book)
        case 6:
            func_search(phone_book)
            select = int(input('Какой контакт будем изменять? '))
            name = change_contact(phone_book, select)
            print(f'\nКонтакт {name} успешно изменён!\n')
        case 7:
            func_search(phone_book)
            select = int(input('Какой контакт будем удалять? '))
            name = delete_contact(phone_book, select)
            print(f'\nКонтакт {name} успешно удалён!\n')
        case 8:
            print('\nВсего хорошего!')
            break