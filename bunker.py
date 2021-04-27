#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os


bunker = {
       'room01':
            {
                'name': 'Комната 1',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'noway', 'e': 'room02', 's': 'room04', 'w': 'noway', 'u': 'noway', 'd': 'noway'}
            },
        'room02':
            {
                'name': 'Комната 2',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'noway', 'e': 'room03', 's': 'room05', 'w': 'room01', 'u': 'noway', 'd': 'noway'}
            },
        'room03':
            {
                'name': 'Комната 3',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'noway', 'e': 'noway', 's': 'room06', 'w': 'room02', 'u': 'noway', 'd': 'noway'}
            },
       'room04':
            {
                'name': 'Комната 4',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room01', 'e': 'room05', 's': 'room07', 'w': 'noway', 'u': 'noway', 'd': 'noway'}
            },
        'room05':
            {
                'name': 'Комната 5',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room02', 'e': 'room06', 's': 'room08', 'w': 'room04', 'u': 'noway', 'd': 'noway'}
            },
        'room06':
            {
                'name': 'Комната 6',
                'desc': 'Лифтовая комната.',
                'goto': {'n': 'room03', 'e': 'noway', 's': 'room09', 'w': 'room05', 'u': 'room15', 'd': 'noway'}
            },
        'room07':
            {
                'name': 'Комната 7',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room04', 'e': 'room08', 's': 'noway', 'w': 'noway', 'u': 'noway', 'd': 'noway'}
            },
        'room08':
            {
                'name': 'Комната 8',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room05', 'e': 'room09', 's': 'noway', 'w': 'room07', 'u': 'noway', 'd': 'noway'}
            },
        'room09':
            {
                'name': 'Комната 9',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room06', 'e': 'noway', 's': 'noway', 'w': 'room08', 'u': 'noway', 'd': 'noway'}
            },
       'room10':
            {
                'name': 'Комната 10',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'noway', 'e': 'room11', 's': 'room13', 'w': 'noway', 'u': 'noway', 'd': 'noway'}
            },
        'room11':
            {
                'name': 'Комната 11',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'noway', 'e': 'room12', 's': 'room14', 'w': 'room10', 'u': 'noway', 'd': 'noway'}
            },
        'room12':
            {
                'name': 'Комната 12',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'noway', 'e': 'noway', 's': 'room15', 'w': 'room11', 'u': 'noway', 'd': 'noway'}
            },
       'room13':
            {
                'name': 'Комната 13',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room10', 'e': 'room14', 's': 'room16', 'w': 'noway', 'u': 'noway', 'd': 'noway'}
            },
        'room14':
            {
                'name': 'Комната 14',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room11', 'e': 'room15', 's': 'room17', 'w': 'room13', 'u': 'noway', 'd': 'noway'}
            },
        'room15':
            {
                'name': 'Комната 15',
                'desc': 'Лифтовая комната.',
                'goto': {'n': 'room12', 'e': 'noway', 's': 'room18', 'w': 'room14', 'u': 'room24', 'd': 'room06'}
            },
        'room16':
            {
                'name': 'Комната 16',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room13', 'e': 'room17', 's': 'noway', 'w': 'noway', 'u': 'noway', 'd': 'noway'}
            },
        'room17':
            {
                'name': 'Комната 17',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room14', 'e': 'room18', 's': 'noway', 'w': 'room16', 'u': 'noway', 'd': 'noway'}
            },
        'room18':
            {
                'name': 'Комната 18',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room15', 'e': 'noway', 's': 'noway', 'w': 'room17', 'u': 'noway', 'd': 'noway'}
            },
       'room19':
            {
                'name': 'Комната 19',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'noway', 'e': 'room20', 's': 'room22', 'w': 'noway', 'u': 'noway', 'd': 'noway'}
            },
        'room20':
            {
                'name': 'Комната 20',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'noway', 'e': 'room21', 's': 'room23', 'w': 'room19', 'u': 'noway', 'd': 'noway'}
            },
        'room21':
            {
                'name': 'Комната 21',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'noway', 'e': 'noway', 's': 'room24', 'w': 'room20', 'u': 'noway', 'd': 'noway'}
            },
       'room22':
            {
                'name': 'Комната 22',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room19', 'e': 'room23', 's': 'room25', 'w': 'noway', 'u': 'noway', 'd': 'noway'}
            },
        'room23':
            {
                'name': 'Комната 23',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room20', 'e': 'room24', 's': 'room26', 'w': 'room22', 'u': 'noway', 'd': 'noway'}
            },
        'room24':
            {
                'name': 'Комната 24',
                'desc': 'Лифтовая комната.',
                'goto': {'n': 'room21', 'e': 'noway', 's': 'room27', 'w': 'room23', 'u': 'noway', 'd': 'room15'}
            },
        'room25':
            {
                'name': 'Комната 25',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room22', 'e': 'room26', 's': 'noway', 'w': 'noway', 'u': 'noway', 'd': 'noway'}
            },
        'room26':
            {
                'name': 'Комната 26',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room23', 'e': 'room27', 's': 'noway', 'w': 'room25', 'u': 'noway', 'd': 'noway'}
            },
        'room27':
            {
                'name': 'Комната 27',
                'desc': 'Пустое помещение с серыми стенами.',
                'goto': {'n': 'room24', 'e': 'noway', 's': 'noway', 'w': 'room26', 'u': 'noway', 'd': 'noway'}
            }
}

you_are_here = bunker['room01']
histeria = 0

# print(
# you_are_here.get('name'), "\n\n",
# bunker.get('room01').keys(),"\n\n",
# bunker.keys(),"\n\n",
# )

def gogogo():
    global you_are_here
    global histeria

    if histeria >= 2:
        print('Прекратите истерику! Успокаиваясь, вы пропускаете ход.')
        histeria -= 1
        return




    you_was_here = you_are_here.get('name')

    if you_are_here.get('goto')[cmd] != 'noway':
        you_are_here = bunker[you_are_here.get('goto')[cmd]]
        if cmd == 'u':
            moving = 'Вы поднялись на лифте из '
        elif cmd == 'd':
            moving = 'Вы спустились на лифте из '
        else:
            moving = 'Вы перешли из '
        print(moving + you_was_here.lower().replace('та','ты') + " в " + you_are_here.get('name').lower().replace('та','ту') + "...")

    else:
        if cmd == 'u':
            moving = 'Вы уже находитесь на самом верхнем этаже. '
            histeria +=1
        elif cmd == 'd':
            moving = 'Вы уже на самом нижнем этаже, ниже некуда.'
            histeria += 1
        else:
            moving = 'Вы безуспешно пытаетесь пробить лбом внешнюю стену.'
            histeria += 1
        print( moving )



def look():
    global you_are_here
    print('Вы находитесь в ' + you_are_here.get('name') + '.')
    print(you_are_here.get('desc'))




def map():
    print('''ПЛАН БУНКЕРА:
         Этаж -3            Этаж -2            Этаж -1
    ┌────┬────┬────┐  ┌────┬────┬────┐  ┌────┬────┬────┐    
    │ 01 │ 02 │ 03 │  │ 10 │ 11 │ 12 │  │ 19 │ 20 │ 21 │      N     
    ├────┼────┼────┤  ├────┼────┼────┤  ├────┼────┼────┤      │     
    │ 04 │ 05 │ 06 │  │ 13 │ 14 │ 15 │  │ 22 │ 23 │ 24 │   W ─┼─ E  
    ├────┼────┼────┤  ├────┼────┼────┤  ├────┼────┼────┤      │     
    │ 07 │ 08 │ 09 │  │ 16 │ 17 │ 18 │  │ 25 │ 26 │ 27 │      S     
    └────┴────┴────┘  └────┴────┴────┘  └────┴────┴────┘''')
    print('Вы сейчас здесь: ' + str(you_are_here.get('name')) +
    '. Уровень вашей истерики: ' + str(histeria) + '\n')




def take():
    pass

def clearscr():
    try:
        os.system('clear')
    except:
        os.system('cls')


def hlp():
    pass
    print('''
n - идти на север
e - идти на
s - идти на юг
w - идти на восток

u - подняться наверх
d - спуститься вниз

l - осмотреться
t - взять предмет

с - очистить экран
h - эта справка
q - покинуть игру
    ''')

def game_exit():
    sys.exit()




def gamestep():

    print('... Ходит игра ...')
    # тут должен рыскать монстр



def show_mainmenu():
    global you_are_here
    print('\n' +
    'Вы находитесь в подземном многоуровневом бункере в помещении ' +
    you_are_here.get('name').lower() + ',\n' +
    'попробуйте его обследовать, избежать опасностей и выбраться на поверхность.\n')



actions = {
    'n': gogogo,
    'e': gogogo,
    's': gogogo,
    'w': gogogo,
    'u': gogogo,
    'd': gogogo,

    'l': look,
    'm': map,

    't': take,
    'c': clearscr,
    'h': hlp,
    'q': game_exit
    }
# print(actions.keys())       # вывести ключи словаря
# print(actions.values())     # вывести значения словаря
# https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html


if __name__== '__main__':
    show_mainmenu()

    while True:
        cmd = input('[' + you_are_here.get('name') + '] Ваша команда? (h - help) > ')

        action = actions.get(cmd)   # .get() - метод словаря, возвращает значение ключа

        if action:
            action()

        else:
            print('\nНеизвестная команда.')
        gamestep()


