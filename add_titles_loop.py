import datetime as dt


# Начало программы
def main():
    # Инициализируем список заметок
    notes = []
    # Создаём заметки
    note = build_note(notes)
    # Выводим заметки
    output(note)
    

# Функция приведения даты к формату DD-MM-YYYY
def normalize_date(date_str):
    # Преобразуем эту дату в единый формат DD-MM-YYYY
    return date_str.replace(".", "-").replace("/", "-")


# Функция инициализации данных
def data_init():
    # Получаем данные
    username = input("👤 Введите своё имя >> ")
    titles   = title_init()
    content  = input("\n📝 Введите описание заметки >> ")
    dates    = date_init()
    status   = status_init()
    
    return [username, titles, content, *dates, status]


# Функция инициализации дат
def date_init():
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
        '2': '🟡 В процессе',
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


# Старт программы
if __name__ == '__main__':
    main()