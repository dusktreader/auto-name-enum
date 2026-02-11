from auto_name_enum import AutoNameEnum, auto, LowerCaseMixin, TitleCaseMixin


class LowerEnum(AutoNameEnum, LowerCaseMixin):
    JAWA = auto()
    EWOK = auto()
    HUTT = auto()


class TestLowerCaseMixin:
    def test_auto(self):
        assert LowerEnum.JAWA.value == "jawa"
        assert LowerEnum.EWOK.value == "ewok"
        assert LowerEnum.HUTT.value == "hutt"


class TitleEnum(AutoNameEnum, TitleCaseMixin):
    JAWA = auto()
    EWOK = auto()
    HUTT = auto()


class TestTitleCaseMixin:
    def test_auto(self):
        assert TitleEnum.JAWA.value == "Jawa"
        assert TitleEnum.EWOK.value == "Ewok"
        assert TitleEnum.HUTT.value == "Hutt"
