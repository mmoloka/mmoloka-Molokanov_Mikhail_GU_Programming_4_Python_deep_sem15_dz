class AboveZeroException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Вы ввели некорректное значение стороны прямоугольника: {self.value}, \
значение должно быть больше нуля.'

