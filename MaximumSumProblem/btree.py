# -*- coding: utf-8 -*-
from collections import Iterable
import networkx as nx
import matplotlib.pyplot as plt


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value   # 节点的值
        self.left = left     # 左子节点
        self.right = right   # 右子节点


class BinaryTree:

    def __init__(self, seq=()):
        assert isinstance(seq, Iterable)
        self.root = None
        # self.insert(*seq)

    def __insert__(self, *args):
        if not args:
            return
        if not self.root:
            self.root = Node(args[0])
            args = args[1:]
        for i in args:
            seed = self.root
            while True:
                if i > seed.value:
                    if not seed.right:
                        node = Node(i)
                        seed.right = node
                        break
                    else:
                        seed = seed.right
                else:
                    if not seed.left:
                        node = Node(i)
                        seed.left = node
                        break
                    else:
                        seed = seed.left

    def insert(self, root):
        self.root = root

    def find(self, item, seed=None):
        node = seed or self.root   # 修改查询起点
        parent = None              # 父节点
        while node:
            if item > node.value:
                parent, node = node, node.right
            elif item < node.value:
                parent, node = node, node.left
            else:
                return (node, parent)

    def minNode(self, seed=None):
        node = seed or self.root
        while node.left:
            node = node.left
        return node

    def maxNode(self, seed=None):
        node = seed or self.root
        while node.right:
            node = node.right
        return node

    def remove(self, item):
        result = self.find(item)
        if result:
            new_node = None  # 替换 A 的节点
            del_node, del_node_parent = result
            if del_node.value == self.root.value:
                raise ValueError('can not remove root')  # 根节点固定
            if del_node.left and del_node.right:
                right_min = self.minNode(seed=del_node.right)
                new_node = Node(right_min.value)

                # 当 A 节点的右子树节点没有子节点时，临时节点的右子节点 为 None
                if del_node.right.value == new_node.value:
                    new_node.left = del_node.left
                else:
                    new_node.left, new_node.right = del_node.left, del_node.right
                self.remove(right_min.value)
                # A 节点的父节点与临时节点关联

            elif del_node.left or del_node.right:
                new_node = del_node.left or del_node.right

            if del_node_parent.left and del_node_parent.left.value == del_node.value:
                del_node_parent.left = new_node
            elif del_node_parent.right and del_node_parent.right.value == del_node.value:
                del_node_parent.right = new_node
            del del_node
            return
        raise ValueError('item not in tree')


def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.value] = (x, y)
    if node.left:
        G.add_edge(node.value, node.left.value)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.value, node.right.value)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)


def draw(node):   # 以某个节点为根画图
    graph = nx.Graph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
    print(pos)
    nx.draw_networkx(graph, pos, ax=ax, node_size=800, node_color=['green', 'yellow'])
    plt.show()


def convert2graph(parent, arr, i):
    # if 2 * i + 1 >= len(arr) or 2 * i + 2 >= len(arr):
    #     return
    if i >= int((len(arr) - 1) / 2):
        return
    if not parent.left:
        node = Node(arr[2 * i + 1])
        parent.left = node
        convert2graph(parent.left, arr, 2 * i + 1)

    if not parent.right:
        node = Node(arr[2 * i + 2])
        parent.right = node
        convert2graph(parent.right, arr, 2 * i + 2)


if __name__ == '__main__':
    li = [40, 20, 30, 70, 60, 75, 71]
    root = Node(li[0])
    convert2graph(root, li, 0)
    tree = BinaryTree()
    tree.insert(root)
    draw(tree.root)
