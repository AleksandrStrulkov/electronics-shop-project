import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, file_csv):
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        try:
            with open(file_csv, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls.all.append(cls(row["name"], row["price"], row["quantity"]))

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

        except KeyError:
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(string_num):
        """Статический метод, возвращающий число из числа-строки"""
        if string_num.isdigit():
            return int(string_num)
        return float(string_num) // 1


class InstantiateCSVError(Exception):
    """Класс исключения при поврежденном файле"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return self.message



