import datetime as dt


# Начало программы
def main():
    # Инициализируем список заметок
    notes = []
    # Инициализируем меню
    menu = {
        '1': '✏️  Редактировать заметки',
        '2': '⭕ Выйти из программы'
    }
    # Инициализируем меню редактирования заметок
    options = {
        '1': '📝 Показать все заметки',
        '2': '✏️  Добавить заметку',
        '3': '❌ Удалить заметку',
        '4': '🟡 Изменить статус заметки',
        '5': '✅ Выйти в меню'
    }
    
    # Цикл для начала работы с заметками
    while True:
        # Выводим меню
        print('\n' + '='*50 + '\nМеню:')
        dict_output(menu)
        print('='*50)
        choice = menu.get(input('Выберите действие >> '))
        
        # Если пользователь хочет выйти из программы, то выходим из цикла
        if choice == '⭕ Выйти из программы':
            break
        # Если пользователь хочет редактировать заметки, то выводим меню редактирования заметок
        elif choice == '✏️  Редактировать заметки':
            # Цикл для выбора действия
            while True:
                # Выводим меню редактирования заметок
                print('\n' + '='*50 + '\nРедактирование заметок:')
                dict_output(options)
                print('='*50)
                choice = options.get(input('Выберите действие >> '))
                
                # Если пользователь хочет показать все заметки, то выводим их
                if choice == '📝 Показать все заметки':
                    output(notes)
                # Если пользователь хочет добавить заметку, то добавляем её
                elif choice == '✏️  Добавить заметку':
                    notes = build_note(notes)
                    output(notes)
                # Если пользователь хочет удалить заметку, то удаляем её
                elif choice == '❌ Удалить заметку':
                    delete_note(notes)
                # Если пользователь хочет изменить статус заметки, то изменяем его
                elif choice == '🟡 Изменить статус заметки':
                    change_status(notes)
                # Если пользователь хочет выйти в меню, то выходим из цикла
                elif choice == '✅ Выйти в меню':
                    break
                # Если пользователь ввёл неизвестное действие, то выводим сообщение об ошибке
                else:
                    print('\n❌ Неизвестное действие.\n')
        # Если пользователь ввёл неизвестное действие, то выводим сообщение об ошибке
        else:
            print('\n❌ Неизвестное действие.\n')


# Функция вывода словаря в виде таблицы
def dict_output(dict_):
    for key, value in dict_.items():
        if type(value) != list:
            print(f'{key} - {value}')
        else:
            print(f'{key}: {", ".join(value)}')


# Функция инициализации данных
def data_init():
    print(f'\n{"="*50}\nСоздание заметки...✏️\n{"="*50}')
    # Получаем данные
    username = input("\n👤 Введите своё имя >> ")
    titles   = title_init()
    content  = input("\n📝 Введите описание заметки >> ")
    dates    = date_init()
    status   = status_init()
    deadline = deadline_init(dates[1], dates[0])
    
    return [username, titles, content, *dates, status, deadline]


# Функция инициализации дат
def date_init():
    # Преобразуем эту дату в единый формат DD-MM-YYYY
    normalize_date = lambda date: date.replace(".", "-").replace("/", "-")
    
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
        dict_output(statuses)
    
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
    # Инициализируем список заметок
    func_notes = notes
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
    
    func_notes.append(note)

    return func_notes


# Функция вывода данных
def output(notes):
    func_notes = notes
    for i, note in enumerate(func_notes, 1):
        # Выводим заголовок
        print(f'\n{"="*50}\n📝 Заметка #{i}:\n{"="*50}')
        # Выводим данные в виде таблицы
        dict_output(note)


# Функция замены статуса
def change_status(notes):
    # Инициализируем список заметок
    func_notes = notes
    while True:
        # Получаем номер заметки
        note_number = int(input(f'\n📝 Введите номер заметки (1-{len(func_notes)})>> '))
        # Если номер заметки валидный, то заменяем статус
        if note_number > 0 and note_number <= len(func_notes):
            func_notes[note_number-1]['🔔 Статус'] = status_init()
            print('\n✅ Статус заметки изменён.\n')
            output(func_notes)
            break
        # Если номер заметки не валидный, то выводим сообщение об ошибке
        else:
            print('\n❌ Такой заметки нет.\n')


# Функция удаления заметки
def delete_note(notes):
    # Инициализируем список заметок
    func_notes = notes
    while True:
        # Получаем номер заметки
        note_number = int(input(f'\n📝 Введите номер заметки (1-{len(func_notes)})>> '))
        # Если номер заметки валидный, то удаляем заметку
        if note_number > 0 and note_number <= len(func_notes):
            func_notes.pop(note_number-1)
            print('\n✅ Заметка удалена.\n')
            output(func_notes)
            break
        # Если номер заметки не валидный, то выводим сообщение об ошибке
        else:
            print('\n❌ Такой заметки нет.\n')


# Старт программы
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n⚠️  Программа завершена аварийно.')
