from recommendation.algorithms.matching import Matching
from recommendation.algorithms.ranking import Ranking
from recommendation.algorithms.recall.rule_base import RuleBase

from recommendation.dao.mysql_utils import MysqlDB
from recommendation.objects import User
from recommendation.utils.view_helper import ViewFeed


class Recommender(object):
    """组合各推荐算法计算结果"""

    def __init__(self):
        self.db = MysqlDB()
        self.matching = Matching()
        self.ranking = Ranking()
        self.rule_base = RuleBase()
        self.view_help = ViewFeed()

    def recommend(self, user_id, num=10):
        result_feeds = self.do_recommend(user_id, num)
        return result_feeds[:num]

    # @show_runtime
    def do_recommend(self, user_id, num=10):
        ws_user = self.db.get_user_info(user_id)
        user = User(**ws_user.to_dict()) if ws_user is not None else User(id=user_id)
        matched_poems = self.matching.concurrent_match(user, num=max(num * 5, 100))  # 初步筛选,最少100，原因是user_id过滤
        result_poems = self.ranking.rank(user, num=num, matched_poems=matched_poems)  # 进一步排序,组合多算法结果
        # self.view_help.print_result_feeds(result_feeds)  # 输出推荐视频详细信息，线上注释
        return result_poems
