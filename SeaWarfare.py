import random
print("*" * 10, " Игра морской бой! ", "*" * 10)
field = [[' ', '1', '2', '3', '4', '5', '6'],
        ['1', 'O', 'O', 'O', 'O', 'O','O'],
        ['2', 'O', 'O', 'O', 'O', 'O','O'],
        ['3', 'O', 'O', 'O', 'O', 'O','O'],
        ['4', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['5', 'O', 'O', 'O', 'O', 'O','O'],
        ['6', 'O', 'O', 'O', 'O', 'O','O']]

ship = [[4, 2], [4,3], [4,4]]
deck = 3
ship1 = [[3,2], [3,3]]
deck = 2
ship2 = [5,2]
deck = 1
ship3 = [5,5]
deck = 1
ship4 = [6,2]
deck = 1
ship5 = [6,6]
deck = 1

def random_ship():
  global ship
  x = random.randint(0, 3)
  y = random.randint(0, 3)
  d = random.randint(0, 1)
  if d == 0:
    ship = [[x, y], [x, y+1], [x, y+2], [x, y+3]]
  else:
    ship = [[x, y], [x+1, y], [x+2, y], [x+3, y]]

def show_field():
  for row in field:
        print('|'.join(row))
        print('-'*14)

def where_shoot():
  global deck
  print('Укажите столбец:')
  stolbec = int(input())
  print('Укажите ряд:')
  ryad = int(input())

  if [ryad, stolbec] in ship:
    if field[ryad][stolbec] != '#':
      print('Попал!')
      field[ryad][stolbec] = '#'
      deck = deck - 1
      if deck == 0:
        print('Вы победили!!')
  else:
    print('Мимо...')
    field[ryad][stolbec] = 'X'

show_field()
random_ship()
for i in range(14):
  where_shoot()
  show_field()
