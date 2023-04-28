import logging
from my_exceptions import AboveZeroException
import argparse

# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

logging.basicConfig(filename='task_2_logger.log', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


class Rectangle:

    def __init__(self, length, width=None):
        self._length = length
        self._width = width or length

    def __repr__(self):
        return f'r = Rectangle({self._length}, {self._width})'

    def get_perimeter(self):
        return 2 * (self._length + self._width)

    def get_square(self):
        return self._length * self._width

    @property
    def get_length(self):
        return self._length

    @property
    def get_width(self):
        return self._width

    @get_length.setter
    def get_length(self, value):
        if value > 0:
            self._length = value
        else:
            logger.error(AboveZeroException(value))

    @get_width.setter
    def get_width(self, value):
        if value > 0:
            self._width = value
        else:
            logger.error(AboveZeroException(value))


def get_args(r: Rectangle):
    args = argparse.ArgumentParser(description='Получаем длину и ширину прямоугольника')
    args.add_argument('-l', '--length', type=int, default=r.get_length)
    args.add_argument('-w', '--width', type=int, default=r.get_width)
    args_res = args.parse_args()

    r.get_length = args_res.length
    r.get_width = args_res.width
    return r


if __name__ == '__main__':
    print(get_args(Rectangle(5, 8)))

