from operator import attrgetter


class Human(Dying):
    is_alive = property(attrgetter("_Human__is_alive"))  # Public
    __is_alive: bool = True  # Private

    def __init__(self, name: str):
        self.name = name  # Public

    def say(self) -> str:  # Public
        return "{} {}".format(
            self.name,
            "said something" if self._is_alive else "won't say anything",
        )

    def die(self) -> None:  # Public
        self.__is_alive = False


class Beast(Dying):
    is_alive = property(attrgetter("_Beast__is_alive"))  # Public
    __is_alive: bool = True  # Private

    def __init__(self, name: str):
        self.name = name  # Public

    def scream(self) -> str:  # Public
        return "{} {}".format(
            self.name,
            "screamed" if self._is_alive else "won't scream anything",
        )

    def die(self) -> None:  # Public
        self.__is_alive = False
