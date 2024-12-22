import datetime


# Функция для нормализации даты


def normalize_date(date_str):
   # Заменяем точки и слеши на дефисы
   return date_str.replace('.', '-').replace('/', '-')


# Функция для запроса данных о заметке data


def data_init():

  username         = input('\nИмя пользователя >> ')
  content          = input('Описание заметки >> ')
  
  # Нормализуем введенную дату, заменяя разделители на дефисы
  created_date_str = normalize_date(input('Дата создания заметки >> '))
  issue_date_str   = normalize_date(input('Дата истечения заметки >> '))
  
  # Преобразуем строки в объекты datetime
  created_date     = datetime.datetime.strptime(created_date_str, '%d-%m-%Y')
  issue_date       = datetime.datetime.strptime(issue_date_str, '%d-%m-%Y')
  
  return [username, content, created_date, issue_date]


# Функция для запроса статуса заметки status


def status_init():
  
  # Словарь для хранения соответствия между цифровым выбором пользователя
  # и текстовым представлением статуса
  
  statuses = {
    '1': 'В процессе',  # Статус для активных заметок
    '2': 'Выполнено',   # Статус для завершенных заметок
    '3': 'Отложено'     # Статус для отложенных заметок
  }

  while True:
    print('\nСтатус заметки:\n1 - В процессе\n2 - Выполнено\n3 - Отложено')
    
    choice = input('Выберите пункт 1-3 >> ')
    
    # Проверка есть ли выбор в словаре статусов
    if choice in statuses:
      return statuses[choice]  # Возврат текстового значения статуса
      
    # Сообщение об ошибке при неверном выборе
    print('\nТакого статуса не существует')


# Функция для запроса заголовков titles


def title_init():

  titles, title, count = [], ' ', 0
  
  while True:

    title = str(input(f'\nНазвание заголовка {count+1} - [Enter] продолжить >> '))
    
    # Проверка строки title на пустоту, если строка пустая принудительно завершаем цикл
    # Проверка строки на дубликаты в списке, если дубликат есть - не добавляем в список
    
    if title != '':
      if title.lower() not in (map(str.lower, titles)):
        titles.append(title)
        i += 1
      else:
        print('Обнаружен дубликат! Удаление...')
    else:
      break

  return titles


# Функция для вывода данных в консоль


def output(note):
  
  print('\nВы ввели следующие данные:\n')
  
  for key, value in note.items():
    
    # Используем f-строку и преобразуем список в строку через join если это список
    value_str = ', '.join(value) if isinstance(value, list) else value
    print(f'{key}: {value_str}')


# Функция для проверки дедлайна

 
def check_deadline(created_date, issue_date):
  current_date = datetime.datetime.now()
   
  # Проверяем, что дата создания не в будущем
  if created_date > current_date:
    return "Ошибка: дата создания не может быть в будущем"
   
  # Проверяем, что дедлайн не раньше даты создания
  if issue_date < created_date:
    return "Ошибка: дедлайн не может быть раньше даты создания"
   
  # Вычисляем оставшееся время
  time_left = issue_date - current_date
   
  if time_left.days < 0:
    return "Дедлайн просрочен!"
  elif time_left.days == 0:
    return "Дедлайн сегодня!"
  else:
    return f"До дедлайна осталось {time_left.days} дней"


# Начало программы


def main():
  
  # Инициализируем данные заметки
  note_data = data_init()
  note_data.append(status_init())
  note_data.append(title_init())
  
  # Проверяем дедлайн
  deadline_status = check_deadline(note_data[2], note_data[3])
  
  # Создаем словарь с данными заметки
  note = {
    'Ваше имя'               : note_data[0],
    'Заголовки заметки'      : note_data[5],
    'Описание заметки'       : note_data[1],
    'Статус заметки'         : note_data[4],
    'Дата создания заметки'  : note_data[2].strftime('%d-%m'),
    'Дата истечения заметки' : note_data[3].strftime('%d-%m')
  }
  
  # Добавляем статус дедлайна только если заметка не выполнена
  if note_data[4] != 'Выполнено':
    note['Статус дедлайна'] = deadline_status
  
  # Сначала показываем данные
  output(note)
  
  # Спрашиваем про смену статуса
  while True:
    check_status = input('\nХотите сменить статус? y/n >> ')
    print()
    
    if check_status.lower() == 'y':
      old_status = note_data[4]
      note_data[4] = status_init()
      
      # Проверяем, что статус не выполнен
      if old_status == 'Выполнено' and note_data[4] != 'Выполнено':
        deadline_status = check_deadline(note_data[2], note_data[3])
        note_data.append(deadline_status)
        note['Статус дедлайна'] = note_data[6]
      
      # Проверяем, что статус выполнен
      elif old_status != 'Выполнено' and note_data[4] == 'Выполнено':
        if 'Статус дедлайна' in note:
          del note['Статус дедлайна']
          if len(note_data) > 6:
            note_data.pop()

      note['Статус заметки'] = note_data[4]
      output(note)

    else:
      break


if __name__ == '__main__':
  main()