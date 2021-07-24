import os
from jqdatasdk import *
pd.set_option('display.max_columns', None)

# 设置全局变量
data_root = "/Users/zhongbo/PycharmProjects/pythonProject1/DelatTrader/data/"


def get_stock_list():
    """
    获取所有A股列表
    :return: stock_list
    """
