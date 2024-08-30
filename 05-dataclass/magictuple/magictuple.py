"""
MagicTuple: a factory for namedtuples with class syntax

>>> from magictuple import MagicTuple
>>> class Coordinate(MagicTuple):
...     lat
...     lon
...
...     def hemisphere(self):
...         ns = 'N' if self.lat >= 0 else 'S'
...         ew = 'E' if self.lon >= 0 else 'W'
...         return ns + ew
>>> c = Coordinate(-23.5558, -46.6396)
>>> c.lat
-23.5558
>>> c.lon
-46.6396
>>> c
Coordinate(lat=-23.5558, lon=-46.6396)
>>> type(c)
<class 'magictuple.Coordinate'>
>>> isinstance(c, tuple)
True
>>> issubclass(Coordinate, tuple)
True

Support for instance methods:

>>> c.hemisphere()
'SW'

Error handled by namedtuple:

>>> d = Coordinate(23.5558)
Traceback (most recent call last):
  ...
TypeError: Coordinate.__new__() missing 1 required positional argument: 'lon'
"""


from collections import defaultdict, namedtuple

MAGIC_FIELD = object()


class MagicDict(dict):

    def __missing__(self, key):
        if key.startswith('__') and key.endswith('__'):
            raise KeyError(key)
        self[key] = MAGIC_FIELD
        return MAGIC_FIELD


class MagicTupleMeta(type):

    @classmethod
    def __prepare__(metacls, _name, _bases):
        return MagicDict()


class MagicTuple(tuple, metaclass=MagicTupleMeta):

    cache = {}

    def __new__(cls, *args):
        cls_dict = cls.__dict__
        tuple_cls = cls.cache.get(cls.__name__)
        if tuple_cls is None:
            field_names = []
            other_attrs = []
            for name in cls_dict:
                if cls_dict[name] is MAGIC_FIELD:
                    field_names.append(name)
                else:
                    other_attrs.append(name)
            tuple_cls = cls.cache[cls.__name__] = namedtuple(cls.__name__, field_names)
            for name in other_attrs:
                setattr(tuple_cls, name, cls_dict[name])
        return tuple_cls(*args)
