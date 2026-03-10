# A utility for producing enums with automatic names

This package provides an extension of python Enum objects that automatically
assigns values to members. This uses the `auto()` feature to assign text values
to the enums instead of having to manually set them.


## Specifying your enum
For example, you might create an enum with this like so:

```
class Aliens(AutoNameEnum):
    JAWA = auto()
    EWOK = auto()
    HUTT = auto()
    PYKE = auto()
```

## Getting values

Using the class, verify the value of `JAWA` would be 'JAWA':

```
>>> print(Aliens.JAWA.value)
'JAWA'
```

You may also get the same value by just using the name of the item:

```
>>> print(Aliens.JAWA)
'JAWA'
```

## Iterating

Python enums may be iterated over:

```
for alien in Aliens:
    print(f"name: {alien.name}, value: {alien.value}")
```

For more information on enums (and the auto method), see [the official docs]
(https://docs.python.org/3/library/enum.html)


## Mixins

There are two mixins provided that change the case of member values for both `auto()` and `autodoc()`:

- `LowerCaseMixin`: values are in all lower-case
- `TitleCaseMixin`: values are in title-case (lower-case except for first letter)

When these mixins are used, they _must_ be included after `AutoNameEnum` in the class inheritance declaration:

```python
class Aliens(AutoNameEnum, TitleCaseMixin)
    JAWA = auto()
    EWOK = auto()
    HUTT = auto()
    PYKE = auto()
```


## Documented members with `autodoc()`

The `autodoc()` function works like `auto()`, but also attaches a `description` and/or
`display_name` to each enum member. This is useful for self-documenting enums where members
need human-readable explanations or labels:

```python
class Aliens(AutoNameEnum):
    JAWA = autodoc("A small, rodent-like alien from Tatooine")
    EWOK = autodoc("A furry, diminutive alien from the forest moon of Endor")
    HUTT = autodoc("A large, slug-like alien from Nal Hutta")
    PYKE = autodoc("A secretive, spice-dealing alien from Oba Diah")
```

The value works just like `auto()`:

```
>>> print(Aliens.JAWA.value)
'JAWA'
```

Access the description via the `.description` property:

```
>>> print(Aliens.JAWA.description)
'A small, rodent-like alien from Tatooine'
```

A `display_name` can also be attached as a keyword argument:

```python
class Aliens(AutoNameEnum):
    JAWA = autodoc(description="A small, rodent-like alien from Tatooine", display_name="Jawa (Tatooine)")
    EWOK = autodoc(description="A furry, diminutive alien from the forest moon of Endor", display_name="Ewok (Endor)")
```

```
>>> print(Aliens.JAWA.display_name)
'Jawa (Tatooine)'
```

You can mix `auto()` and `autodoc()` in the same enum. Members created with `auto()` will return
`None` for `.description` and their value for `.display_name`:

```python
class Aliens(AutoNameEnum):
    JAWA = autodoc("A small, rodent-like alien from Tatooine")
    EWOK = auto()
    HUTT = autodoc("A large, slug-like alien from Nal Hutta")
```

```
>>> print(Aliens.JAWA.description)
'A small, rodent-like alien from Tatooine'
>>> print(Aliens.EWOK.description)
None
>>> print(Aliens.EWOK.display_name)
'EWOK'
```
