import argparse

from recommendation.utils.logger import logging_config


def deploy():
    from recommendation.dao.models.mysql_models import create_all
    create_all()


def task():
    logging_config("task.log")
    from recommendation.tasks.load_poem import PoemTask
    from recommendation.tasks.tasks import TagTask
    # PoemTask().run()
    # TagTask().run()
    TagTask().create_fake_history()


def test():
    import unittest
    tests = unittest.TestLoader().discover("tests", pattern="test_recommend*")
    unittest.TextTestRunner().run(tests)


def main():
    ''' Parse command line arguments and execute the code'''
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)  # 一组互斥参数,且至少需要互斥参数中的一个
    group.add_argument('--test', '-t', action="store_true")
    group.add_argument('--task', action="store_true")
    # parse args
    args = parser.parse_args()

    if args.test:
        test()
    elif args.task:
        task()


if __name__ == '__main__':
    deploy()
    task()
    # main()
