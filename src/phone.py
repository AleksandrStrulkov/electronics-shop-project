from src.item import Item


class Phone(Item):
    """Класс, содержащий информацию о телефоне"""
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self) -> str:
        """Функция, возвращающая строку с информацией для разработчика"""
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self) -> str:
        """Функция, возвращающая строку с информацией для пользователя"""
        return f'{self.name}'

    @property
    def number_of_sim(self) -> int:
        """""Возвращает количество сим карт в телефоне. К атрибуту можно обращаться без ()."""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int) -> None:
        """Метод добавляет исключение к полю number_of_sim"""
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        else:
            self.__number_of_sim = number_of_sim

    def __add__(self, other: Item) -> int:
        """Метод позволяет складывать экземпляры класса Item и Phone"""
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только экземпляры класса Item и Phone')
        return self.quantity + other.quantity

    def __radd__(self, other):
        """Метод позволяет выполнить отраженное сложение экземпляров класса Item и Phone"""
        return self + other

