# A utility for producing enums with automatic names

This package provides an extension of python Enum objects that automatically
assigns values to members. This uses the `auto()` feature to assign text values
to the enums instead of having to manually set them.


## Specifying your enum
For example, you might create an enum with this like so:

```
class Pets(AutoNameEnum):
    DOG = auto()
    CAT = auto()
    PIG = auto()
```

## Getting values

Using the class, verify the value of `DOG` would be 'dog':

```
>>> print(Pets.DOG.value)
'DOG'
```

You may also get the same value by just using the name of the item:

```
>>> print(Pets.DOG)
'DOG'
```

## Iterating

Python enums may be iterated over:

```
for pet in Pets:
    print(f"name: {pet.name}, value: {pet.value}")
```

For more information on enums (and the auto method), see [the official docs]
(https://docs.python.org/3/library/enum.html)


## Mixins

There are two mixins provided that change the behavior of `auto()`:

- `LowerCaseMixin`: values produced by `auto()` are in all lower-case
- `TitleCaseMixin`: values produced by `auto()` will be in title- case (lower-case except for first letter)

When these mixins are used, they _must_ be included after `AutoNameEnum` in the class inheritance declaration:

```python
class Pets(AutoNameEnum, TitleCaseMixin)
    DOG = auto()
    CAT = auto()
    PIG = auto()
```
