# NetworkXplorer

Social network analysis toolkit built with NetworkX. Analyzes ego networks and friendship graphs to compute structural metrics like clustering coefficients, path lengths, and degree distributions.

Built as part of a university course on semantic web and social networks.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python)
![NetworkX](https://img.shields.io/badge/NetworkX-2.x-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-blue)

---

## What It Does

Three analysis scripts, each targeting a different network structure:

| Script | Input | Analysis |
|---|---|---|
| `ego_net.py` | `data/ego.csv` | Ego network — degree, path length, clustering coefficient |
| `user_friends.py` | `data/users_friends.csv` | Friendship graph — connectivity, degree distribution, score frequency |
| `semantic_part_a.py` | `data/json/keys.json` | Twitter API authentication to fetch social graph data |

### Metrics Computed

- **Mean degree** — average connections per node
- **Characteristic path length** — average shortest path between any two nodes
- **Mean clustering coefficient** — how tightly nodes cluster together
- **Connectivity check** — whether all nodes in the graph are reachable

---

## Installation

```bash
git clone https://github.com/NickLitharis/networkxplorer
cd networkxplorer
pip install -r requirements.txt
```

---

## Usage

```bash
# Ego network analysis
python ego_net.py

# Friendship graph analysis
python user_friends.py
```

For `semantic_part_a.py`, add your Twitter API keys to `data/json/keys.json`:

```json
{
  "api_key": "...",
  "api_secret": "...",
  "access_token": "...",
  "access_secret": "..."
}
```

---

## Data Format

**ego.csv** — edge list with `source` and `target` columns  
**users_friends.csv** — edge list with `id_a`, `id_b`, and `score` columns
