import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Ερώτημα Β

# Read the ego.csv file
df = pd.read_csv('data/ego.csv')

# Create graph
G = nx.Graph()

# Add nodes and edges to the graph
for _, row in df.iterrows():
    source = row['source']
    target = row['target']
    G.add_edge(source, target)

# Calculate the number of nodes and edges
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

# Calculate graph metrics
degree = dict(G.degree())
mean_degree = sum(degree.values()) / num_nodes
characteristic_path_length = nx.average_shortest_path_length(G)
mean_clustering_coefficient = nx.average_clustering(G)

# Print the results
print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)
print("Mean degree:", mean_degree)
print("Characteristic path length:", characteristic_path_length)
print("Mean clustering coefficient:", mean_clustering_coefficient)


# Draw the network
nx.draw(G, node_size=10, node_color='red', edge_color='blue', with_labels=True)
plt.show()
