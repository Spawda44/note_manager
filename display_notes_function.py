import datetime as dt
from colorama import Fore as f, Style as s


# Начало программы
def main():
    # Инициализируем список заметок
    notes = []
    # Инициализируем меню
    menu = {
        '1': '📝 Показать все заметки',
        '2': '✏️  Редактировать заметки',
        '3': '🔰 Добавить заметку',
        '4': '⭕ Выйти из программы'
    }
    # Инициализируем меню редактирования заметок
    options = {
        '1': '❌ Удалить заметку',
        '2': '📝 Редактировать заметку',
        '3': '💠 Выйти в меню'
    }
    # Основный цикл программы
    while True:
        # Выводим меню
        print(f'{f.YELLOW+s.BRIGHT}\n{"="*50}\nМеню:')
        dict_output(menu)
        print(f'{"="*50}')
        
        choice = menu.get(input(f'Выберите действие >> {f.WHITE}'))

        if choice == '⭕ Выйти из программы':
            break
        elif choice == '🔰 Добавить заметку':
            notes = build_note(notes)
            display_notes(notes)
        elif choice == '✏️  Редактировать заметки':
            # Цикл для выбора действия
            while True:
                # Выводим меню
                print(f'{f.CYAN+s.BRIGHT}\n{"="*50}\nМеню редактирования заметок:')
                dict_output(options)
                print(f'{"="*50}')

                choice = options.get(input(f'Выберите действие >> {f.WHITE}'))

                if choice == '💠 Выйти в меню':
                    break
                elif choice == '❌ Удалить заметку':
                    if len(notes) == 0:
                        print('\n❌ Заметок нет.')
                    else:
                        delete_note(notes)
                        display_notes(notes)
                elif choice == '📝 Редактировать заметку':
                    if len(notes) == 0:
                        print('\n❌ Заметок нет.')
                    else:
                        update_note(notes)
                else:
                    print('\n❌ Неизвестное действие')

        elif choice == '📝 Показать все заметки':
            if len(notes) == 0:
                print('\n❌ Заметок нет.')
            else:
                display_notes(notes)
        else:
            print('\n❌ Неизвестное действие')


# Функция вывода словаря в виде таблицы
def dict_output(dict_):
    for key, value in dict_.items():
        if type(value) != list:
            print(f'{key}: {value}')
        else:
            print(f'{key}: {", ".join(value)}')


# Функция редактирования заметки
def update_note(notes):
    # Инициализируем меню редактирования заметок
    options = {
    '1': '👤 Сменить имя',
    '2': '📌 Сменить заголовки',
    '3': '📝 Сменить описание',
    '4': '🗓️  Сменить дату создания',
    '5': '⏰ Сменить дату дедлайна',
    '6': '🔔 Сменить статус',
    '7': '💠 Назад'
    }
    while True:
        note_number = int(input(f'\n📝 Введите номер заметки (1-{len(notes)})'))

        if note_number > 0 and note_number <= len(notes):
            # Цикл для выбора действия
            while True:
                # Выводим меню редактирования заметки
                print(f'{f.GREEN+s.BRIGHT}\n{"="*50}\nМеню редактирования заметки #{note_number}:')
                dict_output(options)
                print(f'{"="*50}')

                choice = options.get(input(f'Выберите действие >> {f.WHITE}'))

                if choice == '💠 Назад':
                    return
                elif choice == '👤 Сменить имя':
                    notes[note_number-1]['👤 Ваше имя'] = user_init()
                    print('\n✅ Имя заметки изменено.\n')
                    display_notes(notes)
                elif choice == '📌 Сменить заголовки':
                    notes[note_number-1]['📌 Заголовки'] = title_init()
                    print('\n✅ Заголовки заметки изменены.\n')
                    display_notes(notes)
                elif choice == '📝 Сменить описание':
                    notes[note_number-1]['📝 Описание заметки'] = content_init()
                    print('\n✅ Описание заметки изменено.\n')
                    display_notes(notes)
                elif choice == '🗓️  Сменить дату создания':
                    notes[note_number-1]['📅 Дата создания'] = create_date_init().strftime("%d-%m-%Y")
                    print('\n✅ Дата создания изменена.\n')
                    display_notes(notes)
                elif choice == '⏰ Сменить дату дедлайна':
                    date = issue_date_init()
                    notes[note_number-1]['⏰ Дата дедлайна'] = dt.datetime.strftime(date, "%d-%m-%Y")
                    print('\n✅ Дата дедлайна изменена.\n')
                    notes[note_number-1]['⌛ До дедлайна'] = deadline_init(date)
                    display_notes(notes)
                elif choice == '🔔 Сменить статус':
                    notes[note_number-1]['🔔 Статус'] = status_init()
                    print('\n✅ Статус заметки изменен.\n')
                    display_notes(notes)
                else:
                    print('\n❌ Неизвестное действие\n')
        else:
            print('\n❌ Такой заметки нет.\n')


# Функция сборки заметки
def build_note(notes):
    # Инициализируем список заметок
    func_notes = notes

    print(f'\n{"="*50}\nСоздание заметки...✏️\n{"="*50}')
    # Получаем данные
    username = user_init()    or 'N/A'
    titles   = title_init()   or 'N/A'
    content  = content_init() or 'N/A'
    dates    = [create_date_init(), issue_date_init()]
    status   = status_init()
    deadline = deadline_init(dates[1])

    # Формируем словарь с данными
    note = {
        '👤 Ваше имя'           : username,
        '📌 Заголовки'          : titles,
        '📝 Описание заметки'   : content,
        '📅 Дата создания'      : dates[0].strftime("%d-%m-%Y"),
        '⏰ Дата дедлайна'      : dates[1].strftime("%d-%m-%Y"),
        '🔔 Статус'             : status,
        '⌛ До дедлайна'        : deadline
    }
    
    func_notes.append(note)

    return func_notes


# Функции инициализации данных: Имя пользователя, описание заметки
user_init      = lambda: input(f"\n{f.WHITE}👤 Введите своё имя >> ")
content_init   = lambda: input(f"\n{f.WHITE}📝 Введите описание заметки >> ")


# Функция нормализации даты
normalize_date = lambda date: date.replace(".", "-").replace("/", "-")


# Функция инициализации даты создания
def create_date_init():
    try:
        create_date = normalize_date(input("\n🗓️  Введите дату создания заметки (дд-мм-гггг) >>"))
        create_date = dt.datetime.strptime(create_date, "%d-%m-%Y")
    except ValueError:
        print('\n❌ Некорректная дата!')
        return create_date_init()
    
    return create_date


# Функция инициализации даты дедлайна
def issue_date_init():
    try:
        issue_date = normalize_date(input("\n🗓️  Введите дату дедлайна заметки (дд-мм-гггг) >>"))
        issue_date  = dt.datetime.strptime(issue_date, "%d-%m-%Y")
    except ValueError:
        print('\n❌ Некорректная дата!')
        return issue_date_init()

    return issue_date


# Функция инициализации заголовков
def title_init():

    titles, count, title = [], 0, ' '
    print(f'\n{"="*50}\n📌 Введите заголовки заметки, [Enter] - что бы продолжить\n{"="*50}')

    while True:
        # Получаем заголовок
        title = str(input(f'📌 Заголовок #{count+1} >> '))
        # Если заголовок не пуст, то проверяем его на уникальность
        if title != '':
            if title.lower() not in list(map(str.lower, titles)):
                titles.append(title)
                count += 1
            else:
                print('\n❌ Такой заголовок уже есть!')
        else:
            break

    return titles


# Функция инициализации статуса
def status_init():
    # Инициализируем словарь статусов
    statuses = {
        '1': f'{f.GREEN}✔️  Выполнено{f.WHITE}',
        '2': f'{f.YELLOW}🟡 Отложено{f.WHITE}',
        '3': f'{f.RED}❌ Не выполнено{f.WHITE}'
    }
    while True:
        print(f'\n{"="*50}\nДоступные статусы:')
        dict_output(statuses)
        print(f'{"="*50}')
        
        status = input("\nВведите статус заметки >> ")
        
        if status in statuses:
            return statuses.get(status)
        else:
            print ('\n❌ Неизвестный статус')


# Функция подсчёта времени до дедлайна
def deadline_init(deadline_date):
    # Вычисляем разницу между датами
    deadline = deadline_date - dt.datetime.now()

    if deadline.days == 0:
        return f'{f.YELLOW}🔔 Дедлайн уже сегодня!{f.WHITE}'
    elif deadline.days < 0:
        return f'{f.RED}❗ Дедлайн уже прошёл!{f.WHITE}'
    else:
        return f'{f.YELLOW}🔔 Дедлайн через {deadline.days} дней!{f.WHITE}'
     

# Функция вывода данных
def display_notes(notes):
    func_notes = notes
    for i, note in enumerate(func_notes, 1):
        print(f'{s.BRIGHT}\n{"="*50}\n📝 Заметка #{i}:\n{"="*50}')
        dict_output(note)


# Функция удаления заметки
def delete_note(notes):
    func_notes = notes
    while True:
        note_number = int(input(f'\n📝 Введите номер заметки (1-{len(func_notes)})>> '))
        if note_number > 0 and note_number <= len(func_notes):
            func_notes.pop(note_number-1)
            print('\n✅ Заметка удалена.\n')
            display_notes(func_notes)
            break
        else:
            print('\n❌ Такой заметки нет.\n')


# Старт программы [Ctrl+C] для выхода из программы
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n⚠️  Программа завершена аварийно.')