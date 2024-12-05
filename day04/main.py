import time
import machine

# Set CPU frequency to 250MHz
machine.freq(250000000)

def read_input(filename: str) -> list[str]:
    """
    Read the input file and return a list of lines.

    Args:
        filename (str): The path to the input file.

    Returns:
        list[str]: The lines from the input file.
    """
    with open(filename) as f:
        return [line.strip() for line in f if all(c in 'XMAS' for c in line.strip())]

def count_xmas_occurrences(grid: list[str]) -> int:
    """
    Count the number of XMAS occurrences in the grid.

    Args:
        grid (list[str]): The grid of characters.

    Returns:
        int: The number of XMAS occurrences.
    """
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    R, C = len(grid), len(grid[0])

    def check(x: int, y: int, dx: int, dy: int) -> bool:
        return all(0 <= x + i * dx < R and 0 <= y + i * dy < C and
                   grid[x + i * dx][y + i * dy] == "XMAS"[i] for i in range(4))

    return sum(check(i, j, dx, dy)
               for i in range(R)
               for j in range(C)
               for dx, dy in dirs)

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

    patterns = [('MAS', 'MAS'), ('MAS', 'SAM'), ('SAM', 'MAS'), ('SAM', 'SAM')]
    for p1, p2 in patterns:
        if (grid[r-1][c-1] == p1[0] and grid[r][c] == p1[1] and grid[r+1][c+1] == p1[2] and
            grid[r-1][c+1] == p2[0] and grid[r][c] == p2[1] and grid[r+1][c-1] == p2[2]):
            return True
    return False

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