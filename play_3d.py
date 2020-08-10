# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/8/10
"""
play_3d
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

print('number:', len(data_3d))

strs = [v for w in data_3d for v in f'{w[0]}{w[1]}{w[2]}']

ctdt = clt.Counter(strs)
outdt = clt.defaultdict(int)
for k, v in ctdt.items():
    outdt[v] += 1

out = clt.Counter(outdt).most_common()
print(out)

if __name__ == "__main__":
    print(__file__)