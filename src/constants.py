"""Shared constants for the Evolutionary Path Planning project."""

# Possible movement directions
MOVES = ['L', 'U', 'R', 'D']

# Fitness function penalties
HARD_PENALTY_BOUNDARY = -10000  # Penalty for going out of bounds
HARD_PENALTY_DISTANCE = -10     # Penalty coefficient for distance from target

# Rewards
TARGET_REACHED_MULTIPLIER = 10000  # Reward multiplier for reaching target early

# Default robot parameters
DEFAULT_ROBOT_HEIGHT = 3
