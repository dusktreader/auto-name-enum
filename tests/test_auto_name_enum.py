import sys
from collections import Counter

import pytest

from auto_name_enum import AutoNameEnum, auto, autodoc


class DummyEnum(AutoNameEnum):
    JAWA = auto()
    EWOK = auto()
    HUTT = auto()


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


class PositionalDescriptionEnum(AutoNameEnum):
    JAWA = autodoc("A small, rodent-like alien from Tatooine")
    EWOK = autodoc("A furry, diminutive alien from the forest moon of Endor")
    HUTT = autodoc("A large, slug-like alien from Nal Hutta")
    PYKE = autodoc("A secretive, spice-dealing alien from Oba Diah")


class KwargDocsEnum(AutoNameEnum):
    JAWA = autodoc(description="A small, rodent-like alien from Tatooine", display_name="Jawa (Tatooine)")
    EWOK = autodoc(description="A furry, diminutive alien from the forest moon of Endor", display_name="Ewok (Endor)")
    HUTT = autodoc(description="A large, slug-like alien from Nal Hutta", display_name="Hutt (Nal Hutta)")
    PYKE = autodoc(description="A secretive, spice-dealing alien from Oba Diah", display_name="Pyke (Oba Diah)")


class MixedEnum(AutoNameEnum):
    JAWA = autodoc("A small, rodent-like alien from Tatooine")
    EWOK = auto()
    HUTT = autodoc(description="A large, slug-like alien from Nal Hutta")
    PYKE = autodoc(description="A secretive, spice-dealing alien from Oba Diah", display_name="Pyke (Oba Diah)")


class TestAutodoc:
    def test_autodoc_value(self):
        """
        Test that autodoc enum members still have the correct auto-generated value
        """
        assert PositionalDescriptionEnum.JAWA.value == "JAWA"
        assert PositionalDescriptionEnum.EWOK.value == "EWOK"
        assert PositionalDescriptionEnum.HUTT.value == "HUTT"
        assert PositionalDescriptionEnum.PYKE.value == "PYKE"

    def test_autodoc_str(self):
        """
        Test that autodoc enum members can be properly cast to strings
        """
        assert str(PositionalDescriptionEnum.JAWA) == "JAWA"
        assert str(PositionalDescriptionEnum.EWOK) == "EWOK"
        assert str(PositionalDescriptionEnum.HUTT) == "HUTT"
        assert str(PositionalDescriptionEnum.PYKE) == "PYKE"

    def test_autodoc_positional_description(self):
        """
        Test that autodoc enum members have the correct description
        """
        assert PositionalDescriptionEnum.JAWA.description == "A small, rodent-like alien from Tatooine"
        assert PositionalDescriptionEnum.EWOK.description == "A furry, diminutive alien from the forest moon of Endor"
        assert PositionalDescriptionEnum.HUTT.description == "A large, slug-like alien from Nal Hutta"
        assert PositionalDescriptionEnum.PYKE.description == "A secretive, spice-dealing alien from Oba Diah"

    def test_autodoc_kwarg_docs(self):
        """
        Test that autodoc enum members have the correct description
        """
        assert KwargDocsEnum.JAWA.description == "A small, rodent-like alien from Tatooine"
        assert KwargDocsEnum.EWOK.description == "A furry, diminutive alien from the forest moon of Endor"
        assert KwargDocsEnum.HUTT.description == "A large, slug-like alien from Nal Hutta"
        assert KwargDocsEnum.PYKE.description == "A secretive, spice-dealing alien from Oba Diah"

        assert KwargDocsEnum.JAWA.display_name == "Jawa (Tatooine)"
        assert KwargDocsEnum.EWOK.display_name == "Ewok (Endor)"
        assert KwargDocsEnum.HUTT.display_name == "Hutt (Nal Hutta)"
        assert KwargDocsEnum.PYKE.display_name == "Pyke (Oba Diah)"

    def test_mixed_auto_and_autodoc(self):
        """
        Test that auto() and autodoc() can be mixed in the same enum
        """
        assert MixedEnum.JAWA.value == "JAWA"
        assert MixedEnum.JAWA.description == "A small, rodent-like alien from Tatooine"
        assert MixedEnum.JAWA.display_name == "JAWA"

        assert MixedEnum.EWOK.value == "EWOK"
        assert MixedEnum.EWOK.description is None
        assert MixedEnum.EWOK.display_name == "EWOK"

        assert MixedEnum.HUTT.value == "HUTT"
        assert MixedEnum.HUTT.description == "A large, slug-like alien from Nal Hutta"
        assert MixedEnum.HUTT.display_name == "HUTT"

        assert MixedEnum.PYKE.value == "PYKE"
        assert MixedEnum.PYKE.description == "A secretive, spice-dealing alien from Oba Diah"
        assert MixedEnum.PYKE.display_name == "Pyke (Oba Diah)"

    def test_autodoc_iteration(self):
        """
        Test that enums with autodoc can be iterated over
        """
        members = list(PositionalDescriptionEnum)
        assert len(members) == 4
        assert PositionalDescriptionEnum.JAWA in members
        assert PositionalDescriptionEnum.EWOK in members
        assert PositionalDescriptionEnum.HUTT in members
        assert PositionalDescriptionEnum.PYKE in members
