def data_init(): # Запрос данных о заметке data

  username     = input('Имя пользователя >> ')
  content      = input('Описание заметки >> ')
  status       = input('Статус заметки >> ')
  created_date = input('Дата создания заметки (дд-мм-гггг) >> ')
  issue_date   = input('Дата истечения заметки (дд-мм-гггг) >> ')
  
  return [username, content, status, created_date, issue_date]

def title_init(): # Запрос заголовков titles

  titles = []

  for i in range(3):
    title = input(f'Название заголовка {i+1} >> ')
    titles.append(title)

  return [titles]

# Начало программы

def main():

  note_data = data_init()
  note_data.append(title_init())
  
  note = {
    'Ваше имя' : note_data[0],
    'Заголовки заметки' : note_data[5],
    'Описание заметки' : note_data[1],
    'Статус заметки' : note_data[2],
    'Дата создания заметки' : note_data[3],
    'Дата истечения заметки' : note_data[4]
  }
  
  print('\nВы ввели следующие данные:')

  for key, value in note.items():
    print("{0}: {1}".format(key, value)) # Красивый вывод данных в консоль

main()
