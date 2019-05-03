from recommendation.dao.memory import Memory
from recommendation.dao.models.mysql_models import Poem as PoemModel, Poet as PoetModel
from recommendation.objects.object_utils import ObjectMetaClass


class Poem(metaclass=ObjectMetaClass):
    __basetable__ = PoemModel  # 字段名必须与此表对应，所有属性若不在表中，必须写在_slots_
    _slots_ = ()  # 省内存，速度

    def __init__(self, id=None, **kwargs):
        self.id = id
        for k, v in kwargs.items():
            setattr(self, k, v)


class Poet(metaclass=ObjectMetaClass):
    __basetable__ = PoetModel  # 字段名必须与此表对应，所有属性若不在表中，必须写在_slots_
    _slots_ = ()  # 省内存，速度

    def __init__(self, id=None, **kwargs):
        self.id = id
        for k, v in kwargs.items():
            setattr(self, k, v)


class ResultPoem(object):
    memory = Memory()

    def __init__(self, poem_id, match_algorithm, rank_algorithm, score, type=0, reasons=None):
        """
        :param poem_id: str
        :param match_algorithm: str
        :param rank_algorithm: str
        :param score: float
        :param type: int
        :param reasons: dict {"tags":["tag_1","tag_2"],""}
        """
        self.poem_id = poem_id
        self.match_algorithm = match_algorithm
        self.rank_algorithm = rank_algorithm
        self.score = score
        self.type = type
        self.reasons = reasons

    def to_dict(self):
        recommend = {"poem_id": self.poem_id, "match_algorithm": self.match_algorithm,
                     "rank_algorithm": self.rank_algorithm, "score": self.score, "type": self.type,
                     "reasons": self.reasons}
        poem = self.memory.all_poems_dict[self.poem_id]
        poet_name = ""
        if poem.poet_id in self.memory.all_poets_dict:
            poet_name = self.memory.all_poets_dict[poem.poet_id].name
        poem = {"title": poem.name, "content": poem.content.replace("<br>", "\n").split("\n"),
                "dynasty": poem.dynasty,
                "tags": list(poem.tags),
                "poet": poet_name}
        data = {"poem": poem, "recommend": recommend}
        return data
