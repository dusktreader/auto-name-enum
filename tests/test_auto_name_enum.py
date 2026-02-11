import sys
from collections import Counter

import pytest

from auto_name_enum import AutoNameEnum, auto, autodoc


class DummyEnum(AutoNameEnum):
    JAWA = auto()
    EWOK = auto()
    HUTT = auto()


class DocEnum(AutoNameEnum):
    JAWA = autodoc("A small, rodent-like alien from Tatooine")
    EWOK = autodoc("A furry, diminutive alien from the forest moon of Endor")
    HUTT = autodoc("A large, slug-like alien from Nal Hutta")
    PYKE = autodoc("A secretive, spice-dealing alien from Oba Diah")


class MixedEnum(AutoNameEnum):
    JAWA = autodoc("A small, rodent-like alien from Tatooine")
    EWOK = auto()
    HUTT = autodoc("A large, slug-like alien from Nal Hutta")


class TestAutoNameEnum:
    def test_auto(self):
        """
        This test verifies that the values of the items from the enum are
        the lower-case version of the name
        """
        assert DummyEnum.JAWA.value == "JAWA"
        assert DummyEnum.EWOK.value == "EWOK"
        assert DummyEnum.HUTT.value == "HUTT"

    def test_rando(self):
        """
        This test verifies a goodness of fit of the rando() function using
        a chi-squared distribution with 95% confidence.

        The RNG is seeded so the test is deterministic.
        """
        import random

        random.seed(42)
        results: Counter[DummyEnum] = Counter()
        N = 10000
        for _ in range(N):
            results[DummyEnum.rando()] += 1
        chi_squared = 0.0
        Ei = N / len(DummyEnum)
        df = len(DummyEnum) - 1
        critical_values_95 = {
            1: 3.841,
            2: 5.991,
            3: 7.815,
            4: 9.488,
            5: 11.070,
            6: 12.592,
            7: 14.067,
            8: 15.507,
            9: 16.919,
            10: 18.307,
        }
        for n in results.values():
            chi_squared += (n - Ei) ** 2 / Ei
        assert chi_squared < critical_values_95[df]

    def test_pretty_list(self):
        """
        This test verifies that the pretty_list function produces a nice
        list of the enumerated values
        """
        assert DummyEnum.pretty_list() == "JAWA, EWOK, HUTT"

    def test___str__(self):
        """
        This test verifies that the enum's entries can be properly cast to
        strings
        """
        assert str(DummyEnum.JAWA) == "JAWA"
        assert str(DummyEnum.EWOK) == "EWOK"
        assert str(DummyEnum.HUTT) == "HUTT"

    def test___contains__(self):
        assert "jawa" not in DummyEnum
        assert "JAWA" in DummyEnum
        assert "Jawa" not in DummyEnum
        # check we didn't break normal contains
        assert DummyEnum.JAWA in DummyEnum
        if sys.version_info < (3, 12):
            # python 3.9,10,11 throw a type error
            with pytest.raises(TypeError):
                1 in DummyEnum
        else:
            # python 3.12 and 3.13 just return False for __contains__ on enums with incorrect types
            assert 1 not in DummyEnum


class TestAutodoc:
    def test_autodoc_value(self):
        """
        Test that autodoc enum members still have the correct auto-generated value
        """
        assert DocEnum.JAWA.value == "JAWA"
        assert DocEnum.EWOK.value == "EWOK"
        assert DocEnum.HUTT.value == "HUTT"
        assert DocEnum.PYKE.value == "PYKE"

    def test_autodoc_description(self):
        """
        Test that autodoc enum members have the correct description
        """
        assert DocEnum.JAWA.description == "A small, rodent-like alien from Tatooine"
        assert DocEnum.EWOK.description == "A furry, diminutive alien from the forest moon of Endor"
        assert DocEnum.HUTT.description == "A large, slug-like alien from Nal Hutta"
        assert DocEnum.PYKE.description == "A secretive, spice-dealing alien from Oba Diah"

    def test_autodoc_str(self):
        """
        Test that autodoc enum members can be properly cast to strings
        """
        assert str(DocEnum.JAWA) == "JAWA"
        assert str(DocEnum.EWOK) == "EWOK"
        assert str(DocEnum.HUTT) == "HUTT"
        assert str(DocEnum.PYKE) == "PYKE"

    def test_mixed_auto_and_autodoc(self):
        """
        Test that auto() and autodoc() can be mixed in the same enum
        """
        assert MixedEnum.JAWA.value == "JAWA"
        assert MixedEnum.JAWA.description == "A small, rodent-like alien from Tatooine"

        assert MixedEnum.EWOK.value == "EWOK"
        assert MixedEnum.EWOK.description is None

        assert MixedEnum.HUTT.value == "HUTT"
        assert MixedEnum.HUTT.description == "A large, slug-like alien from Nal Hutta"

    def test_autodoc_iteration(self):
        """
        Test that enums with autodoc can be iterated over
        """
        members = list(DocEnum)
        assert len(members) == 4
        assert DocEnum.JAWA in members
        assert DocEnum.EWOK in members
        assert DocEnum.HUTT in members
        assert DocEnum.PYKE in members

    def test_description_on_auto_members(self):
        """
        Test that members created with auto() return None for description
        """
        assert DummyEnum.JAWA.description is None
        assert DummyEnum.EWOK.description is None
        assert DummyEnum.HUTT.description is None
