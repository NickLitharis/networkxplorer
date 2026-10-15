# NetworkXplorer

Social network analysis toolkit built with NetworkX. Analyzes ego networks and friendship graphs to compute structural metrics like clustering coefficients, path lengths, and degree distributions.

Built as part of a university course on semantic web and social networks.

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python)
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
uv sync
```

---

## Usage

```bash
# Ego network analysis
uv run ego_net.py

# Friendship graph analysis
uv run user_friends.py
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

> **Note:** Twitter's v1.1 API was retired, so `semantic_part_a.py` no longer runs.
> The `python_twitter` dependency is kept so the historical code is not silently
> broken; the two graph scripts above are unaffected.

---

## Data Format

**ego.csv** — edge list with `source` and `target` columns  
**users_friends.csv** — edge list with `id_a`, `id_b`, and `score` columns
