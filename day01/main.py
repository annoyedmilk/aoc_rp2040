import time

def calculate_distance(input_file: str) -> int:
    """
    Calculate the total distance between the left and right numbers in the input file.

    Args:
        input_file (str): The path to the input file.

    Returns:
        int: The total distance.
    """
    left_numbers = []
    right_numbers = []

    with open(input_file) as file:
        for line in file:
            left, right = line.split()
            left_numbers.append(int(left))
            right_numbers.append(int(right))

    left_numbers.sort()
    right_numbers.sort()

    total_distance = 0
    for i in range(len(left_numbers)):
        distance = abs(left_numbers[i] - right_numbers[i])
        total_distance += distance

    return total_distance

def calculate_similarity_score(input_file: str) -> int:
    """
    Calculate the similarity score between the left and right numbers in the input file.

    Args:
        input_file (str): The path to the input file.

    Returns:
        int: The similarity score.
    """
    left_numbers = []
    right_numbers = []

    with open(input_file) as file:
        for line in file:
            left, right = line.split()
            left_numbers.append(int(left))
            right_numbers.append(int(right))

    similarity_score = 0
    for left_num in left_numbers:
        appearances = right_numbers.count(left_num)
        similarity_score += left_num * appearances

    return similarity_score

def main():
    input_file = 'input.txt'

    # Solve part 1 and measure how long it takes
    start_time = time.ticks_ms()
    result_part1 = calculate_distance(input_file)
    duration1 = time.ticks_diff(time.ticks_ms(), start_time)

    # Solve part 2 and measure how long it takes
    start_time = time.ticks_ms()
    result_part2 = calculate_similarity_score(input_file)
    duration2 = time.ticks_diff(time.ticks_ms(), start_time)

    print("Advent of Code 2040 - Day 1")
    print("Solver: annoyedmilk")
    print(f"Part 1 - Total distance: {result_part1}")
    print(f"Part 1 - Execution time: {duration1 / 1000:.4f} seconds")
    print(f"Part 2 - Similarity score: {result_part2}")
    print(f"Part 2 - Execution time: {duration2 / 1000:.4f} seconds")

if __name__ == "__main__":
    main()