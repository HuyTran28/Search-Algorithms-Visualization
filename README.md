# Search Algorithms Visualization

This project is a visualization tool for various pathfinding and search algorithms, built with Python and Pygame. It provides an interactive interface to explore how different algorithms traverse a grid to find a path from a start to a goal node, making it ideal for educational purposes and algorithm analysis.

## Features
- Visualize popular search algorithms such as:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - A* Search
  - Uniform Cost Search (UCS)
  - Iterative Deepening Search (IDS)
  - Iterative Deepening A* (IDA*)
  - Beam Search
  - Bidirectional Search
- Interactive grid editor: set start, goal
- Maze generation for randomized challenges
- Full-run visualization
- Algorithm selection and result display

## Directory Structure
- `main.py` — Entry point; runs the visualization app
- `algorithms/` — Implementations of search algorithms and utilities
- `core/` — Core data structures (grid, node, problem, result)
- `gui/` — User interface components and rendering logic
- `utils/` — Constants and helper functions
- `assets/` — Fonts, tile images, and UI graphics

## Requirements
- Python 3.10+
- [Pygame](https://www.pygame.org/)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/HuyTran28/Search-Algorithms-Visualization
   cd Search-Algorithms-Visualization
   ```
2. Install dependencies:
   ```sh
   pip install pygame
   ```

## Usage
Run the application with:
```sh
python main.py
```

- Use the interface to select an algorithm, generate a maze, and run the visualization.
- Interact with the grid to set start and goal.

## License
This project is for educational and demonstration purposes.
