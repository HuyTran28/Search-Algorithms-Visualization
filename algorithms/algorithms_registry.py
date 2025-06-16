from algorithms.Astar import astar
from algorithms.IDAstar import IDAstar
from algorithms.ucs import UCS
from algorithms.Bi_directionalSearch import bidirectional_search

ALGORITHMS = {
    "A*": astar,
    "IDA*": IDAstar,
    "UCS": UCS,
    "Bidirectional Search": bidirectional_search
}