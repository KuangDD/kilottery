# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/8/10
"""
play_3d
模拟开奖
1. 单次开奖
    * 单注成本
    * 中奖规则
    * 中奖金额

2. 多次开奖
    * 成本
    * 中奖金额
"""
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(Path(__name__).stem)

import os
import re
import json
import shutil
import collections as clt
from functools import partial
from multiprocessing.pool import Pool

import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt

from parse_xlsx import parse_lottery_ticket

# data_3d = parse_lottery_ticket(lottery_type='3d', number_of_numbers=3)
# np.savetxt('data/data_3d.txt', data_3d, fmt='%d')
data_3d = np.loadtxt('data/data_3d.txt', dtype=int)


class Match3D():
    def __init__(self):
        pass

    def judge(self, src, dst):
        if all([s == d for s, d in zip(src, dst)]):
            return 1
        else:
            return 0

    def reward(self, flag):
        if flag == 1:
            return 1000
        else:
            return 0

    def cost(self):
        return 2

    def earn(self, src, dst):
        flag = self.judge(src=src, dst=dst)
        out = self.reward(flag) - self.cost()
        return out


from sklearn.linear_model.logistic import LogisticRegression
from sklearn.metrics import accuracy_score


class Predict3D():
    def __init__(self):
        self.data = np.loadtxt('data/data_3d.txt', dtype=int)

    def predict(self, index):
        return self.data[index]
        # return np.random.choice(list(range(10)), 3, replace=False)

    def split(self):
        X, y = [], []
        for line in self.data.T:
            for idx in range(len(line) - 100):
                X.append(line[idx: idx + 10])
                y.append(line[idx + 10])
        return X, y

    def method(self):
        lr = LogisticRegression()
        X, y = self.split()
        lr.fit(X, y)
        y_pred = lr.predict(X)
        print(accuracy_score(y, y_pred))


class Target3D():
    def __init__(self):
        self.data = np.loadtxt('data/data_3d.txt', dtype=int)

    def target(self, index):
        return self.data[index]


class BetHandler():

    def __init__(self, match_class, predict_class, target_class):
        self.match_class = match_class
        self.predict_class = predict_class
        self.target_class = target_class

    def bet_one(self, index):
        src = self.predict_class.predict(index)
        dst = self.target_class.target(index)
        out = self.match_class.earn(src=src, dst=dst)
        return out

    def bet_many(self, index_list):
        return sum([self.bet_one(i) for i in index_list])


if __name__ == "__main__":
    print(__file__)
    bet_handler = BetHandler(match_class=Match3D(), predict_class=Predict3D(), target_class=Target3D())
    print(bet_handler.bet_many(range(100)))
    bet_handler.predict_class.method()
