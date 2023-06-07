from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import partial
from operator import attrgetter
from typing import Iterable, Generator


@dataclass
class Room:
    name: str
    is_light_on: bool = False


class Premise(ABC):  # Помещение
    @property
    @abstractmethod
    def rooms(self) -> Iterable[Room]:
        ...

    @property
    def is_light_on(self) -> bool:
        return all(room.is_light_on for room in self.rooms)

    def turn_light(self) -> None:
        for room in self.rooms:
            room.is_light_on = True


class Studio(Premise):
    rooms = property(lambda studio: [studio._room])

    def __init__(self, room: Room):
        self._room = room


class Apartment(Premise):
    rooms = property(attrgetter("_rooms"))

    def __init__(self, rooms: Iterable[Room]):
        self._rooms = tuple(rooms)


class Building(Premise):
    id_ = property(attrgetter('_id'))

    def __init__(self, id_: int, premises: Iterable[Premise]):
        self._id = id_
        self._premises = tuple(premises)

    @property
    def rooms(self) -> Generator[Room, None, None]:
        for rooms in map(attrgetter("rooms"), self._premises):
            yield from rooms


bedroom = Room("bedroom", is_light_on=True)
kitchen = Room("kitchen", is_light_on=True)
living_room = Room("living_room")
balcony = Room("balcony", is_light_on=True)

studio = Studio(kitchen)
building = partial(Building, 42)([
    Apartment([balcony, living_room]),
    Studio(bedroom),
])

print(f"Lights on in the studio - {studio.is_light_on}")
print(f"Lights on in the building - {building.is_light_on}")

living_room.is_light_on = True
print(
    "\nTurning on the light in the living room "
    "in the building's apartment\n"
)

print(f"Lights on in the building - {building.is_light_on}")