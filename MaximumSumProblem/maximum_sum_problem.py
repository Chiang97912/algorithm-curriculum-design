# -*- coding: utf-8 -*-
# @Author: Peter
# @Date:   2019-01-01 22:53:54
import networkx as nx
import matplotlib.pyplot as plt


def get_path(score):
    """

    利用回溯法求路径

    Arguments:
        score {[type]} -- [description]

    Returns:
        list -- 使得总和最大的路径
    """
    path = []
    n = len(score)
    path.append((0, 0))

    j = 0
    for i in range(n - 1):
        if score[i + 1][j] > score[i + 1][j + 1]:
            path.append((i + 1, j))
            i += 1
        else:
            path.append((i + 1, j + 1))
            i += 1
            j += 1
    return path


def msp(value):
    """

    maximum sum problem

    Arguments:
        value {list} -- 数字三角形

    Returns:
        list -- 解
    """
    n = len(value)
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        d[n - 1][i] = value[n - 1][i]

    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            d[i][j] = value[i][j] + max(d[i + 1][j], d[i + 1][j + 1])

    return d


def read_data():
    """

    读取数据

    Returns:
        list -- 数字三角形矩阵
    """
    n = int(input('请输入三角形底边数目:'))
    print(n)
    d = [[0] * n for _ in range(n)]
    print('请输入各节点的数：')
    for i in range(1, n + 1):
        flag = 0
        inputs = input().split(' ')
        for j in range(1, n + 1):
            if j <= i:
                d[i - 1][j - 1] = int(inputs[flag])
                flag += 1
    return d


def display_matrix(a):
    """

    打印矩阵

    Arguments:
        a {list} -- 二维矩阵
    """
    for item in a:
        print("\t".join([str(i) for i in item]))


def create_graph(G, matrix):
    """

    利用数字三角形矩阵创建networkx图

    Arguments:
        G {networkx.classes.graph.Graph} -- networkx内置对象
        matrix {nested list} -- 数字三角形
    """
    pos = {}
    n = len(matrix)
    pos[0] = (n + 1, -1)

    for i in range(n):
        for j in range(i + 1):
            G.add_node(n * i + j, value=matrix[i][j])

    for i in range(n - 1):
        for j in range(i + 1):
            parent = n * i + j
            left = n * (i + 1) + j
            right = n * (i + 1) + j + 1

            left_i, left_j = i + 1, j
            right_i, right_j = i + 1, j + 1
            pos[left] = (n - left_i + 2 * left_j + 1, -(left_i + 1))
            G.add_edge(parent, left)

            pos[right] = (n - right_i + 2 * right_j + 1, -(right_i + 1))
            G.add_edge(parent, right)

    return (G, pos)


def view(matrix, path):
    """

    可视化界面

    Arguments:
        matrix {nested list} -- 数字三角形
        path {list} -- 最佳路径
    """
    n = len(matrix)
    colors = []
    for i in range(n):
        for j in range(i + 1):
            colors.append('b')
            # if (i, j) in path:
            #     colors.append('b')
            # else:
            #     colors.append('r')
    graph = nx.Graph()
    graph, pos = create_graph(graph, matrix)
    fig, ax = plt.subplots(figsize=(10, 8))  # 比例可以根据树的深度适当调节z
    labels = {}
    for i in graph:
        labels[i] = graph.node[i]['value']
    nx.draw(graph, pos, font_size=20, node_size=2000, node_color=colors, node_shape='s', with_labels=False)
    # nx.draw_networkx(graph, pos, ax=ax, node_size=800, node_color=colors, node_shape='s', with_labels=False)
    nx.draw_networkx_labels(graph, pos, labels)  # 添加标签
    # plt.draw()
    plt.pause(3)
    plt.clf()
    plt.xticks([])  # 去掉横坐标值
    plt.yticks([])  # 去掉纵坐标值
    # plt.show()

    k = len(colors) - 1
    # for i in range(n):
    #     for j in range(i + 1):
    for i in range(n - 1, -1, -1):
        for j in range(i, -1, -1):
            if (i, j) in path:
                colors[k] = 'r'
                nx.draw(graph, pos, font_size=20, node_size=2000, node_color=colors, node_shape='s', with_labels=False)
                nx.draw_networkx_labels(graph, pos, labels)  # 添加标签
                plt.draw()
                plt.pause(1.5)
                plt.clf()
            k -= 1
    plt.show()


if __name__ == '__main__':
    triangle = read_data()
    display_matrix(triangle)
    score = msp(triangle)
    path = get_path(score)
    print("路径：", path)
    print("得分矩阵:")
    display_matrix(score)
    print("结果：", score[0][0])
    view(triangle, path)
