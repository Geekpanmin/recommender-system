"""基于规则的推荐"""

from recommendation.algorithms.common.constants import MatchAlgorithmEnum
from recommendation.dao.memory import Memory
from recommendation.dao.mysql_utils import MysqlDB
from recommendation.utils.tools import try_catch_with_logging
from recommendation.objects import ResultPoem


class RuleBase(object):
    def __init__(self):
        self.memory = Memory()
        self.mysql_db = MysqlDB()

    @try_catch_with_logging(default_response=[])
    def get_popular_poems(self, user=None, num=None):
        """
        :type user: User Object
        :type num int 返回数目
        :return:  list of ResultFeed Object
        """
        result_poems = [ResultPoem(poem_id, MatchAlgorithmEnum.rule_base, MatchAlgorithmEnum.rule_base, 0)
                        for poem_id in self.memory.popular_poem_ids[:num]]
        return result_poems
