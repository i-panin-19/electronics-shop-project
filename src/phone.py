from src.item import Item

class Phone(Item):
    """
    Phone, дочерний класс Item. Появляется атрибут number_of_sim (кол-во сим карт)
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        '''
        геттер атрибута number_of_sim
        '''
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        '''
        сеттер атрибута number_of_sim
        '''
        # проверка количества сим карт
        if number_of_sim <= 0:
            print('ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = number_of_sim
