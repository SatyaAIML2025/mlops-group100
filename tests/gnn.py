#Importing required libraries
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# Create a Graph
G = nx.barabasi_albert_graph(50, 2)  # Scale-free network with 50 nodes, 2 edges per node

# 1. Degree Distribution
degrees = [G.degree(n) for n in G.nodes()]
plt.hist(degrees, bins=10, color='blue', alpha=0.7)
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()