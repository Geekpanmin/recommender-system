import datetime
import time
from functools import wraps

from recommendation.dao.memory import Memory


class ViewFeed(object):
    def __init__(self):
        self.group_size = 10
        self.memory = Memory()

    def print_result_feeds(self, result_feeds):
        """ 简单输出所有VideoResult相关信息
        :param result_feeds: list of ResultFeed Object
        :return: None
        """
        for index, result_feed in enumerate(result_feeds):
            if result_feed.feed_id not in self.memory.all_poems_dict:
                print(("not in memory , feed_id:*{}, score: {}, match_algorithm:{}, rank_algorithm:{} ")
                      .format(1 + index, result_feed.feed_id, result_feed.score, result_feed.match_algorithm,
                              result_feed.rank_algorithm))
                continue  # 视频不在内存
            video_feed = self.memory.all_poems_dict[result_feed.feed_id]
            days = (datetime.datetime.now() - video_feed.create_time).days
            ss = ("*{}, days: {}, feed_id: {}, user_id:{}, upi: {}, \n"
                  "view_count:{}, like_count:{}, is_feature: {}, score: {}, match_algorithm:{}, rank_algorithm:{}\n\n"
                  ).format(1 + index, days, video_feed.id, str(video_feed.user_id), video_feed.upi,
                           video_feed.view_count, video_feed.like_count, video_feed.is_feature,
                           result_feed.score, result_feed.match_algorithm, result_feed.rank_algorithm)
            print(ss)
        print("**" * 100)


def show_runtime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print("*** function: {}, take time: {:.4}s".format(func.__name__, t2 - t1))
        return res

    return wrapper
