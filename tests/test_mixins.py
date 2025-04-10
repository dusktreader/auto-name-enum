from auto_name_enum import AutoNameEnum, auto, LowerCaseMixin, TitleCaseMixin


class LowerEnum(AutoNameEnum, LowerCaseMixin):
    DOG = auto()
    CAT = auto()
    PIG = auto()


class TestLowerCaseMixin:
    def test_auto(self):
        assert LowerEnum.DOG.value == "dog"
        assert LowerEnum.CAT.value == "cat"
        assert LowerEnum.PIG.value == "pig"


class TitleEnum(AutoNameEnum, TitleCaseMixin):
    DOG = auto()
    CAT = auto()
    PIG = auto()

class TestTitleCaseMixin:
    def test_auto(self):
        assert TitleEnum.DOG.value == "Dog"
        assert TitleEnum.CAT.value == "Cat"
        assert TitleEnum.PIG.value == "Pig"
