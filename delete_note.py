import datetime


# Функция для нормализации даты


def normalize_date(date_str):
  # Заменяем точки и слеши на дефисы
  return date_str.replace('.', '-').replace('/', '-')


# Функция для запроса данных о заметке data


def data_init():

  username         = input('\n👤 • Имя пользователя >> ')
  content          = input('📝 • Описание заметки >> ')
  
  # Нормализуем введенную дату, заменяя разделители на дефисы
  created_date_str = normalize_date(input('📅 • Дата создания заметки >> '))
  issue_date_str   = normalize_date(input('📅 • Дата истечения заметки >> '))
  
  # Преобразуем строки в объекты datetime
  created_date     = datetime.datetime.strptime(created_date_str, '%d-%m-%Y')
  issue_date       = datetime.datetime.strptime(issue_date_str, '%d-%m-%Y')
  
  return [username, content, created_date, issue_date]


# Функция для запроса статуса заметки status


def status_init():
  
  # Словарь для хранения соответствия между цифровым выбором пользователя
  # и текстовым представлением статуса
  
  statuses = {
    '1': '⏳ • В процессе',  # Статус для активных заметок
    '2': '✔️  • Выполнено',   # Статус для завершенных заметок
    '3': '❌ • Отложено'     # Статус для отложенных заметок
  }

  while True:
    print('\n🔘 • Статус заметки:\n1 - ⏳ • В процессе\n2 - ✔️  • Выполнено\n3 - ❌ • Отложено')
    
    choice = input('🔘 • Выберите пункт 1-3 >> ')
    
    # Проверка есть ли выбор в словаре статусов
    if choice in statuses:
      return statuses[choice]  # Возврат текстового значения статуса
      
    # Сообщение об ошибке при неверном выборе
    print("❌ Некорректный выбор!")


# Функция для запроса заголовков titles


def title_init():

  titles, title, count = [], ' ', 0
  
  while True:

    title = str(input(f'\n🔖 • Название заголовка {count+1} - [Enter] продолжить >> '))
    
    # Проверка строки title на пустоту, если строка пустая принудительно завершаем цикл
    # Проверка строки на дубликаты в списке, если дубликат есть - не добавляем в список
    
    if title != '':
      if title.lower() not in (map(str.lower, titles)):
        titles.append(title)
        count += 1
      else:
        print("⚠️ • Такой заголовок уже существует!")
    else:
      break

  return titles


# Функция для вывода данных в консоль


def output(notes):
  for i, note in enumerate(notes, 1):
    print(f"\n" + "=" * 50 + f"\n📝 Заметка #{i}:\n" + "=" * 50 + "\n")
    
    for key, value in note.items():
      # Используем f-строку и преобразуем список в строку через join если это список
      value_str = ', '.join(value) if isinstance(value, list) else value
      print(f'{key}: {value_str}')


# Функция для проверки дедлайна

 
def check_deadline(created_date, issue_date):
  current_date = datetime.datetime.now()
   
  # Проверяем, что дата создания не в будущем
  if created_date > current_date:
    return "⚠️ • Ошибка: дата создания не может быть в будущем"
   
  # Проверяем, что дедлайн не раньше даты создания
  if issue_date < created_date:
    return "⚠️ • Ошибка: дедлайн не может быть раньше даты создания"
   
  # Вычисляем оставшееся время
  time_left = issue_date - current_date
   
  if time_left.days < 0:
    return "⚠️ • Дедлайн просрочен!"
  elif time_left.days == 0:
    return "⚠️ • Дедлайн сегодня!"
  else:
    return f"⏰ • До дедлайна осталось {time_left.days} дней"


# Функция создания новой заметки


def create_note():
  # Инициализируем данные заметки
  note_data = data_init()
  note_data.append(status_init())
  note_data.append(title_init())
  
  # Проверяем дедлайн
  deadline_status = check_deadline(note_data[2], note_data[3])
  
  # Создаем словарь с данными заметки
  note = {
    '👤 • Ваше имя'               : note_data[0],
    '📌 • Заголовки заметки'      : note_data[5],
    '📝 • Описание заметки'       : note_data[1],
    '🔘 • Статус заметки'         : note_data[4],
    '📅 • Дата создания заметки'  : note_data[2].strftime('%d-%m'),
    '📅 • Дата истечения заметки' : note_data[3].strftime('%d-%m')
  }
  
  # Добавляем статус дедлайна только если заметка не выполнена
  if note_data[4] != '✔️  • Выполнено':
    note['🔴 • Статус дедлайна'] = deadline_status
    
  return note, note_data


# Функция удаления заметки


def delete_note(notes, note_data_list):
  if not notes:
    print("\n❌ Нет заметок для удаления!")
    return False
    
  print("\nСписок заметок:")
  for i, note in enumerate(notes, 1):
    print(f"{i}. {note['📌 • Заголовки заметки']}")
    
  while True:
    try:
      note_num = int(input('\n🗑️  • Введите номер заметки для удаления >> ')) - 1
      if 0 <= note_num < len(notes):
        del notes[note_num]
        del note_data_list[note_num]
        print("\n✅ • Заметка успешно удалена!")
        return True
      print("❌ Некорректный номер заметки!")
    except ValueError:
      print("❌ Введите число!")


# Начало программы


def main():
  notes = []           # Список для хранения всех заметок
  note_data_list = []  # Список для хранения данных всех заметок
  
  while True:
    # Создаем новую заметку
    note, note_data = create_note()
    notes.append(note)
    note_data_list.append(note_data)
    
    # Показываем все заметки
    output(notes)
    
    # Спрашиваем про создание новой заметки
    while True:
      create_new = input('\nХотите создать новую заметку? y/n >> ')
      if create_new.lower() in ['y', 'n']:
        break
      print("❌ Некорректный ввод! Введите 'y' или 'n'")
        
    if create_new.lower() == 'n':
      while True:
        print("\n1 - Изменить статус заметки")
        print("2 - Удалить заметку")
        print("3 - Выйти")
        choice = input("\nВыберите действие >> ")
        
        if choice == "1":
          # Если хотим изменить статус
          while True:
            change_status = input('\nХотите изменить статус какой-либо заметки? y/n >> ')
            if change_status.lower() == 'y':
              # Показываем список заметок с номерами
              print("\nСписок заметок:")
              for i, note in enumerate(notes, 1):
                print(f"{i}. {note['📌 • Заголовки заметки']}")
                
              # Запрашиваем номер заметки
              while True:
                try:
                  note_num = int(input('\nВведите номер заметки для изменения статуса >> ')) - 1
                  if 0 <= note_num < len(notes):
                    break
                  print("❌ Некорректный номер заметки!")
                except ValueError:
                  print("❌ Введите число!")
              
              # Меняем статус выбранной заметки
              old_status = note_data_list[note_num][4]
              note_data_list[note_num][4] = status_init()
              
              # Обновляем статус в словаре заметки
              if old_status == '✔️  • Выполнено' and note_data_list[note_num][4] != '✔️  • Выполнено':
                deadline_status = check_deadline(note_data_list[note_num][2], note_data_list[note_num][3])
                notes[note_num]['🔴 • Статус дедлайна'] = deadline_status
              elif old_status != '✔️  • Выполнено' and note_data_list[note_num][4] == '✔️  • Выполнено':
                if '🔴 • Статус дедлайна' in notes[note_num]:
                  del notes[note_num]['🔴 • Статус дедлайна']
              
              notes[note_num]['🔘 • Статус заметки'] = note_data_list[note_num][4]
              output(notes)
            elif change_status.lower() == 'n':
              break
            else:
              print("❌ Некорректный ввод! Введите 'y' или 'n'")
              
        elif choice == "2":
          # Если хотим удалить заметку
          if delete_note(notes, note_data_list):
            output(notes)
            
        elif choice == "3":
          break
            
        else:
          print("❌ Некорректный выбор!")
      break


if __name__ == '__main__':
  main()