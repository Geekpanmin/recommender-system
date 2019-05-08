import os
# pprint = p.PrettyPrinter(indent=2)
import pprint
# import pprint as p
import sys

import jieba
from gensim.models import word2vec

cur_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(cur_dir))
sys.path.append(root_dir)
from config import data_dir


def read_poems():
    with open(os.path.join(data_dir, "poems.txt"), "r", encoding="utf-8") as f:
        lines = [line.strip().replace(" ", '') for line in f]
    return "".join(lines)


def prepare():
    with open(os.path.join(data_dir, "train.txt"), "w", encoding="utf-8") as f_train:
        with open(os.path.join(data_dir, "poems.txt"), "r", encoding="utf-8") as f:
            for line in f:
                seg_list = jieba.cut(line)
                # seg_list = line.split()
                f_train.write(" ".join(seg_list) + "\n")


def train():
    # 加载语料
    sentences = word2vec.Text8Corpus(os.path.join(data_dir, "train.txt"))
    # 训练模型
    model = word2vec.Word2Vec(sentences)
    # 保存模型
    model.save('poem.model')
    # 选出最相似的10个词
    for e in model.most_similar(positive=['春'], topn=10):
        print(e[0], e[1])


def main():
    poem = read_poems()
    from collections import Counter
    res = Counter(poem).most_common(100)
    pprint.pprint(res)


if __name__ == "__main__":
    # main()
    # exit(1)
    # prepare()
    # train()
    # 加载模型
    model = word2vec.Word2Vec.load('poem.model')
    for word in ["春", '思乡', "梅", "冬", "中秋"]:
        res = model.most_similar(positive=[word], topn=10)
        print(word)
        pprint.pprint(res)
        print("-" * 10)
