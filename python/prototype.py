from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class House(Prototype):
    walls = None
    roof = None

    def __init__(self, walls: int, roof: str):
        self.walls = walls
        self.roof = roof

    def clone(self):
        return House(self.walls, self.roof)

    def __str__(self):
        return f'''This is house with:
    {self.walls} walls and {self.roof} roof.'''

    def __eq__(self, other):
        return self.walls == other.walls and self.roof == other.roof


house: House = House(4, 'base')
clonedHouse: House = house.clone()

print(house)
print(clonedHouse)
print('Is this houses equal? \n', house == clonedHouse)
