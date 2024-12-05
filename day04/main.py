import time
import machine

# Set CPU frequency to 250MHz
machine.freq(250000000)

# Pre-computed constants
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
XMAS = "XMAS"
PATTERNS = (
    (('M','A','S'), ('M','A','S')),
    (('M','A','S'), ('S','A','M')),
    (('S','A','M'), ('M','A','S')),
    (('S','A','M'), ('S','A','M'))
)

def read_input(filename: str) -> list[str]:
    """
    Read the input file and return a list of lines.

    Args:
        filename (str): The path to the input file.

    Returns:
        list[str]: The lines from the input file.
    """
    with open(filename) as f:
        return [line.strip() for line in f if all(c in XMAS for c in line.strip())]

def check(x: int, y: int, dx: int, dy: int, R: int, C: int, grid: list[str]) -> bool:
    """
    Check if there is a valid XMAS sequence starting at (x,y) in direction (dx,dy).
    
    Args:
        x, y (int): Starting coordinates
        dx, dy (int): Direction vector
        R, C (int): Grid dimensions
        grid (list[str]): The character grid
        
    Returns:
        bool: True if valid XMAS sequence found
    """
    end_x = x + 3 * dx
    end_y = y + 3 * dy
    if not (0 <= end_x < R and 0 <= end_y < C):
        return False
    
    for i in range(4):
        if grid[x + i * dx][y + i * dy] != XMAS[i]:
            return False
    return True

def count_xmas_occurrences(grid: list[str]) -> int:
    """
    Count the number of XMAS occurrences in the grid.

    Args:
        grid (list[str]): The grid of characters.

    Returns:
        int: The number of XMAS occurrences.
    """
    R, C = len(grid), len(grid[0])
    return sum(check(i, j, dx, dy, R, C, grid)
              for i in range(R)
              for j in range(C)
              for dx, dy in DIRS)

def check_xmas_pattern(grid: list[str], r: int, c: int) -> bool:
    """
    Check if there is an X-MAS pattern at the given row and column.

    Args:
        grid (list[str]): The grid of characters.
        r (int): The row index.
        c (int): The column index.

    Returns:
        bool: True if there is an X-MAS pattern, False otherwise.
    """
    if r < 1 or r >= len(grid) - 1 or c < 1 or c >= len(grid[0]) - 1:
        return False
        
    # Early exit if center isn't 'A'
    center = grid[r][c]
    if center != 'A':
        return False
        
    # Create tuples for current pattern
    diag1 = (grid[r-1][c-1], center, grid[r+1][c+1])
    diag2 = (grid[r-1][c+1], center, grid[r+1][c-1])
    
    return (diag1, diag2) in PATTERNS

def count_xmas_patterns(grid: list[str]) -> int:
    """
    Count the number of X-MAS patterns in the grid.

    Args:
        grid (list[str]): The grid of characters.

    Returns:
        int: The number of X-MAS patterns.
    """
    return sum(check_xmas_pattern(grid, r, c)
              for r in range(1, len(grid) - 1)
              for c in range(1, len(grid[0]) - 1))

def main():
    input_file = 'input.txt'

    # Solve part 1 and measure how long it takes
    start_time = time.ticks_ms()
    grid = read_input(input_file)
    result_part1 = count_xmas_occurrences(grid)
    duration1 = time.ticks_diff(time.ticks_ms(), start_time)

    # Solve part 2 and measure how long it takes
    start_time = time.ticks_ms()
    result_part2 = count_xmas_patterns(grid)
    duration2 = time.ticks_diff(time.ticks_ms(), start_time)

    print("Advent of Code 2040 - Day 4")
    print("Solver: annoyedmilk")
    print(f"Part 1 - Number of XMAS occurrences: {result_part1}")
    print(f"Part 1 - Execution time: {duration1 / 1000:.4f} seconds")
    print(f"Part 2 - Number of X-MAS patterns: {result_part2}")
    print(f"Part 2 - Execution time: {duration2 / 1000:.4f} seconds")

if __name__ == "__main__":
    main()