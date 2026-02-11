import enum
import random
import sys
from typing import Any

if sys.version_info < (3, 12):
    from typing_extensions import Self, override
else:
    from typing import Self, override

auto = enum.auto


class _AutodocValue:
    """Sentinel wrapper that carries a description alongside an enum member assignment."""

    def __init__(self, description: str) -> None:
        self.description = description


class _EnumDictProxy:
    """
    Wraps an EnumDict to intercept _AutodocValue assignments during class body execution.

    When an _AutodocValue is assigned to a member name, the proxy extracts the description
    and replaces the value with the member name (mimicking auto-naming behavior). All other
    attribute access is delegated to the underlying EnumDict via __getattr__.
    """

    def __init__(self, enum_dict: Any) -> None:
        object.__setattr__(self, "_enum_dict", enum_dict)
        object.__setattr__(self, "_descriptions", {})

    def __setitem__(self, key: str, value: Any) -> None:
        if isinstance(value, _AutodocValue):
            self._descriptions[key] = value.description
            self._enum_dict[key] = key
        else:
            self._enum_dict[key] = value

    def __getitem__(self, key: str) -> Any:
        return self._enum_dict[key]

    def __contains__(self, key: str) -> bool:
        return key in self._enum_dict

    def __getattr__(self, name: str) -> Any:
        return getattr(self._enum_dict, name)


def autodoc(description: str) -> Any:
    """
    Like auto(), but allows attaching a description to the enum member.

    The description can be accessed via the .description property on the enum member.

    Example:
        class Aliens(AutoNameEnum):
            JAWA = autodoc("A small, rodent-like alien from Tatooine")
            EWOK = autodoc("A furry, diminutive alien from the forest moon of Endor")
            HUTT = autodoc("A large, slug-like alien from Nal Hutta")

        >> print(Aliens.JAWA.value)
        'JAWA'
        >> print(Aliens.JAWA.description)
        'A small, rodent-like alien from Tatooine'
    """
    return _AutodocValue(description)


class AutoNameEnumMeta(enum.EnumMeta):
    @classmethod
    @override
    def __prepare__(
        mcs, name: str, bases: tuple[type, ...], **kwds: Any
    ) -> Any:  # ty: ignore[invalid-method-override]  -- returns _EnumDictProxy instead of _EnumDict; intentional to intercept autodoc assignments
        ed = super().__prepare__(name, bases, **kwds)
        return _EnumDictProxy(ed)

    @override
    def __new__(mcs, name: str, bases: tuple[type, ...], namespace: Any, **kwds: Any) -> "AutoNameEnumMeta":
        # Extract descriptions from our proxy before passing the real EnumDict to super
        if isinstance(namespace, _EnumDictProxy):
            descriptions: dict[str, str] = namespace._descriptions
            real_ns = namespace._enum_dict
        else:
            descriptions = {}
            real_ns = namespace

        cls = super().__new__(mcs, name, bases, real_ns, **kwds)
        cls._descriptions = descriptions  # type: ignore[attr-defined]  -- dynamically attaching _descriptions dict to the class; not declared in type stubs
        return cls

    @override
    def __contains__(  # ty: ignore[invalid-method-override]  -- widens parameter type to allow `str in EnumClass` membership checks
        cls, member: Any
    ) -> bool:
        if isinstance(member, str):
            return member in cls.__members__.keys()
        else:
            return super().__contains__(member)


class AutoNameEnum(str, enum.Enum, metaclass=AutoNameEnumMeta):
    """
    An implementation of enum that automatically assigns the value of each item to its name.

    Example:
        class Aliens(AutoNameEnum):
            JAWA = auto()
            EWOK = auto()
            HUTT = auto()

        >> print(Aliens.JAWA)
        'JAWA'

    Members can also be created with autodoc() to attach a description:

        class Aliens(AutoNameEnum):
            JAWA = autodoc("A small, rodent-like alien from Tatooine")
            EWOK = autodoc("A furry, diminutive alien from the forest moon of Endor")

        >> print(Aliens.JAWA.value)
        'JAWA'
        >> print(Aliens.JAWA.description)
        'A small, rodent-like alien from Tatooine'

    Note:
        This class inherits from str as well as Enum so that it will be properly
        presented by swagger when used in api apps.
    """

    @override
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> str:
        """Generate the next value, always returning the member name."""
        return name

    @override
    def __str__(self) -> str:
        return self.value

    @property
    def description(self) -> str | None:
        """Return the description if this member was created with autodoc()."""
        if hasattr(self.__class__, "_descriptions"):
            return self.__class__._descriptions.get(self.name)  # type: ignore[attr-defined]  -- _descriptions is dynamically attached by the metaclass __new__
        return None

    @classmethod
    def rando(cls) -> Self:
        return random.choice([e for e in cls])

    @classmethod
    def pretty_list(cls) -> str:
        return ", ".join(str(e) for e in cls)
