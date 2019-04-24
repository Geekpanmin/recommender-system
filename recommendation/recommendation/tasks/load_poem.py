import json
import os
from recommendation.dao.models.mysql_models import Poet, Poem
from config import data_dir

gushiwenwang = os.path.join(data_dir, "poetry-master")

from recommendation.dao.mysql_utils import MysqlDB


class Task(object):
    def __init__(self):
        self.mysql_db = MysqlDB()

    def load_gushiwenwang_poet(self):
        gushiwenwang_poet = os.path.join(gushiwenwang, "poet")
        count = 0
        for poet_fname in os.listdir(gushiwenwang_poet):
            with open(os.path.join(gushiwenwang_poet, poet_fname), "r", encoding="utf-8") as f:
                poet_json = json.load(f)
            print(poet_json)
            poet_dict = {"id": poet_json["id"], "name": poet_json["name"], "dynasty": poet_json.get("dynasty", ""),
                         "image": poet_json.get("image", ""), "star": poet_json["star"], "source": "gushiwen.org",
                         "description": poet_json["desc"], "about": poet_json.get("content", "")}
            self.mysql_db.session.add(Poet(**poet_dict))
            count += 1
            if count % 1000:
                self.mysql_db.session.commit()
        self.mysql_db.session.commit()

    def load_gushiwenwang_poetry(self):
        gushiwenwang_poetry = os.path.join(gushiwenwang, "poetry")
        # i = 0
        for poetry_fname in os.listdir(gushiwenwang_poetry):
            with open(os.path.join(gushiwenwang_poetry, poetry_fname), "r", encoding="utf-8") as f:
                poetry_json = json.load(f)
            # print(poetry_json)
            poem_dict = {"type": 0, "name": poetry_json["name"],
                         "dynasty": poetry_json["dynasty"],
                         "poet_name": poetry_json["poet"]["name"], "poet_id": poetry_json["poet"]["id"],
                         "picture": "", "content": poetry_json["content"],
                         "strains": "", "fanyi": poetry_json.get("fanyi", ""),
                         "shangxi": poetry_json.get("shangxi", ""),
                         "star": poetry_json["star"], "source": "gushiwen.org"}
            self.mysql_db.session.add(Poem(**poem_dict))
            try:
                self.mysql_db.session.commit()
            except:
                self.mysql_db.session.rollback()
                import traceback
                print(traceback.format_exc())
            # i += 1
            # if i % 1000:
            #     self.mysql_db.session.commit()
        self.mysql_db.session.commit()

    def load_(self):
        pass

    def run(self):
        # self.load_gushiwenwang_poet()
        self.load_gushiwenwang_poetry()
