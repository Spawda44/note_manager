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

  note = data_init()
  note.append(title_init())
  
  print('\nВы ввели следующие данные:')
  print(f'Ваше имя: {note[0]}')
  print(f'Заголовки заметки: {' '.join(map(str, *note[5]))}') # Распаковка и преобразование подлиста в строку
  print(f'Описание заметки: {note[1]}')
  print(f'Статус заметки: {note[2]}')
  print(f'Дата создания заметки: {note[3]}')
  print(f'Дата истечения заметки: {note[4]}')

main()
