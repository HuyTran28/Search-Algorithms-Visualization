from dataclasses import dataclass
from typing import List, Optional

@dataclass
class SearchResult:
    path: Optional[List]  # List of nodes in path
    explored_count: int   # Number of nodes explored
    path_cost: float      # Total cost of path (sum of g)
    time_ms: float        # Time taken (milliseconds)
    memory_kb: float      # Estimated memory usage in KB
