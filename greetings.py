username     = 'Илья'
title        = 'Д/З'
content      = 'Сделать Д/З'
status       = 'В процессе'
created_date = '14-12-2024'
issue_date   = '14-12-2024'

def main(): # Начало программы
  
  print('\nВы ввели следующие данные:')
  print(f'Ваше имя: {username}')
  print(f'Заголовки заметки: {title}')
  print(f'Описание заметки: {content}')
  print(f'Статус заметки: {status}')
  print(f'Дата создания заметки: {created_date[0:5]}')
  print(f'Дата истечения заметки: {issue_date[0:5]}')

main()
