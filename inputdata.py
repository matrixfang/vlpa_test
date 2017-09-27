import networkx as nx
import random


def two_cluster_group(size, degree_ave, u):
    # return a two cluster group
    p = float(degree_ave) / size
    edge = size * (size - 1) * p / 2
    inter = int(edge * u)
    G = nx.fast_gnp_random_graph(size, p)

    for e in G.edges():
        G.add_edge(e[0] + size, e[1] + size)

    for i in range(1, inter + 1):
        G.add_edge(random.randint(1, size), random.randint(size + 1, size + size))
    return G


def read_network(filename):
    G = nx.Graph()
    fp = open(filename, 'r')
    while 1:
        line = fp.readline()
        if not line:
            break
        temp = line.split()
        G.add_edge(int(temp[0]), int(temp[1]))
    fp.close()
    return G


def read_community(filename):
    community_label = dict()
    fp = open(filename, 'r')
    while 1:
        line = fp.readline()
        if not line:
            break
        temp = line.split()
        community_label[int(temp[0])] = (int(temp[1]))
    fp.close()
    return community_label


def read_lfr(number):
    if number in [12, 128, 500, 800, 1300, 1000, '128b', '800b']:
        str(number)
        path_1 = '/Users/fangwenyi/Documents/Data_set/network/network_'+ str(number) + '/'+ str(number) + '_network.dat'
        path_2 = '/Users/fangwenyi/Documents/Data_set/network/network_'+ str(number) + '/'+ str(number) + '_community.dat'
    else:
        print("There are no such network")
    G = read_network(path_1)
    community_label = read_community(path_2)
    return G, community_label
