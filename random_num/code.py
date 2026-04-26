from random import *

def is_valid(number):
    if is_valid in range(1, 101):
        return True
    else:
        return False

def end_word(count_try):
    if count_try == 1:
        return 'ку'
    elif count_try in [2, 3, 4]:
        return 'ки'
    else:
        return 'ок'
    
mind_num = randint(1, 100)
request_num = 0

print('Добро пожаловать в числовую угадайку')
gameTrue = 'да'
while gameTrue == 'да':
    count_try = 0
    while True:
        count_try += 1
        if count_try == 1:
            print('Новая игра!')
        print(f'Попытка угадать №{count_try}')
        request_num = int(input())
        if is_valid:
            if request_num > mind_num:
                print('Слишком много, попробуйте еще раз')
            if request_num < mind_num:
                print('Слишком мало, попробуйте еще раз')
            if request_num == mind_num:
                print('Вы угадали, поздравляем!')
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?', end = ' ')
            continue

    print(f'Вы справились за {count_try} попыт{end_word(count_try)}!')
    print('Играем еще раз? (ДА | НЕТ)')
    gameTrue = input().lower()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    