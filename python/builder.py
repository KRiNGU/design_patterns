from abc import ABC, abstractmethod


class SmallHouse():
    wallsHeight = None
    roof = None
    foundation = None
    windowsNumber = None

    def __str__(self):
        return f'''This is small house with: 
    walls heigh = {self.wallsHeight},
    {self.roof} roof,
    {self.foundation} foundation,
    windows number = {self.windowsNumber}.'''


class LargeHouse():
    wallsHeight = None
    roof = None
    foundation = None
    windowsNumber = None
    pool = None

    def __str__(self):
        return f'''This is large house with: 
    walls heigh = {self.wallsHeight},
    {self.roof} roof,
    {self.foundation} foundation,
    windows number = {self.windowsNumber},
    {self.pool} pool.'''


class HouseBuilder(ABC):
    @abstractmethod
    def setWallsHeight(self, height: int):
        pass

    @abstractmethod
    def setRoof(self, type: str):
        pass

    @abstractmethod
    def setFoundation(self, type: str):
        pass

    @abstractmethod
    def setWindowsNumber(self, number: int):
        pass


class SmallHouseBuilder(HouseBuilder):
    house = SmallHouse()

    def setWallsHeight(self, height: int):
        self.house.wallsHeight = height
        return self

    def setRoof(self, type: str):
        self.house.roof = type
        return self

    def setFoundation(self, type: str):
        self.house.foundation = type
        return self

    def setWindowsNumber(self, number: int):
        self.house.windowsNumber = number
        return self

    def getHouse(self):
        return self.house


class LargeHouseBuilder(HouseBuilder):
    house = LargeHouse()

    def setWallsHeight(self, height: int):
        self.house.wallsHeight = height
        return self

    def setRoof(self, type: str):
        self.house.roof = type
        return self

    def setFoundation(self, type: str):
        self.house.foundation = type
        return self

    def setWindowsNumber(self, number: int):
        self.house.windowsNumber = number
        return self

    def setPool(self, type: str):
        self.house.pool = type
        return self

    def getHouse(self):
        return self.house


smallHouseBuilder: HouseBuilder = SmallHouseBuilder()
smallHouse: SmallHouse = smallHouseBuilder.setRoof('base').setWallsHeight(
    2).setWindowsNumber(4).setFoundation('base').getHouse()
largeHouseBuilder: HouseBuilder = LargeHouseBuilder()
largeHouse: LargeHouse = largeHouseBuilder.setRoof('premium').setWallsHeight(
    4).setWindowsNumber(14).setFoundation('premium').setPool('small').getHouse()
print(smallHouse.__str__())
print('----------------------------------------------------------------')
print(largeHouse.__str__())
