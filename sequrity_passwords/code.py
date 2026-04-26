from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def valid(x):
    while not x.isdigit():
        if not x.isdigit():
            print('Некорректное значение! Введи еще раз:')
            x = input()

    return int(x)

def data(data_pass):
    data_list = []
    data_list.append(digits)
    data_list.append(lowercase_letters)
    data_list.append(uppercase_letters)
    data_list.append(punctuation)
    chars = ''
    for i in data_pass:
        chars += data_list[int(i)-1]
    return chars

def exception(chars):
    ex = 'il1Lo0O'
    for i in ex:
        chars = chars.replace(i, '')
    return chars

def generate_pass(len_pass, chars):
    pasw = ''
    for i in range(len_pass):
        pasw += choice(chars)
    return pasw

print('Привет! Это программа генератор паролей. \nСколько паролей нужно создать?')
count_pass = valid(input())

print('Отлично! Теперь мне нужно знать длину одного пароля для генерации:')
len_pass = valid(input())

print('Замечательно! Теперь укажи какие наборы символов использовать? Вот список для выбора (выбери номера): \n'
        '1 - digits = 0123456789\n'
        '2 - lowercase_letters = abcdefghijklmnopqrstuvwxyz\n'
        '3 - uppercase_letters = ABCDEFGHIJKLMNOPQRSTUVWXYZ\n'
        '4 - punctuation = !#$%&*+-=?@^_', sep = ' ')
data_pass = input().split()

chars = data(data_pass)

print('Исключать ли неоднозначные символы - "il1Lo0O" ? (yes/no)')

if input() == 'yes':
    chars = exception(chars)

print('Хорошо! Вот список сгенерированных случайных паролей:')

for _ in range(count_pass):
    print(generate_pass(len_pass, chars))
    
print('На этом все! Хорошего дня!')