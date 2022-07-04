from abc import ABC, abstractmethod


class House(ABC):
    @abstractmethod
    def getClassName(self) -> str:
        pass


class SmallHouse(House):
    def getClassName(self) -> str:
        return 'SmallHouse'


class MediumHouse(House):
    def getClassName(self) -> str:
        return 'MediumHouse'


class LargeHouse(House):
    def getClassName(self) -> str:
        return 'LargeHouse'


class HouseFactory(ABC):
    @abstractmethod
    def factoryMethod(self):
        pass


class SmallHouseFactory(HouseFactory):
    def factoryMethod(self):
        return SmallHouse()


class MediumHouseFactory(HouseFactory):
    def factoryMethod(self):
        return MediumHouse()


class LargeHouseFactory(HouseFactory):
    def factoryMethod(self):
        return LargeHouse()


factory: HouseFactory = SmallHouseFactory()
house1 = factory.factoryMethod()
factory: HouseFactory = MediumHouseFactory()
house2 = factory.factoryMethod()
factory: HouseFactory = LargeHouseFactory()
house3 = factory.factoryMethod()
print(house1.getClassName())
print(house2.getClassName())
print(house3.getClassName())
