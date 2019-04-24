from recommendation.dao.db import DB
from recommendation.dao.db_tools import try_commit_rollback_expunge
from recommendation.dao.models.mysql_models import User, Poem


class MysqlDB(DB):
    def __init__(self):
        super().__init__()

    @try_commit_rollback_expunge
    def get_user_info(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        return user

    @try_commit_rollback_expunge
    def get_all_poems(self):
        poems = self.session.query(Poem).limit(100).all()
        return poems

    @try_commit_rollback_expunge
    def get_user_history(self, user_id):
        return []
