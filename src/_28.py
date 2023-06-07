from abc import ABC, abstractmethod
from typing import Tuple


class IAnimal(ABC):
    @abstractmethod
    def speak(self) -> None:
        ...


class Dog(IAnimal):
    def speak(self) -> None:
        print("Woof!")


class Cat(IAnimal):
    def speak(self) -> None:
        print("Meaow!")


class Cow(IAnimal):
    def speak(self) -> None:
        print("Moo!")


animals: Tuple[IAnimal] = (Dog(), Cat(), Cat(), Dog(), Cow())

for animal in animals:
    animal.speak()