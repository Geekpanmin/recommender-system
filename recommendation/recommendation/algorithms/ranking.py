"""
Ranking阶段对Matching后的视频采用更精细的特征计算user-item之间的排序分，作为最终输出推荐结果的依据。
"""

from recommendation.dao.memory import Memory


class Ranking(object):
    def __init__(self):
        self.group_size = 5
        self.memory = Memory()

    def rank(self, user, num, matched_poems, rank_algorithm=None):
        """
        :param user: User Object
        :param matched_videos: list of VideoResult Object
        :param rank_algorithm: [("CB",1), ("RB",0.3), ("TB",0.1), ("UC",0), ("IC",0), ("FB",0)]；指定排序算法
        :return: list of VideoResult Object
        """
        if user is None:
            return matched_poems
        ranked_poems = self.rank_score(user=user, matched_poems=matched_poems)  # rank策略暂时不用
        return ranked_poems

    def rank_score(self, user, matched_poems):
        """
        :param user: User Object
        :param matched_videos: list of VideoResult
        :return: list of VideoResult
        """

        return matched_poems
