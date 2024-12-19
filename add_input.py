def data_init(): # Инициализация и присваивание значений переменным

  username     = input('Имя пользователя >> ')
  content      = input('Описание заметки >> ')
  status       = input('Статус заметки >> ')
  created_date = input('Дата создания заметки (дд-мм) >> ')
  issue_date   = input('Дата истечения заметки (дд-мм) >> ')
  
  return username, content, status, created_date, issue_date

def title_init(): # Инициализация и присваивание значений переменной titles
  
  title1 = input('Введите 1-й заголовок >> ')
  title2 = input('Введите 2-й заголовок >> ')
  title3 = input('Введите 3-й заголовок >> ')
  titles = [title1, title2, title3]
  
  return titles

# Начало программы

def main():

  username, content, status, created_date, issue_date = data_init()
  titles = title_init()
  
  print('\nВы ввели следующие данные:')
  print(f'Ваше имя: {username}')
  print('Заголовки заметки:', *titles)
  print(f'Описание заметки: {content}')
  print(f'Статус заметки: {status}')
  print(f'Дата создания заметки: {created_date}')
  print(f'Дата истечения заметки: {issue_date}')

main()
