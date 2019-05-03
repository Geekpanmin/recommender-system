import time
from collections import Counter
from functools import wraps

from recommendation.algorithms.common.constants import MatchAlgorithmEnum
from recommendation.dao.memory import Memory
from recommendation.utils.tools import try_catch_with_logging


class ViewFeed(object):
    def __init__(self):
        self.group_size = 5
        self.memory = Memory()

    @try_catch_with_logging(default_response=None)
    def print_result_poems(self, result_poems, num):
        """ 简单输出所有VideoResult相关信息
        :param result_poems: list of ResultPoem Object
        :return: None
        """
        for index, result_poem in enumerate(result_poems):
            if result_poem.poem_id not in self.memory.all_poems_dict:
                print(("not in memory , poem_id:*{}, score: {}, match_algorithm:{}, rank_algorithm:{} ")
                      .format(1 + index, result_poem.poem_id, result_poem.score, result_poem.match_algorithm,
                              result_poem.rank_algorithm))
                continue  # 视频不在内存
            poem = self.memory.all_poems_dict[result_poem.poem_id]
            ss = (
                f"poem_id: {result_poem.poem_id}, match_algorithm:{result_poem.match_algorithm}, rank_algorithm:{result_poem.rank_algorithm}\n"
                f"title:{poem.name},poet:{poem.poet_name},dynasty:{poem.dynasty},star:{poem.star}\n"
                f"match_tags:{result_poem.reasons}\n"
            )
            print(ss)
            # pprint(result_poem)
        expectation = {_algorithm: int(num * _proportion) for _algorithm, _proportion in MatchAlgorithmEnum}
        reality = Counter([_result_poem.match_algorithm for _result_poem in result_poems]).most_common()
        print(f"expectation: {expectation}")
        print(f"reality: {reality}")
        print("**" * 10)


def show_runtime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print("*** function: {}, take time: {:.4}s".format(func.__name__, t2 - t1))
        return res

    return wrapper
