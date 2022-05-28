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
