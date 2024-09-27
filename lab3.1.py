#task 1.1
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('А ещё хорошо бы уметь всем на зависть чётко'
            ' и наглядно писать буквы и цифры.')

#task 1.2
with open('test.txt', 'a', encoding='utf-8') as f:
    f.write('\nАэрофотосъёмка ландшафта уже выявила '
            'земли богачей и процветающих крестьян.')

# task 1.3
with open('test.txt', 'r', encoding='utf-8') as f:
    read_test = f.read()
    print(read_test)