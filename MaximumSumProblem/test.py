import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
G.add_node(1, value=80)
G.add_node(2, value=100)
G.add_node(3, value=50)
G.add_node(4, value=100)
G.add_node(5, value=150)
G.add_node(6, value=100)
G.add_node(7)
G.add_node(8)
G.add_edges_from([(1, 2), (2, 3), (2, 4), (1, 6), (6, 5)])

# change the value of nodes
for i in G:
    if 'value' in G.node[i]:
        # do something?
        continue
    else:
        G.node[i]['value'] = 200


labels = {}
for i in G:
    labels[i] = G.node[i]['value']
pos = nx.circular_layout(G)

nx.draw_circular(G, node_size=1000, node_color='r',
                 node_shape='s', with_labels=False)
nx.draw_networkx_labels(G, pos, labels, font_size=12)
plt.show()
