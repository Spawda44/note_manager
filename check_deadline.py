#==============================================
# Импорт библиотек
#==============================================


import datetime


#==============================================
# Функция приведения даты к формату DD-MM-YYYY
#==============================================


# Получаем дату в любом формате
def normalize_date(date_str):
    # Преобразуем эту дату в единый формат DD-MM-YYYY
    return date_str.replace(".", "-").replace("/", "-")


#==============================================
# Функция инициализации данных
#==============================================


def data_init():

    # Получаем данные об имени и описании заметки
    username = input("👤 Введите своё имя >> ")
    content  = input("📝 Введите описание заметки >> ")

    while True:
        # Получаем дату создания и дату дедлайна
        create_date_str = normalize_date(input("🗓️  Введите дату создания заметки (дд-мм-гггг) >>"))
        issue_date_str  = normalize_date(input("🗓️  Введите дату дедлайна заметки (дд-мм-гггг) >>"))

        # Преобразуем даты в объекты datetime
        create_date = datetime.datetime.strptime(create_date_str, "%d-%m-%Y")
        issue_date  = datetime.datetime.strptime(issue_date_str, "%d-%m-%Y")

        # Если дата дедлайна больше даты создания, то выходим из цикла
        if issue_date >= create_date:
            break
        else:
            print('❌ Дата дедлайна не может быть меньше даты создания')
    
    # Возвращаем данные в виде списка
    return [username, content, create_date, issue_date]


#==============================================
# Функция инициализации заголовков
#==============================================


def title_init():
    # Инициализируем список заголовков и счётчик
    titles, count, title = [], 0, ' '

    while True:
        # Получаем заголовок
        title = str(input(f'\nНазвание заголовка {count+1} - [Enter] продолжить >> '))
        # Если заголовок не пуст, то проверяем его на уникальность
        if title != '':
            # Если заголовок не уникальный, то выводим сообщение об ошибке
            if title.lower() not in list(map(str.lower, titles)):
                # Добавляем заголовок в список
                titles.append(title)
                count += 1
            else:
                print('\n❌ Такой заголовок уже есть!')
        # Если заголовок пуст, то выходим из цикла
        else:
            break

    # Возвращаем список заголовков
    return titles


#==============================================
# Функция инициализации статусов
#==============================================


def status_init():
    
    # Инициализируем словарь статусов
    statuses = {
        '1': '✔️  Выполнено',
        '2': '🟡 В процессе',
        '3': '❌ Не выполнено'
    }

    while True:
    # Выводим статусы в виде таблицы
        for key, value in statuses.items():
            print(f'[{key}] - {value}')
    
        # Получаем статус заметки
        status = input("Введите статус заметки >> ")
        
        # Если статус валидный, то возвращаем его
        if status in statuses:
            return statuses.get(status)
        # Если статус не валидный, то возвращаем сообщение об ошибке
        else:
            print ('\n❌ Неизвестный статус\n')


#==============================================
# Функция инициализации дедлайна
#==============================================


def deadline_init(deadline_date, create_date):
    
    # Получаем разницу между датами
    deadline = deadline_date - create_date

    # Возвращаем разницу в виде строки
    if deadline.days <= 0:
        return 'Дедлайн уже сегодня!'
    elif deadline.days == 1:
        return 'Дедлайн завтра!'
    else:
        return 'Дедлайн через ' + str(deadline.days) + ' дней!'
     

#==============================================
# Сборка заметки
#==============================================


def build_note():
    
    # Получаем данные
    data = data_init()
    data.extend([status_init(), title_init(), deadline_init(data[3], data[2])])

    # Формируем словарь с данными
    note = {
        '👤 Ваше имя'          : data[0],
        '📌 Заголовки'         : data[5],
        '📝 Описание заметки'  : data[1],
        '📅 Дата создания'     : data[2].strftime("%d-%m"),
        '⏰ Дата дедлайна'     : data[3].strftime("%d-%m"),
        '🔔 Статус'            : data[4],
        '⌛ До дедлайна'       : data[6]
    }

    return note


#==============================================
# Функция вывода данных
#==============================================


def output(data):
    
    # Выводим заголовок
    print('='*50 + '\n📝 Ваша заметка:\n' + '='*50)
    
    # Выводим данные в виде таблицы
    for key, value in data.items():
        # Если значение - список, то применяем метод join для вывода в виде строки
        if type(value) == list:
            print(f'{key}: {", ".join(value)}')
        # Если значение - строка, то выводим его в виде строки
        else:
            print(f'{key}: {value}')


#==============================================
# Начало программы
#==============================================


def main():

    # Создаём и выводим заметку
    output(build_note())

if __name__ == '__main__':
    main()