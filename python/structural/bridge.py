from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def get_is_running(self):
        pass

    @abstractmethod
    def set_is_running(self, is_running):
        pass

    @abstractmethod
    def set_speed(self, value: int):
        pass

    @abstractmethod
    def get_speed(self):
        pass


class Toyota(Car):
    is_running: bool = False
    speed: int = 0

    def get_is_running(self):
        return self.is_running

    def set_is_running(self, is_running: bool):
        self.is_running = is_running

    def set_speed(self, value: int):
        self.speed = value

    def get_speed(self):
        return self.speed


class Engine():
    car: Car

    def __init__(self, car: Car):
        self.car = car

    def start(self):
        self.car.set_is_running(True)
        self.car.set_speed(1.0)

    def stop(self):
        self.car.set_is_running(False)
        self.car.set_speed(0.0)

    def accelerate(self, value):
        new_speed: int = self.car.get_speed() + value
        self.car.set_speed(new_speed)

    def slow_down(self, value):
        new_speed: int = self.car.get_speed() - value
        self.car.set_speed(new_speed)

# Now we can modify both of these bridge classes (abstraction and implementation) separately.
# We control Car field with an engine that can drive it.
# We can add additional methods or fields to Car to complicate its behavior, eg.


toyota: Car = Toyota()
engine: Engine = Engine(toyota)
print('---------------------------------------------------')
print(f'Start: ')
print(f'Is runned? {toyota.get_is_running()}')
print(f'Speed? {toyota.get_speed()}')
print('After we turn car on.')
engine.start()
print(f'Is runned? ', toyota.get_is_running())
print(f'Speed? {toyota.get_speed()}')
print('Increase speed by 50.')
engine.accelerate(50.0)
print(f'Is runned? ', toyota.get_is_running())
print(f'Speed? {toyota.get_speed()}')
print('Decrease speed by 14.')
engine.slow_down(14.0)
print(f'Is runned? ', toyota.get_is_running())
print(f'Speed? {toyota.get_speed()}')
