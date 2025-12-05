# 🧬 Evolutionary Path Planning

Path planning using Genetic Algorithms for robot navigation in terrain with varying elevations.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
</p>

## Demo

https://github.com/user-attachments/assets/path_planning.mov

## Quick Start

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python pygame_visualization.py
```

## How It Works

A **Genetic Algorithm** mimics natural evolution to find optimal solutions. Here's how it solves path planning:

### The Problem
Navigate a robot from start `(4,4)` to goal `(8,1)` on a 10x10 grid where each cell has an elevation (0-8). The robot can only move to adjacent cells if:
```
current_height + robot_height ≥ destination_height
```

### The Solution

1. **Chromosome**: Each individual is a sequence of moves like `['U', 'R', 'R', 'D', 'L', ...]`

2. **Fitness Function**: Evaluates how good a path is by:
   - ✅ Rewarding valid moves toward the goal
   - ✅ Big bonus for reaching the destination (earlier = better)
   - ❌ Penalizing out-of-bounds moves (-10,000)
   - ❌ Penalizing distance from target

3. **Evolution Cycle** (repeated for N generations):
   ```
   Selection → Crossover → Mutation → Survival
   ```
   - **Selection**: Roulette wheel - fitter individuals have higher chance of being parents
   - **Crossover**: Combine two parents at a random point to create children
   - **Mutation**: Randomly change moves (adaptive rate: 80% for weak, 0% for strong)
   - **Survival**: Keep the best individuals (elitism)

## Configuration

```python
from src.genetic_algorithm import GeneticAlgorithm

ga = GeneticAlgorithm(
    population_size=10,
    num_possible_moves=15,
    iterations=2000
)
```

## Project Structure

```
src/
├── constants.py          # Shared constants
├── individual.py         # Chromosome representation
├── population.py         # Population management
└── genetic_algorithm/    # GA implementations (fixed & variable length)
```

## License

MIT License - see [LICENSE](LICENSE)

## Author

**Mohit Manoj** - [GitHub](https://github.com/lolzone13)