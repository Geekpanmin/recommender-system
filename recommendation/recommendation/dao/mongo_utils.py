from recommendation.dao.db import Mongo
from recommendation.dao.models.mongo_models import Poem, Ci


class MongoDB(Mongo):
    def get_poems(self, days):
        Poem.objects().first()

    def get_ci(self, days):
        Ci.objects().all()
