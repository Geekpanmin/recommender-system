import logging
import time

import numpy as np

from recommendation.algorithms.common.bases import largest_indices
from recommendation.dao.memory import Memory
from recommendation.dao.mysql_utils import MysqlDB
from recommendation.objects import Poem
from recommendation.utils.tools import synchronized


class Preprocessor(object):

    def __init__(self):
        self.memory = Memory()
        self.mysql_db = MysqlDB()

    @synchronized
    def load_all_feeds(self):
        """所有视频载入内存"""
        all_poems = self.mysql_db.get_all_poems()  # 2s
        assert len(all_poems) > 0
        self.memory.all_poems_dict = {_poem.id: Poem(**_poem.to_dict()) for _poem in all_poems}  # 1.5s
        self.memory.all_poem_ids = list(self.memory.all_poems_dict.keys())
        self.memory.popular_poem_ids = self.get_popular_poem_ids(1000)
        log_str = '*** load {} feeds to memory'.format(len(self.memory.all_poems_dict))
        print(log_str)
        logging.info(log_str)

    def get_popular_poem_ids(self, num):
        """视频按照流行程度popular_index排序载入内存,0.023"""
        poem_stars = [self.memory.all_poems_dict[poem_id].star for poem_id in self.memory.all_poem_ids]
        ordered_top_n_star = largest_indices(np.asarray(poem_stars), min(num, len(poem_stars)))
        popular_poem_ids = [self.memory.all_poem_ids[index] for index in ordered_top_n_star]
        return popular_poem_ids

    @synchronized
    def task(self, app):
        app.app_context().push()
        while True:
            self.load_all_feeds()
            time.sleep(5 * 60)

    def run(self, app):
        from threading import Thread
        t = Thread(target=self.task, args=[app])
        t.start()
