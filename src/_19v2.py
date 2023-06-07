from operator import attrgetter


class Dying:
    is_alive = property(attrgetter("_is_alive"))  # Public
    _is_alive: bool = True  # Protected

    def __init__(self, name: str):
        self.name = name  # Public

    def die(self) -> None:  # Public
        self._is_alive = False


class Human(Dying):
    def say(self) -> str:  # Public
        return "{} {}".format(
            self.name,
            "said something" if self._is_alive else "won't say anything",
        )

class Beast(Dying):
    def scream(self) -> str:  # Public
        return "{} {}".format(
            self.name,
            "screamed" if self._is_alive else "won't scream anything",
        )


oleg = Human("Oleg")
fox = Beast("Fox")

print(oleg.say())
print(fox.scream())

fox.die()

print(fox.scream())