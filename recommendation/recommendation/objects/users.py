from recommendation.dao.models.mysql_models import User as UserModel
from recommendation.dao.mysql_utils import MysqlDB
from recommendation.objects.object_utils import ObjectMetaClass


class User(metaclass=ObjectMetaClass):
    __basetable__ = UserModel  # 字段名必须与此表对应，所有属性若不在表中，必须写在_slots_
    _slots_ = ("__history")  # 省内存，速度

    def __init__(self, id=None, **kwargs):
        self.id = id
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.__history = None

    @property
    def history(self):
        if self.__history is None:
            self.__history = set(MysqlDB().get_user_history(self.id))
        return self.__history
