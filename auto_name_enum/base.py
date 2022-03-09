import enum
import random


auto = enum.auto


class AutoNameEnumMeta(enum.EnumMeta):
    def __contains__(cls, member):
        if isinstance(member, str):
            return member.upper() in map(str.upper, cls.__members__.keys())
        else:
            super().__contains__(member)


class AutoNameEnum(str, enum.Enum, metaclass=AutoNameEnumMeta):
    """
    An implementation of enum that automatically assigns the value of each item
    to the lower-case version of the name

    Example:
        class Pets(AutoNameEnum):
            DOG = auto()
            CAT = auto()

        >> fido = Pets.DOG
        >> print(fido)
        'dog'

    Note:
        this class inherits from str as well as Enum so that it will be properly
        presented by swagger when used in api apps
    """

    def _generate_next_value_(name: str, *_):  # type: ignore
        return name.lower()

    def __str__(self):
        return self.value

    @classmethod
    def rando(cls, *_):
        return random.choice([e for e in cls])

    @classmethod
    def pretty_list(cls):
        return ", ".join(str(e) for e in cls)


class NoMangleMixin(enum.Enum):
    """
    This mixin can be used to disable the default mangling of values that
    AutoNameMixin performs (forcing values to lower-case).

    Example:
        class Pets(AutoNameMixin, NoMangleMixin):
            DOG = auto()
            CAT = auto()

        >> fido = Pets.DOG
        >> print(fido)
        'DOG'

    Note:
        Inheritance order is important! This must *follow* AutoNameEnum in the
        list of subclasses
    """

    def _generate_next_value_(name: str, *_):  # type: ignore
        return name
