# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/8/7
"""
play_ssq

模拟双色球开奖。

1.每个数字的出现概率。
2.在前一个出现A的条件下，后一个出现B的条件概率。
3.如果这些数字是汉字，最可能是什么字。
4.如果这些数字是字母，最可能是什么字母。
5.如果这些数字是颜色，最可能是什么颜色。
6.这些数字和当天老黄历有没一点关系。
7.如果这些数字是音符，最可能是什么音符。
8.声音信号看起来也是上下无规律波动，这个和这些数字有相似。
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

if __name__ == "__main__":
    print(__file__)