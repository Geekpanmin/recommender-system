import logging

from local_config import LocalConfig
from recommendation import create_app
from recommendation.preprocessor import Preprocessor
from recommendation.recommender import Recommender
from recommendation.utils.logger import logging_config

logging_config('./recommend.log', relative_path="..")

log_str = "\n** Runtime : {}".format(LocalConfig.runtime)
logging.info(log_str)
print(log_str)

recomender = Recommender()

app = create_app()  # 运行环境

# 初始化
Preprocessor().run(app)

if __name__ == '__main__':
    app.run()
