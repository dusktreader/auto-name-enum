import enum
from typing import Any, override


class LowerCaseMixin(enum.Enum):
    """
    This mixin can be used to make values lower case.

    Example:
        class Pets(AutoNameMixin, LowerCaseMixin):
            DOG = auto()
            CAT = auto()

        >> fido = Pets.DOG
        >> print(fido)
        'dog'

    Note:
        Inheritance order is important! This must *follow* AutoNameEnum in the
        list of subclasses
    """

    @override
    @staticmethod
    def _generate_next_value_(name: str, *_: Any, **__: Any) -> str:
        return name.lower()


class TitleCaseMixin(enum.Enum):
    """
    This mixin can be used to make values lower case.

    Example:
        class Pets(AutoNameMixin, TitleCaseMixin):
            DOG = auto()
            CAT = auto()

        >> fido = Pets.DOG
        >> print(fido)
        'Dog'

    Note:
        Inheritance order is important! This must *follow* AutoNameEnum in the
        list of subclasses
    """

    @override
    @staticmethod
    def _generate_next_value_(name: str, *_: Any, **__: Any) -> str:
        return name[0].upper() + name[1:].lower()
