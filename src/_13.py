from typing import Iterable


class Color:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return self.name


class Fruit:
    def __init__(self, name: str, colors: Iterable[Color]):
        self.name = name
        self.colors = tuple(colors)

    def get_color_report(self) -> str:
        return "{} can only be {}".format(
            self.name.capitalize(),
            " or ".join(map(str, self.colors)),
        )


red = Color('red')
green = Color("green")
yellow = Color("yellow")

apple = Fruit("apple", [red, green, yellow])
papaya = Fruit("papaya", [green, yellow])
banana = Fruit("banana", [yellow])

print(banana.get_color_report())
print(papaya.get_color_report())
print(apple.get_color_report())