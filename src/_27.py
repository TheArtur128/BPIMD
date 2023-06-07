from abc import ABC, abstractmethod
from operator import attrgetter
from typing import TypeVar, Generic, Any, Tuple


_ObjT = TypeVar("_ObjT")


class Instrument(ABC, Generic[_ObjT]):
    quality = property(attrgetter("_quality"))

    def __init__(self, quality: int):
        self._quality = quality

    def interact_with(self, obj: _ObjT) -> None:
        if self._quality <= 0:
            print("this instrument is broken")
            return

        self._apply(obj)
        self._quality -= 1

    @abstractmethod
    def _apply(self, obj: _ObjT) -> None:
        ...


class Sword(Instrument):
    def _apply(self, obj: Any) -> None:
        print(f"{obj} was attacked")


class Plow(Instrument):
    def _apply(self, obj: Any) -> None:
        print(f"{obj} was plowed")


sword = Sword(1)

sword.interact_with("some man")
sword.interact_with("other man")
print()

instruments: Tuple[Instrument] = (Sword(2), Plow(1))

for instrument in instruments:
    instrument.interact_with("something")