'''2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''


from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, base_param):
        self.base_param = base_param

    @property
    def consumption(self):
        return f'Сумма использованной ткани равна: {self.base_param / 6.5 + 0.5 + 2 * self.base_param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Smth vary abstract'


class Coat(Clothes):
    @property
    def consumption(self):
        return f'Для изготовления пальто необходимо : {self.base_param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Абстрактный метод для пальто'


class Costume(Clothes):

    def consumption(self):
        return f'Для изготовления костюма необходимо : {2 * self.base_param + 0.3 :.2f} ткани'

    def abstract(self):
        return 'Абстрактный метод для костюмов'


coat = Coat(400)
costume = Costume(55)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())
