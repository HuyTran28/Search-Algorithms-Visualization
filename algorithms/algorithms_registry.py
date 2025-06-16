from algorithms.Astar import astar
from algorithms.IDAstar import IDAstar
from algorithms.bfs import bfs
from algorithms.ids import ids
from algorithms.ucs import UCS
from algorithms.Bi_directionalSearch import bidirectional_search

ALGORITHMS = {
    "A*": astar,
    "IDA*": IDAstar,
    "BFS": bfs,
    "IDS": ids,
    "UCS": UCS,
    "Bidirectional Search": bidirectional_search,
}