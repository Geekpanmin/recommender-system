from recommendation.dao.db import Mongo
from recommendation.dao.models.mongo_models import Poem, Ci


class MongoDB(Mongo):
    def get_poems(self, days):
        Poem.objects().first()

    def get_ci(self, days):
        Ci.objects().all()

    def save_poem(self, poem):
        Poem(**poem).save()  # 新建

    def save_ci(self, ci):
        Ci(**ci).save()  # 新建
