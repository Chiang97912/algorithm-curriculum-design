# -*- coding: utf-8 -*-
# @Author: Peter
# @Date:   2019-01-02 18:42:01
# @Last Modified by:   Peter
# @Last Modified time: 2019-01-05 13:58:31
# coding=utf-8
import sys
import csv
from bs4 import BeautifulSoup


def DrawBlockMap(file_name):
    reader = csv.reader(open(file_name, 'r', encoding='utf-8'), delimiter=",")
    svg = open('jsmap.svg', 'r', encoding='utf-8').read()  # 读取江苏省地图数据
    Price = {}
    price_only = []  # 记录各市的数值
    sort_value = []  # 记录
    sort_no = []  # 记录各市的排名
    for row in reader:  # 遍历读取的文件每一行
        try:
            temp = row[0]  # 序号
            price = float(row[1].strip())  # 价格
            Price[temp] = price
            price_only.append(price)
            sort_value.append(price)
        except:
            pass
    sort_value.sort()  # 对所有数值默认升序排序，计算记录各市的排名
    for i in range(len(price_only)):
        for j in range(len(sort_value)):
            if (price_only[i] == sort_value[j]):
                sort_no.append(j)  # 记录当前排名
                break
    soup = BeautifulSoup(svg, "lxml")
    paths = soup.findAll('path')
    # 颜色列表
    colors = ["#FFD0E7", "#FFA0D0", "#FF71B8", "#FF41A0", "#FF1288", "#E10071",
              "#B20059", "#720039", "#620031", "#510029", "#410021", "#310018", "#210010"]
    path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
    count = 0
    for p in paths:
        try:
            color_class = sort_no[count]  # 根据排名染不同的颜色，排名越前说明值越小，所以颜色越浅
            count += 1
        except:
            continue
        color = colors[color_class]
        p['style'] = path_style + color  # 改变地图对应区域的颜色
    print(soup.prettify())


if __name__ == '__main__':
    DrawBlockMap("value.txt")
