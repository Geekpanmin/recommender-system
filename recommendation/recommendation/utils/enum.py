from collections import OrderedDict

__all__ = ["Enum"]


class _EnumDict(dict):
    def __init__(self):
        super(_EnumDict, self).__init__()
        self._member_names = []

    def __setitem__(self, key, value):
        if key[0] != '_':
            self._member_names.append(key)
        super(_EnumDict, self).__setitem__(key, value)


class EnumMeta(type):

    @classmethod
    def __prepare__(mcs, cls, bases):
        return _EnumDict()

    def __new__(mcs, cls, bases, dct):
        members = {k: dct[k] for k in dct._member_names}
        _member_names_ = dct._member_names
        [dct.pop(name) for name in dct._member_names]
        # create our new Enum type
        enum_class = super(EnumMeta, mcs).__new__(mcs, cls, bases, dct)
        enum_class._member_names_ = _member_names_  # names in definition order
        enum_class._member_map_ = OrderedDict()  # name->value map

        # Reverse value->name map for hashable values.
        enum_class._key2member_map_ = {}
        enum_class.lists = []

        for name, _value in members.items():
            if isinstance(_value, tuple):
                key, value = _value[0], _value[1]
            else:
                key, value = _value, ''
            enum_member = enum_class()
            enum_member._name_ = name
            enum_member._key_ = key
            enum_member._value_ = value
            # now add to _member_map_
            enum_class._member_map_[name] = enum_member
            enum_class._key2member_map_[key] = enum_member
            enum_class.lists.append([key, value])

        return enum_class

    def __delattr__(cls, attr):
        if attr in cls._member_map_:
            raise AttributeError("{}: cannot delete Enum member.".format(cls.__name__))
        super(EnumMeta, cls).__delattr__(attr)

    def __setattr__(cls, name, value):
        member_map = cls.__dict__.get('_member_map_', {})
        if name in member_map:
            raise AttributeError('Cannot reassign members.')
        super(EnumMeta, cls).__setattr__(name, value)

    def __getattr__(cls, name):
        try:
            enum_member = cls._member_map_[name]
            return enum_member._key_
        except KeyError:
            raise AttributeError(name)

    def __getitem__(cls, key):
        return cls._key2member_map_[key]._value_

    def __iter__(cls):
        return ((cls._member_map_[name]._key_,
                 cls._member_map_[name]._value_) for name in cls._member_names_)

    def __reversed__(cls):
        return (cls._member_map_[name] for name in reversed(cls._member_names_))

    def __len__(cls):
        return len(cls._member_names_)

    def __contains__(cls, value):
        return value in cls._key2member_map_

    def __dir__(self):
        return list(super(EnumMeta, self).__dir__()) + self._member_names_


class Enum(metaclass=EnumMeta):
    def __repr__(self):
        return "<{}.{}: {}>".format(self.__class__.__name__, self._name_, self._value_)

    def __str__(self):
        if self._value_:
            return "{}.{}({})".format(self.__class__.__name__, self._name_, self._value_)
        return "{}.{}".format(self.__class__.__name__, self._name_)


# class Demo(Enum):
#     # name key value
#     name = ("KEY", 0.5)
#     name2 = "KEY2"  # default value=''
#
#
# key, key2 = Demo.name, Demo.name2
# print("key: {} ,key2: {}\n".format(key, key2))
#
# value, value2 = Demo["KEY"], Demo["KEY2"]
# print("value: {}, value2: {}\n".format(value, value2))
#
# for key, value in Demo:  # 按属性顺序循环
#     print("key: {}, value: {}".format(key, value))
