from typing import Any, TypeVar, Callable


def square_of(number_or_line: int | float | str) -> str:
    return (
        str(float(number_or_line)**2)
        if isinstance(number_or_line, str)
        else number_or_line**2
    )

# Не смотреть
def _repr_with_type_of(value: Any) -> str:
    return f"{value} ({type(value).__name__})"


V = TypeVar('V')
R = TypeVar('R')


def _showly(action: Callable[V, R], value: V) -> R:
    result = action(value)
    print("{} -> {}".format(
        _repr_with_type_of(value),
        _repr_with_type_of(result),
    ))

    return result
# Смотреть

_showly(square_of, 4)
_showly(square_of, '4')