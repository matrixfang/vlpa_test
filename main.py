import networkx as nx
import numpy as np
import scipy as sp
import inputdata
import draw
import matplotlib.pyplot as plt
import vlpa


G, community_label = inputdata.read_lfr(12)

la = vlpa.vlabels(G)

print(la.to_labels())