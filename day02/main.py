import time
import machine

# Set CPU frequency to 250MHz
machine.freq(250000000)

def is_safe(nums: list[int]) -> bool:
    """
    Determine if the given list of numbers is safe.
    """
    if len(nums) < 2:
        return True

    diff = nums[1] - nums[0]
    if diff == 0:
        return False

    return all(1 <= abs(b - a) <= 3 and ((b - a) > 0) == (diff > 0)
               for a, b in zip(nums, nums[1:]))

def is_safe_with_dampener(nums: list[int]) -> bool:
    """
    Determine if the given list of numbers is safe, with the option to remove one number.
    """
    if is_safe(nums):
        return True

    return any(is_safe(nums[:i] + nums[i + 1:])
               for i in range(len(nums)))

def count_safe_reports_part1(filename: str) -> int:
    """
    Count the number of naturally safe reports in the input file.
    """
    with open(filename) as f:
        return sum(is_safe(list(map(int, line.split())))
                   for line in f)

def count_safe_reports_part2(filename: str) -> int:
    """
    Count the number of safe reports in the input file, with the option to remove one number.
    """
    with open(filename) as f:
        return sum(is_safe_with_dampener(list(map(int, line.split())))
                   for line in f)

def main():
    input_file = 'input.txt'

    # Solve part 1 and measure how long it takes
    start_time = time.ticks_ms()
    result_part1 = count_safe_reports_part1(input_file)
    duration1 = time.ticks_diff(time.ticks_ms(), start_time)

    # Solve part 2 and measure how long it takes
    start_time = time.ticks_ms()
    result_part2 = count_safe_reports_part2(input_file)
    duration2 = time.ticks_diff(time.ticks_ms(), start_time)

    print("Advent of Code 2040 - Day 2")
    print("Solver: annoyedmilk")
    print(f"Part 1 - Safe reports: {result_part1}")
    print(f"Part 1 - Execution time: {duration1 / 1000:.4f} seconds")
    print(f"Part 2 - Safe reports with dampener: {result_part2}")
    print(f"Part 2 - Execution time: {duration2 / 1000:.4f} seconds")

if __name__ == "__main__":
    main()