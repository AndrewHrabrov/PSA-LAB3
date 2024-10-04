import os

types_of_files = {'png': '89504E470D0A1A0A',
                  'pdf': '255044462D',
                  'otf': '4F54544F',
                  'jpg': 'FFD8FF',
                  'rar': '526172211A07',
                  '7z': '377ABCAF271C',
                  'zip': '504B',
                  'UTF-16LE': 'FFFE',
                  'UTF-16BE': 'FEFF',
                  }
val = "".join(list(types_of_files.values()))

folder_path = 'C:/Users/DrShtoppor/Desktop/sem3/PSA/PSA-LAB3/files/lab3_files/BinaryFiles/' # Исходная папка
for i in range(1, 8):
    filename = f"file00{i}"      # Перебор всех файлов
    file_path = os.path.join(folder_path, filename)  # Объединение строки с путем к папке и строки с названием файла
    with open(file_path, 'r+b') as f:
        read_b = f.read()
        hex_string = read_b.hex().upper()

    for file_type, signature in types_of_files.items():   # Перебор пар расширение-сигнатура словаря
        if hex_string.startswith(signature):  # Если вначале 0x строке есть сигнатура из словаря
            new_filename = filename + '.' + file_type
            new_filepath = os.path.join(folder_path, new_filename) # Объединение строки с путем к папке и строки с новым названием файла
            os.rename(file_path, new_filepath) # Переименовывание файла
            break



