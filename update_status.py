def data_init(): # Запрос данных о заметке data

  username     = input('Имя пользователя >> ')
  content      = input('Описание заметки >> ')
  created_date = input('Дата создания заметки (дд-мм-гггг) >> ')
  issue_date   = input('Дата истечения заметки (дд-мм-гггг) >> ')
  
  return [username, content, created_date, issue_date]

def status_init(): # Запрос статуса заметки status
  
  status = input('Статус заметки >> ')
  
  return status

def title_init(): # Запрос заголовков titles

  titles = []     # Инициализация листа titles
  title = ' '     # Инициализация переменной title для дальнейшей работы с ней
  i = 0           # Инициализация переменной i для дальнейшей работы с ней

  # Пример реализации Enter-ом:
  
  while True:

    title = str(input(f'Название заголовка {i+1} - [Enter] продолжить >> '))
    
    # Проверка строки title на пустоту, если строка пустая принудительно завершаем цикл
    # Проверка строки на дубликаты в списке, если дубликат есть - не добавляем в список
    
    if title != '':
      if title.lower() not in (map(str.lower, titles)):
        titles.append(title)
        i += 1
      else:
        print('Обнаружен дубликат! Удаление...\n')
    else:
      break

  return titles

def output(note): # Красивый вывод данных в консоль с использованием .replace()
  
  print('\nВы ввели следующие данные:\n')
  
  for key, value in note.items():  
    print("{0}: {1}".format(key, value).replace('[','').replace(']','').replace('\'',''))
  print()

# Начало программы

def main():

  note_data = data_init()
  note_data.append(status_init())
  note_data.append(title_init())
  
  # Итого: [0:Имя, 1:Описание, 2:дата созд, 3:дата изм, 4:статус, 5:заголовки]
  
  # Создание словаря с данными пользователя
  
  note = {
    'Ваше имя'               : note_data[0],
    'Заголовки заметки'      : note_data[5],
    'Описание заметки'       : note_data[1],
    'Статус заметки'         : note_data[4],
    'Дата создания заметки'  : note_data[2][:5],
    'Дата истечения заметки' : note_data[3][:5]
  }

  output(note) # Вывод в консоль данных

  while True: # Замена статуса
    
    check_status = input('Хотите сменить статус? y/n >> ')
    print()
    
    if check_status.lower() == 'y':
      
      note_data[4] = status_init()                    # Повторный запрос статуса
      note.update({'Статус заметки' : note_data[4]})  # Обновление словаря
      output(note)                                    # Повторный вывод в консоль данных
      
    else:
      break

main()
