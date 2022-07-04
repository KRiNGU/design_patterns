from abc import ABC, abstractmethod


class Bed(ABC):
    @abstractmethod
    def get_class_name(self) -> str:
        pass


class Chair(ABC):
    @abstractmethod
    def get_class_name(self) -> str:
        pass


class VictorianBed(Bed):
    def get_class_name(self) -> str:
        return('Victorian Bed')


class ModernBed(Bed):
    def get_class_name(self) -> str:
        return('Modern Bed')


class VictorianChair(Chair):
    def get_class_name(self) -> str:
        return('Victorian Chair')


class ModernChair(Chair):
    def get_class_name(self) -> str:
        return('Modern Chair')


class FurnitureFactory(ABC):
    @abstractmethod
    def get_bed(self) -> Bed:
        pass

    @abstractmethod
    def get_chair(self) -> Chair:
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    def get_bed(self) -> VictorianBed:
        return VictorianBed()

    def get_chair(self) -> VictorianChair:
        return VictorianChair()


class ModernFurnitureFactory(FurnitureFactory):
    def get_bed(self) -> ModernBed:
        return ModernBed()

    def get_chair(self) -> ModernChair:
        return ModernChair()


vFactory: FurnitureFactory = VictorianFurnitureFactory()
vChair: Chair = vFactory.get_chair()
vBed: Bed = vFactory.get_bed()
mFactory: FurnitureFactory = ModernFurnitureFactory()
mChair: Chair = mFactory.get_chair()
mBed: Bed = mFactory.get_bed()
print('Victorian chair: ' + vChair.get_class_name())
print('Modern chair: ' + mChair.get_class_name())
print('Victorian bed: ' + vBed.get_class_name())
print('Modern bed: ' + mBed.get_class_name())
