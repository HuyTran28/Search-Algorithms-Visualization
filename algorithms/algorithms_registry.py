from algorithms.astar import astar
from algorithms.IDAstar import IDAstar
from algorithms.bfs import bfs
from algorithms.ids import ids
from algorithms.ucs import UCS
from algorithms.dfs import dfs
from algorithms.Bi_directionalSearch import bidirectional_search

ALGORITHMS = {
    "A*": astar,
    "IDA*": IDAstar,
    "UCS": UCS,
    "Bidirectional Search": bidirectional_search,
    "BFS": bfs,
    "IDS": ids,
    "DFS": dfs,
}