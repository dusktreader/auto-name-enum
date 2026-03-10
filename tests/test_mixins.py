from auto_name_enum import AutoNameEnum, auto, autodoc, LowerCaseMixin, TitleCaseMixin


class LowerEnum(AutoNameEnum, LowerCaseMixin):
    JAWA = auto()
    EWOK = auto()
    HUTT = auto()


class LowerAutoDocEnum(AutoNameEnum, LowerCaseMixin):
    JAWA = autodoc(description="A small, rodent-like alien from Tatooine", display_name="Jawa (Tatooine)")
    EWOK = autodoc(description="A furry, diminutive alien from the forest moon of Endor", display_name="Ewok (Endor)")
    HUTT = autodoc(description="A large, slug-like alien from Nal Hutta", display_name="Hutt (Nal Hutta)")


class TestLowerCaseMixin:
    def test_auto(self):
        assert LowerEnum.JAWA.value == "jawa"
        assert LowerEnum.EWOK.value == "ewok"
        assert LowerEnum.HUTT.value == "hutt"

    def test_autodoc(self):
        assert LowerAutoDocEnum.JAWA.value == "jawa"
        assert LowerAutoDocEnum.JAWA.description == "A small, rodent-like alien from Tatooine"
        assert LowerAutoDocEnum.JAWA.display_name == "Jawa (Tatooine)"
        assert LowerAutoDocEnum.EWOK.value == "ewok"
        assert LowerAutoDocEnum.EWOK.description == "A furry, diminutive alien from the forest moon of Endor"
        assert LowerAutoDocEnum.EWOK.display_name == "Ewok (Endor)"
        assert LowerAutoDocEnum.HUTT.value == "hutt"
        assert LowerAutoDocEnum.HUTT.description == "A large, slug-like alien from Nal Hutta"
        assert LowerAutoDocEnum.HUTT.display_name == "Hutt (Nal Hutta)"


class TitleEnum(AutoNameEnum, TitleCaseMixin):
    JAWA = auto()
    EWOK = auto()
    HUTT = auto()


class TitleAutoDocEnum(AutoNameEnum, TitleCaseMixin):
    JAWA = autodoc(description="A small, rodent-like alien from Tatooine", display_name="Jawa (Tatooine)")
    EWOK = autodoc(description="A furry, diminutive alien from the forest moon of Endor", display_name="Ewok (Endor)")
    HUTT = autodoc(description="A large, slug-like alien from Nal Hutta", display_name="Hutt (Nal Hutta)")


class TestTitleCaseMixin:
    def test_auto(self):
        assert TitleEnum.JAWA.value == "Jawa"
        assert TitleEnum.EWOK.value == "Ewok"
        assert TitleEnum.HUTT.value == "Hutt"

    def test_autodoc(self):
        assert TitleAutoDocEnum.JAWA.value == "Jawa"
        assert TitleAutoDocEnum.JAWA.description == "A small, rodent-like alien from Tatooine"
        assert TitleAutoDocEnum.JAWA.display_name == "Jawa (Tatooine)"
        assert TitleAutoDocEnum.EWOK.value == "Ewok"
        assert TitleAutoDocEnum.EWOK.description == "A furry, diminutive alien from the forest moon of Endor"
        assert TitleAutoDocEnum.EWOK.display_name == "Ewok (Endor)"
        assert TitleAutoDocEnum.HUTT.value == "Hutt"
        assert TitleAutoDocEnum.HUTT.description == "A large, slug-like alien from Nal Hutta"
        assert TitleAutoDocEnum.HUTT.display_name == "Hutt (Nal Hutta)"
