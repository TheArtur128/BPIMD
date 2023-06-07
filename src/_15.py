from operator import attrgetter
from typing import Iterable


class Room:
    name = property(attrgetter("_Room__name"))  # Public

    def __init__(self, name: str, *, is_light_on: bool = False):
        self.__name = name  # Private
        self.is_light_on = is_light_on  # Public



class Building:
    id_ = property(attrgetter("_Building__id"))  # Public

    def __init__(self, id_: int, rooms: Iterable[Room]):
        self.__id = id_  # Private
        self.__rooms = tuple(rooms)  # Private
        self.__is_light_on = False  # Private

    @property
    def is_light_on(self) -> bool:  # Public
        return all(room.is_light_on for room in self.__rooms)

    def turn_light(self) -> None: # Public
        for room in self.__rooms:
            room.is_light_on = True


kitchen = Room("Kitchen")
bedroom = Room("Bedroom", is_light_on=True)

building = Building(42, [kitchen, bedroom])

bedroom.name  # Ok
# bedroom.__name  # Error
# building.__rooms  # Error

print(f"\nThere is a light on in the bedroom - {bedroom.is_light_on}")
print(f"There is a light on in the building - {building.is_light_on}")

kitchen.is_light_on = True
print("\nTurn on a light in the kitchen\n")

print(f"There is a light on in the building - {building.is_light_on}")
