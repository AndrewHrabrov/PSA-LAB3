import os
import chardet

folder_path = 'C:/Users/DrShtoppor/Desktop/sem3/PSA/PSA-LAB3/files/lab3_files/WindowsTxtFiles/'

for i in range(1, 5):  # Перебор всех файлов в каталоге
    filename = f"text-{i}.txt" # Формирование названия файла
    file_path = os.path.join(folder_path, filename) # Формирование пути к файлу
    with open(file_path, 'rb') as f:
        read_f = f.read()
        print((chardet.detect(read_f).get('encoding')), # Определение кодировки файла
              read_f.decode((chardet.detect(read_f).get('encoding')))) # Вывод содержимого файла
