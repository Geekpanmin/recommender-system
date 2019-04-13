import argparse
import os

from recommendation.utils.logger import logging_config


def deploy():
    from recommendation.dao.models.mysql_models import create_all
    create_all()


def recommend():
    logging_config("recommend.log")


def test():
    import unittest
    tests = unittest.TestLoader().discover("tests", pattern="test_recommend*")
    unittest.TextTestRunner().run(tests)


def main():
    ''' Parse command line arguments and execute the code'''
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)  # 一组互斥参数,且至少需要互斥参数中的一个
    group.add_argument('--test', '-t', action="store_true")
    parser.add_argument('--runtime', default="prod", type=str, choices=["prod", "local"])
    # parse args
    args = parser.parse_args()
    os.environ['runtime'] = args.runtime

    if args.test:
        test()
    else:
        recommend()


if __name__ == '__main__':
    main()
