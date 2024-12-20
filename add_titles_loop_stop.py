def data_init(): # Запрос данных о заметке data

  username     = input('Имя пользователя >> ')
  content      = input('Описание заметки >> ')
  status       = input('Статус заметки >> ')
  created_date = input('Дата создания заметки (дд-мм-гггг) >> ')
  issue_date   = input('Дата истечения заметки (дд-мм-гггг) >> ')
  
  return [username, content, status, created_date, issue_date]

def title_init(): # Запрос заголовков titles

  titles = []     # Инициализация листа titles
  title = ' '     # Инициализация переменной title для дальнейшей работы с ней
  i = 0           # Инициализация переменной i для дальнейшей работы с ней

  # Пример реализации цикла стоп-словом
  
  while True:

    title = str(input(f'Название заголовка {i+1} - Введите "СТОП" продолжить >> '))
    
    # Проверка строки title на пустоту, если строка пустая принудительно завершаем цикл
    # Проверка строки на дубликаты в списке, если дубликат есть - не добавляем в список
    
    if title.lower != 'стоп':
      if title.lower() not in (map(str.lower, titles)):
        titles.append(title)
        i += 1
      else:
        print('Обнаружен дубликат! Удаление...\n')
    else:
      break

  return titles

# Начало программы

def main():

  note_data = data_init()
  note_data.append(title_init())
  
  # Создание словаря с данными пользователя
  
  note = {
    'Ваше имя'               : note_data[0],
    'Заголовки заметки'      : note_data[5],
    'Описание заметки'       : note_data[1],
    'Статус заметки'         : note_data[2],
    'Дата создания заметки'  : note_data[3][:5],
    'Дата истечения заметки' : note_data[4][:5]
  }
  
  print('\nВы ввели следующие данные:')

  for key, value in note.items():
    
    # Красивый вывод данных в консоль с использованием .replace()
    
    print("{0}: {1}".format(key, value).replace('[','').replace(']','').replace('\'',''))

main()
