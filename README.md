# Network Analysis with Pandas, NetworkX, and Matplotlib

This repository provides code snippets and examples for performing network analysis using the Pandas, NetworkX, and Matplotlib libraries in Python. The snippets demonstrate various tasks such as reading data, creating graphs, calculating network metrics, and visualizing networks. 

## Table of Contents

- [Network Analysis with Pandas, NetworkX, and Matplotlib](#network-analysis-with-pandas-networkx-and-matplotlib)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Code Snippets](#code-snippets)
    - [Snippet A: Twitter API Client](#snippet-a-twitter-api-client)
    - [Snippet B: Network Analysis with Ego Network](#snippet-b-network-analysis-with-ego-network)
    - [Snippet C: Network Analysis with User Friends](#snippet-c-network-analysis-with-user-friends)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [License](#license)
  - [Contributing](#contributing)

## Introduction

Network analysis involves examining relationships and interactions between entities using a graph-based approach. This repository aims to provide practical examples and code snippets for analyzing and visualizing networks using Python.

The code snippets in this repository utilize the following libraries:

- **Pandas**: A powerful data manipulation library that provides data structures and functions for efficient data analysis.
- **NetworkX**: A Python library for creating, manipulating, and studying the structure, dynamics, and functions of complex networks.
- **Matplotlib**: A plotting library for creating visualizations and graphs.

## Prerequisites

To run the code snippets, ensure that you have the following prerequisites installed:

- Python (version 3.7 or higher)
- Pandas library
- NetworkX library
- Matplotlib library

## Code Snippets

This repository provides three code snippets demonstrating different aspects of network analysis. Here is a brief overview of each snippet:

### Snippet A: Twitter API Client

This snippet showcases how to use the `twitter` library to interact with the Twitter API. It demonstrates how to initialize the API client, verify credentials, and store the credentials in a JSON file.

### Snippet B: Network Analysis with Ego Network

This snippet focuses on analyzing an ego network. It reads data from a CSV file and creates a graph using NetworkX. It then calculates various network metrics such as the number of nodes, number of edges, mean degree, characteristic path length, and mean clustering coefficient. Finally, it visualizes the network using Matplotlib.

### Snippet C: Network Analysis with User Friends

This snippet demonstrates network analysis based on user friendships. It reads data from a CSV file containing user friendships and constructs a graph using NetworkX. It calculates network metrics including the number of nodes, number of edges, whether all users are connected, mean degree, characteristic path length, and mean clustering coefficient. Additionally, it generates a bar plot to visualize the frequency distribution of user scores using Matplotlib.

## Getting Started

To get started with the code snippets in this repository, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your-username/network-analysis.git
   ```

2. Navigate to the project directory:

   ```
   cd network-analysis
   ```

3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. Review the code snippets in the repository and customize them as per your requirements.

## Usage

Each code snippet can be executed individually. Open the desired file (e.g., `snippet_a.py`) and run it using Python:

```
python snippet_a.py
```

Make sure you have the necessary input files (e.g., `keys.json`, `ego.csv`, `users_friends.csv`) in the respective data directories.

Feel free to modify the code snippets, adjust the parameters, or integrate them into your own projects as needed.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Contributions to this repository are welcome! If you have any improvements, suggestions, or new features to add, please submit a pull request.
