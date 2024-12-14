def data_init(): # Инициализация и присваивание значений переменным

  username     = input('Имя пользователя >> ')
  title        = input('Заголовок заметки >> ')
  content      = input('Описание заметки >> ')
  status       = input('Статус заметки >> ')
  created_date = input('Дата создания заметки (дд-мм-гггг) >> ')
  issue_date   = input('Дата истечения заметки (дд-мм-гггг) >> ')
  
  return username, title, content, status, created_date, issue_date

def main(): # Начало программы

  username, title, content, status, created_date, issue_date = data_init()
  
  print('\nВы ввели следующие данные:')
  print(f'Ваше имя: {username}')
  print(f'Заголовок заметки: {title}')
  print(f'Описание заметки: {content}')
  print(f'Статус заметки: {status}')
  print(f'Дата создания заметки: {created_date}')
  print(f'Дата истечения заметки: {issue_date}')

main()