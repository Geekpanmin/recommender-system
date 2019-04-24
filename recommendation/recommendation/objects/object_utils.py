import uuid
from collections import Iterable

import numpy as np


class ObjectMetaClass(type):
    """ 使用目的为了处理__slot__，增加与对应table相同的to_dict方法"""

    @classmethod
    def __prepare__(mcs, name, bases):
        """必返回dict，__new__最后一个参数_"""
        return dict()

    def __new__(mcs, class_name, class_parents, class_attr):
        column_keys = class_attr["__basetable__"].__table__.columns.keys()
        _slots_ = [k for k in class_attr["_slots_"]] if "_slots_" in class_attr else []
        _slots_ += [k for k in column_keys if k not in class_attr]  # 跳过property属性

        def to_dict(self):
            dic = {}
            for k in column_keys:
                if '__{}'.format(k) in _slots_:
                    v = getattr(self, '_{}__{}'.format(class_name, k), None)
                else:
                    v = getattr(self, k, None)
                if isinstance(v, np.ndarray):
                    v = v.tolist()  # ndarray to list
                elif isinstance(v, uuid.UUID):
                    v = str(v)  # UUID to str
                dic[k] = v
            return dic

        class_attr['to_dict'] = to_dict
        # class_attr['__slots__'] = tuple(_slots_)  # 省内存，速度； 限制实例object能动态绑定的属性名称 TODO(恢复)
        del class_attr['_slots_']
        del class_attr["__basetable__"]
        return type.__new__(mcs, class_name, class_parents, class_attr)

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)


class Obj(object):
    def __init__(self, d):
        """
        :type d: dict
        """
        for key, value in d.items():
            if isinstance(value, (list, tuple, set)):
                setattr(self, key, [Obj(v) if isinstance(v, dict) else v for v in value])
            else:
                setattr(self, key, Obj(value) if isinstance(value, dict) else value)

    def to_dict(self):
        return todict(self)


def todict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif isinstance(obj, (list, set, tuple)):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey))
                     for key, value in obj.__dict__.items()
                     if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    elif isinstance(obj, Iterable):  # 针对各种封装过的sequence类型，google protobuf
        return [todict(v, classkey) for v in obj]
    else:
        return obj
