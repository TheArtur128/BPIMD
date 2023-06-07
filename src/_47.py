from dataclasses import dataclass


@dataclass(frozen=True)
class RGBColor:
    red: int
    green: int
    blue: int

    def __post_init__(self) -> None:
        assert 0 <= self.red <= 255
        assert 0 <= self.green <= 255
        assert 0 <= self.blue <= 255


yellow = RGBColor(255, 255, 0)  # Ok
no_color = RGBColor(-4, 1024, 42)  # Error


def is_valid(color: RGBColor) -> bool:  # Always `True`
    return 0 <= color.red + color.green + color.blue <= 765
