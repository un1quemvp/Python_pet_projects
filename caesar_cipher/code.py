
al_ru = ''.join([chr(i) for i in range(1072, 1104)])
al_en = ''.join([chr(i) for i in range(97,123)])

dir_way = input('Введите назначение (шифрование - cipher или дешифрование - decipher)')
lang_cipher = input('Введите язык пользования (русский - ru или английский - en)')
rot = int(input('Введите шаг сдвига (для шифрования - вправо | для дешифрования - влево)'))
start_str = input('Введите строку:')

result_cipher = ''

if 'de' in dir_way or dir_way == 'decipher':
    for i in start_str:
        if i.isalpha():
            if lang_cipher == 'ru':
                result_cipher += al_ru[(al_ru.index(i.lower()) - (rot%32)) % 32]
            elif lang_cipher == 'en':
                result_cipher += al_en[(al_en.index(i.lower()) - (rot%26)) % 26]
        else:
            result_cipher += i
else:
    for i in start_str:
        if i.isalpha():
            if lang_cipher == 'ru':
                result_cipher += al_ru[(al_ru.index(i.lower()) + (rot%32)) % 32]
            elif lang_cipher == 'en':
                result_cipher += al_en[(al_en.index(i.lower()) + (rot%26)) % 26]
        else:
            result_cipher += i

print(f'Строка {start_str} была преобразована со сдвигом {rot}. Результ:', result_cipher)