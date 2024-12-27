import datetime as dt


# Начало программы
def main():
    # Инициализируем список заметок
    notes = []
    # Создаём заметки
    note = build_note(notes)
    # Выводим заметки
    output(note)
    
    # Цикл для начала работы с заметками
    while True:
        choice = input('\nЖелаете выйти из программы? \n[1] - ✔️  Да \n[2] - ❌ Нет \n>> ')
        
        # Если пользователь хочет выйти из программы, то выходим из цикла
        if choice == '1':
            break
        elif choice == '2':
        # Предлагаем добавить заметку
            while True:
                choice = input('\nЖелаете добавить заметку? \n[1] - ✔️  Да \n[2] - ❌ Нет \n>> ')
                
                # Если пользователь не хочет добавлять заметку, то выходим из цикла
                if choice == '2':
                    break
                # Если пользователь хочет добавить заметку, то вызываем функцию build_note
                elif choice == '1':
                    note = build_note(notes)
                    output(note)
                # Если пользователь ввёл неизвестное действие, то выводим сообщение об ошибке
                else:
                    print('\n❌ Неизвестное действие.\n')
            
            # Предлагаем изменить статус
            while True:
                choice = input('\nЖелаете изменить статус заметки? \n[1] - ✔️  Да \n[2] - ❌ Нет \n>> ')

                # Если пользователь не хочет изменять статус, то выходим из цикла
                if choice == '2':
                    break
                # Если пользователь хочет изменить статус, то вызываем функцию change_status
                elif choice == '1':
                    change_status(notes)
                # Если пользователь ввёл неизвестное действие, то выводим сообщение об ошибке
                else:
                    print('\n❌ Неизвестное действие.\n')
            
            # Предлагаем удалить заметку
            while True:
                choice = input('\nЖелаете удалить заметку? \n[1] - ✔️  Да \n[2] - ❌ Нет \n>> ')

                # Если пользователь не хочет удалять заметку, то выходим из цикла
                if choice == '2':
                    break
                # Если пользователь хочет удалить заметку, то вызываем функцию delete_note
                elif choice == '1':
                    delete_note(notes)
                # Если пользователь ввёл неизвестное действие, то выводим сообщение об ошибке
                else:
                    print('\n❌ Неизвестное действие.\n')

        # Если пользователь ввёл неизвестное действие, то выводим сообщение об ошибке
        else:
            print('\n❌ Неизвестное действие.\n')


# Функция инициализации данных
def data_init():
    # Получаем данные
    username = input("👤 Введите своё имя >> ")
    titles   = title_init()
    content  = input("\n📝 Введите описание заметки >> ")
    dates    = date_init()
    status   = status_init()
    deadline = deadline_init(dates[1], dates[0])
    
    return [username, titles, content, *dates, status, deadline]


# Функция инициализации дат
def date_init():
    # Преобразуем эту дату в единый формат DD-MM-YYYY
    normalize_date = lambda data: data.replace(".", "-").replace("/", "-")
    # Получаем дату создания и дату дедлайна
    while True:
        issue_date_str = normalize_date(input("\n🗓️  Введите дату дедлайна заметки (дд-мм-гггг) >>"))

        # Получаем текущую дату в нужном формате
        create_date = dt.datetime.now().strftime("%d-%m-%Y")
        create_date = dt.datetime.strptime(create_date, "%d-%m-%Y")
        issue_date  = dt.datetime.strptime(issue_date_str, "%d-%m-%Y")

        # Если дата дедлайна больше даты создания, то выходим из цикла
        if issue_date >= create_date:
            return [create_date, issue_date]
        else:
            print('❌ Дата дедлайна не может быть меньше даты создания')


# Функция инициализации заголовков
def title_init():
    # Инициализируем список заголовков и счётчик
    titles, count, title = [], 0, ' '
    print()

    while True:
        # Получаем заголовок
        title = str(input(f'📌 Название заголовка #{count+1} - [Enter] продолжить >> '))
        # Если заголовок не пуст, то проверяем его на уникальность
        if title != '':
            # Если заголовок не уникальный, то выводим сообщение об ошибке
            if title.lower() not in list(map(str.lower, titles)):
                # Добавляем заголовок в список
                titles.append(title)
                count += 1
            else:
                print('\n❌ Такой заголовок же есть!')
        # Если заголовок пуст, то выходим из цикла
        else:
            break

    # Возвращаем список заголовков
    return titles


# Функция инициализации статуса
def status_init():
    # Инициализируем словарь статусов
    statuses = {
        '1': '✔️  Выполнено',
        '2': '🟡 Отложено',
        '3': '❌ Не выполнено'
    }

    while True:
        # Выводим статусы в виде таблицы
        print('\nДоступные статусы:\n')
        for key, value in statuses.items():
            print(f'[{key}] - {value}')
    
        # Получаем статус заметки
        status = input("\nВведите статус заметки >> ")
        
        # Если статус валидный, то возвращаем его
        if status in statuses:
            print()
            return statuses.get(status)
        # Если статус не валидный, то возвращаем сообщение об ошибке
        else:
            print ('\n❌ Неизвестный статус\n')


# Функция подсчёта времени до дедлайна
def deadline_init(deadline_date, create_date):
    # Получаем разницу между датами
    deadline = deadline_date - create_date

    # Возвращаем разницу в виде строки
    if deadline.days <= 0:
        return '🔔 Дедлайн уже сегодня!'
    elif deadline.days == 1:
        return '🔔 Дедлайн завтра!'
    else:
        return '🔔 Дедлайн через ' + str(deadline.days) + ' дней!'
     

# Функция сборки заметки
def build_note(notes):
    # Получаем данные
    data = data_init()

    # Формируем словарь с данными
    note = {
        '👤 Ваше имя'           : data[0],
        '📌 Заголовки'          : data[1],
        '📝 Описание заметки'   : data[2],
        '📅 Дата создания'      : data[3].strftime("%d-%m"),
        '⏰ Дата дедлайна'      : data[4].strftime("%d-%m"),
        '🔔 Статус'             : data[5],
        '⌛ До дедлайна'        : data[6]
    }
    
    notes.append(note)

    return notes


# Функция вывода данных
def output(notes):
    for note in notes:
        # Выводим заголовок
        print(f'\n{"="*50}\n📝 Заметка #{notes.index(note)+1}:\n{"="*50}')
    
        # Выводим данные в виде таблицы
        for key, value in note.items():
            # Если значение - список, то применяем метод join для вывода в виде строки
            if type(value) == list:
                print(f'{key}: {", ".join(value)}')
            # Если значение - строка, то выводим его в виде строки
            else:
                print(f'{key}: {value}')


# Функция замены статуса
def change_status(notes):
    while True:
        # Получаем номер заметки
        note_number = int(input(f'\n📝 Введите номер заметки (1-{len(notes)})>> '))
        # Если номер заметки валидный, то заменяем статус
        if note_number > 0 and note_number <= len(notes):
            notes[note_number-1]['🔔 Статус'] = status_init()
            print('\n✅ Статус заметки изменён.\n')
            output(notes)
            break
        # Если номер заметки не валидный, то выводим сообщение об ошибке
        else:
            print('\n❌ Такой заметки нет.\n')


# Функция удаления заметки
def delete_note(notes):
    while True:
        # Получаем номер заметки
        note_number = int(input(f'\n📝 Введите номер заметки (1-{len(notes)})>> '))
        # Если номер заметки валидный, то удаляем заметку
        if note_number > 0 and note_number <= len(notes):
            notes.pop(note_number-1)
            print('\n✅ Заметка удалена.\n')
            output(notes)
            break
        # Если номер заметки не валидный, то выводим сообщение об ошибке
        else:
            print('\n❌ Такой заметки нет.\n')


# Старт программы
if __name__ == '__main__':
    main()
