from abc import ABC, abstractmethod
from typing import TypeVar, Iterable


V = TypeVar('V')


class IHeadSlicer(ABC):
    @abstractmethod
    def head_of(self, items: Iterable[V]) -> Iterable[V]:
        ...


class OnlyListSlicer(IHeadSlicer):
    def head_of(self, items: list[V]) -> list[V]:  # Error
        ...


class InclusiveListSlicer(IHeadSlicer):
    def head_of(self, items: Iterable[V]) -> list[V]:  # Ok
        ...


only_list_slicer: IHeadSlicer = OnlyListSlicer()
only_list_slicer.head_of((1, 2, 3))  # Error

inclusive_list_slicer: IHeadSlicer = InclusiveListSlicer()
inclusive_list_slicer.head_of((1, 2, 3))  # Ok
inclusive_list_slicer.head_of((1, 2, 3)).append(4)  # Error
