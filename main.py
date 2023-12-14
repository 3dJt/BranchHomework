from quiz import start_game
import time

print('Добро пожаловать в викторину!')
time.sleep(2)
start_q = input('Желаете начать игру?: ')

if start_q == 'Да':
    print('Игра начинается.. Подождите.')
    time.sleep(2.5)
    start_game()

elif start_q == 'Нет':
    print('До встречи!')

else:
    print('?#42:F/(@), нет такой команды = (')