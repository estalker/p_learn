import os
import time


for dirpath, subdirs, files in os.walk("."):
    for file in files:
        pathParts = dirpath.split("\\")
        pathParts.append(file)
        filepath = os.path.abspath(os.path.join(*pathParts))
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и использование модуля time для корректного отображения времени.
#
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
#
#     Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
#     Примените os.path.join для формирования полного пути к файлам.
#     Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
#     Используйте os.path.getsize для получения размера файла.
#     Используйте os.path.dirname для получения родительской директории файла.