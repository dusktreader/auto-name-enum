from collections import Counter
import sys

import pytest

from auto_name_enum import AutoNameEnum, NoMangleMixin, auto


class DummyEnum(AutoNameEnum):
    DOG = auto()
    CAT = auto()
    PIG = auto()


class TestAutoNameEnum:
    def test_auto(self):
        """
        This test verifies that the values of the items from the enum are
        the lower-case version of the name
        """
        assert DummyEnum.DOG.value == "dog"
        assert DummyEnum.CAT.value == "cat"
        assert DummyEnum.PIG.value == "pig"

    def test_rando(self):
        """
        This test verifies a goodness of fit of the rando() function using
        a chi-squared distribution with 95% confidence
        """
        results = Counter()
        N = 10000
        for _ in range(N):
            results[DummyEnum.rando()] += 1
        chi_squared = 0
        Ei = N / len(DummyEnum)
        df = len(DummyEnum) - 1
        print(Ei, df, results)
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
        assert DummyEnum.pretty_list() == "dog, cat, pig"

    def test___str__(self):
        """
        This test verifies that the enum's entries can be properly cast to
        strings
        """
        assert str(DummyEnum.DOG) == "dog"
        assert str(DummyEnum.CAT) == "cat"
        assert str(DummyEnum.PIG) == "pig"

    def test___contains__(self):
        assert "dog" in DummyEnum
        assert "DOG" in DummyEnum
        assert "Dog" in DummyEnum
        # check we didn't break normal contains
        assert DummyEnum.DOG in DummyEnum
        # python 3.6 and 3.7 just return False for __contains__ on enums with incorrect types
        # python 3.8+ throws a type error
        if sys.version_info.minor < 8:
            assert 1 not in DummyEnum
        else:
            with pytest.raises(TypeError):
                1 in DummyEnum


class IdiotEnum(AutoNameEnum, NoMangleMixin):
    DOG = auto()
    CAT = auto()
    PIG = auto()


class TestNoMangleMixin:
    @pytest.mark.skipif(sys.version_info.minor < 7, reason="NoMangleMixin does not work in python 3.6")
    def test_auto(self):
        """
        This test verifies that the values of the items from the enum are
        the same as the original name
        """
        assert IdiotEnum.DOG.value == "DOG"
        assert IdiotEnum.CAT.value == "CAT"
        assert IdiotEnum.PIG.value == "PIG"
