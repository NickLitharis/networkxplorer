import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Ερώτημα Γ

# # Read the users_friends.csv file
df = pd.read_csv('data/users_friends.csv')

# Create an empty graph
G = nx.Graph()

# Add edges to the graph
for _, row in df.iterrows():
    source = row['id_a']
    target = row['id_b']
    G.add_edge(source, target)

# Calculate the number of nodes and edges
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

# Check if all users are connected
is_connected = nx.is_connected(G)

# Calculate graph metrics
mean_degree = sum(dict(G.degree()).values()) / num_nodes
characteristic_path_length = nx.average_shortest_path_length(G)
mean_clustering_coefficient = nx.average_clustering(G)

# Print the results
print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)
print("Are all users connected?", is_connected)
print("Mean degree:", mean_degree)
print("Characteristic path length:", characteristic_path_length)
print("Mean clustering coefficient:", mean_clustering_coefficient)

sorted_score = df['score'].value_counts().sort_index(ascending=True)

# Plot the score
sorted_score.plot(kind='bar')
plt.plot(sorted_score)
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Score Frequency')
plt.show()
