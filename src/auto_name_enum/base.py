from enum import StrEnum, auto
import random
from typing import Any, Self, override


class AutoNameEnum(StrEnum):
    """
    Some syntactic sugar on top of StrEnum.

    In particular, it will not convert names to lower-case values.

    Example:
        class Pets(AutoNameEnum):
            DOG = auto()
            CAT = auto()

        >> fido = Pets.DOG
        >> print(fido)
        'DOG'
    """

    @override
    @staticmethod
    def _generate_next_value_(name: str, *_: Any, **__: Any) -> str:
        return name

    @classmethod
    def rando(cls) -> Self:
        return random.choice([e for e in cls])

    @classmethod
    def pretty_list(cls) -> str:
        return ", ".join(str(e) for e in cls)
