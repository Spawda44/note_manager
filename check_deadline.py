import datetime

def data_init(): # Запрос данных о заметке data

  username     = input('\nИмя пользователя >> ')
  content      = input('Описание заметки >> ')
  created_date = datetime.datetime.strptime(input('Дата создания заметки (дд-мм-гггг) >> '), '%d-%m-%Y')
  issue_date   = datetime.datetime.strptime(input('Дата истечения заметки (дд-мм-гггг) >> '), '%d-%m-%Y')
  
  return [username, content, created_date, issue_date]

def status_init(): # Запрос статуса заметки status
  while True:
    print('\nСтатус заметки:\n1 - В процессе\n2 - Выполнено\n3 - Отложено')
  
    status = input('Выберите пункт 1-3 >> ')
  
    if status == '1':
      status = 'В процессе'
      break
    elif status == '2':
      status = 'Выполнено'
      break
    elif status == '3':
      status = 'Отложено'
      break
    else:
      print('\nТакого статуса не существует\n')
  
  return status

def title_init(): # Запрос заголовков titles

  titles = []     # Инициализация листа titles
  title  = ' '    # Инициализация переменной title для дальнейшей работы с ней
  i      = 0      # Инициализация переменной i для дальнейшей работы с ней

  # Пример реализации Enter-ом:
  
  while True:

    title = str(input(f'\nНазвание заголовка {i+1} - [Enter] продолжить >> '))
    
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

def output(note): # Красивый вывод данных в консоль с использованием .replace()
  
  print('\nВы ввели следующие данные:\n')
  
  for key, value in note.items():
    
    # Используем f-строку и преобразуем список в строку через join если это список
    value_str = ', '.join(value) if isinstance(value, list) else value
    print(f'{key}: {value_str}')
  
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
  # Инициализация данных заметки
  note_data = data_init()
  note_data.append(status_init())
  note_data.append(title_init())
  
  # Проверка статуса дедлайна
  deadline_status = check_deadline(note_data[2], note_data[3])
  
  # Формирование словаря с данными заметки
  note = {
    'Ваше имя'               : note_data[0],
    'Заголовки заметки'      : note_data[5], 
    'Описание заметки'       : note_data[1],
    'Статус заметки'         : note_data[4],
    'Дата создания заметки'  : note_data[2].strftime('%d-%m'),
    'Дата истечения заметки' : note_data[3].strftime('%d-%m'),
    'Статус дедлайна'        : deadline_status
  }

  # Вывод данных заметки
  output(note)

  # Цикл изменения статуса
  while True:
    check_status = input('\nХотите сменить статус? y/n >> ')
    print()
    
    if check_status.lower() == 'y':
      # Обновление статуса
      note_data[4] = status_init()
      note['Статус заметки'] = note_data[4]
      output(note)
    else:
      break
    
if __name__ == '__main__':
  main()