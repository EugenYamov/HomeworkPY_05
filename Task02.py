# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


def input_tokens(player):
    token = int(input(f'{player}, возьмите конфеты от 1 до 28: '))

    while token < 1 or token > 28:
        token = int(input(f'{player}, вы можете взять от 1 до 28 конфет. Попробуйте снова: '))

    return token

def game_message(player, count, player_tokens, total_tokens):
    print(
        f'{player} взял {count} конфет и теперь у него {player_tokens} конфет. Всего конфет осталось - {total_tokens}')

def pvp_gameplay():

    player1 = input('Игрок №1, введите имя: ')
    player2 = input('Игрок №2, введите имя: ')
    total_tokens = int(input('Введите общее колличество конфет: '))

    player1_tokens = 0
    player2_tokens = 0
    first_move = randint(0, 2)

    if first_move:
        print(f'Ход {player1}')
    else:
        print(f'Ход {player2}')

    while total_tokens > 28:
        if first_move:
            count = input_tokens(player1)
            player1_tokens += count
            total_tokens -= count
            first_move = False
            game_message(player1, count, player1_tokens, total_tokens)
        else:
            count = input_tokens(player2)
            player2_tokens += count
            total_tokens -= count
            first_move = True
            game_message(player2, count, player2_tokens, total_tokens)

    if first_move:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")

def pve_gameplay():
    player = input('Введите имя: ')
    total_tokens = int(input('Введите общее колличество конфет: '))
    first_bot_move = total_tokens
    player_tokens = 0
    bot_tokens = 0
    first_move = randint(0, 2)

    if first_move:
        print(f'Ход {player}')
    else:
        print(f'Ход компьютера')

    while total_tokens > 28:
        if first_move:
            count = input_tokens(player)
            player_tokens += count
            total_tokens -= count
            first_move = False
            game_message(player, count, player_tokens, total_tokens)
        else:
            if total_tokens == first_bot_move or total_tokens > 56 or total_tokens == 28:
                count = 28
            elif total_tokens == 56:
                count = 27
            elif total_tokens < 56:
                count = total_tokens - 29

            bot_tokens += count
            total_tokens -= count
            first_move = True
            game_message("Компьютер", count, bot_tokens, total_tokens)

    if first_move:
        print(f"Выиграл {player}")
    else:
        print(f"Выиграл Компьютер")


gameplay_choice = int(input("Добро пожаловать! Если вы хотите сыграть с другом нажмите '1', если с компьютером, нажмите '2' "))
if gameplay_choice == 1:
    pvp_gameplay()
if gameplay_choice == 2:
    pve_gameplay()