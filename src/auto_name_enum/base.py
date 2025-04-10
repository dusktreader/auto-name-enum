import enum
import random
import sys
from typing import Any

if sys.version_info < (3, 12):
    from typing_extensions import Self, override
else:
    from typing import Self, override

auto = enum.auto


class AutoNameEnumMeta(enum.EnumMeta):
    @override
    def __contains__(cls, member: Any) -> bool:
        if isinstance(member, str):
            return member in cls.__members__.keys()
        else:
            return super().__contains__(member)


class AutoNameEnum(str, enum.Enum, metaclass=AutoNameEnumMeta):
    """
    An implementation of enum that automatically assigns the value of each item to its name.

    Example:
        class Pets(AutoNameEnum):
            DOG = auto()
            CAT = auto()

        >> fido = Pets.DOG
        >> print(fido)
        'DOG'

    Note:
        This class inherits from str as well as Enum so that it will be properly
        presented by swagger when used in api apps.
    """

    @override
    @staticmethod
    def _generate_next_value_(name: str, *_: Any, **__: Any) -> str:
        return name

    @override
    def __str__(self) -> str:
        return self.value

    @classmethod
    def rando(cls) -> Self:
        return random.choice([e for e in cls])

    @classmethod
    def pretty_list(cls) -> str:
        return ", ".join(str(e) for e in cls)
