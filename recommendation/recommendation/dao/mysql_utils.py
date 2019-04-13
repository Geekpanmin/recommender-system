from recommendation.dao.db import DB
from recommendation.dao.db_tools import try_commit_rollback_expunge
from recommendation.dao.models.mysql_models import User


class MysqlDB(DB):
    def __init__(self):
        super().__init__()

    @try_commit_rollback_expunge
    def get_ws_video_info(self, user_id):
        ws_video = self.session.query(User).filter_by(id=user_id).first()
        return ws_video
