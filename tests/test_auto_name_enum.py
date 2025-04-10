from collections import Counter

from auto_name_enum import AutoNameEnum, auto


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
        assert DummyEnum.DOG.value == "DOG"
        assert DummyEnum.CAT.value == "CAT"
        assert DummyEnum.PIG.value == "PIG"

    def test_rando(self):
        """
        This test verifies a goodness of fit of the rando() function using
        a chi-squared distribution with 95% confidence
        """
        results: Counter[DummyEnum] = Counter()
        N = 10000
        for _ in range(N):
            results[DummyEnum.rando()] += 1
        chi_squared = 0
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
        assert DummyEnum.pretty_list() == "DOG, CAT, PIG"

    def test___str__(self):
        """
        This test verifies that the enum's entries can be properly cast to
        strings
        """
        assert str(DummyEnum.DOG) == "DOG"
        assert str(DummyEnum.CAT) == "CAT"
        assert str(DummyEnum.PIG) == "PIG"
