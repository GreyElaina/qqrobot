import random
from mymain import *

@myMain
def main(g,q,m):
    return random.choice(m.split(' ')) if len(m) else '参数错误'