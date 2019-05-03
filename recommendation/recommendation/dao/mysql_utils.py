from recommendation.dao.db import DB
from recommendation.dao.db_tools import try_commit_rollback_expunge
from recommendation.dao.models.mysql_models import User, Poem, Poet, History


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
    def get_all_poets(self):
        poets = self.session.query(Poet).limit(1000).all()
        return poets

    @try_commit_rollback_expunge
    def get_user_history(self, user_id):
        historys = self.session.query(History).filter_by(user_id=user_id).all()
        history_poem_ids = []
        if historys:
            history_poem_ids = [history.poem_id for history in historys]
        return history_poem_ids

    def record_to_history(self, user_id, result_poems):
        history = History(user_id=user_id, poem_id=result_poems)
