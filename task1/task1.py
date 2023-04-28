import os
from collections import namedtuple
import logging
import argparse


# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

def get_path():
    path = argparse.ArgumentParser(description='Получаем путь до директории')
    path.add_argument('-p', '--path', default=os.getcwd())
    path_res = path.parse_args()
    return directory_contents(path_res.path)


def directory_contents(path: str):
    logging.basicConfig(filename='task_1_logger.log', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)
    Content = namedtuple('Content', ['name', 'flag', 'catalog'])
    dir_list = os.listdir(path)
    for obj in dir_list:
        if os.path.isfile(f'{path}\\{obj}'):
            content = Content(obj.split('.')[0], obj.split('.')[1], path.split('\\').pop())
            logger.info(content)
        elif os.path.isdir(f'{path}\\{obj}'):
            content = Content(obj, 'directory', path.split('\\').pop())
            logger.info(content)


if __name__ == '__main__':
    get_path()
# python task1/task1.py -p C:\Users\№1\Desktop\sem15_dz\task1\test_dir
