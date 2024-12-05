import time

def calculate_distance(input_file):
    # Initialize empty lists for left and right numbers
    left_numbers = []
    right_numbers = []
    
    # Read the file and separate numbers into two lists
    with open(input_file) as file:
        for line in file:
            # Split each line into two numbers
            left, right = line.split()
            left_numbers.append(int(left))
            right_numbers.append(int(right))
    
    # Sort both lists
    left_numbers.sort()
    right_numbers.sort()
    
    # Calculate total distance
    total_distance = 0
    for i in range(len(left_numbers)):
        distance = abs(left_numbers[i] - right_numbers[i])
        total_distance += distance
    
    return total_distance

def calculate_similarity_score(input_file):
    # Initialize empty lists for left and right numbers
    left_numbers = []
    right_numbers = []
    
    # Read the file and separate numbers into two lists
    with open(input_file) as file:
        for line in file:
            # Split each line into two numbers
            left, right = line.split()
            left_numbers.append(int(left))
            right_numbers.append(int(right))
    
    # Calculate similarity score
    similarity_score = 0
    for number in left_numbers:
        # Count how many times each left number appears in right list
        count = right_numbers.count(number)
        similarity_score += count
    
    return similarity_score

def main():
    input_file = 'day01/input.txt'
    
    # Part 1
    start_time = time.ticks_ms()
    result_part1 = calculate_distance(input_file)
    end_time = time.ticks_ms()
    execution_time_part1 = time.ticks_diff(end_time, start_time) / 1000  # Convert to seconds
    
    # Part 2
    start_time = time.ticks_ms()
    result_part2 = calculate_similarity_score(input_file)
    end_time = time.ticks_ms()
    execution_time_part2 = time.ticks_diff(end_time, start_time) / 1000  # Convert to seconds
    
    # Print results
    print("Advent of Code 2040 - Day 1")
    print("Solver: annoyedmilk")
    print(f"Part 1 - Total distance: {result_part1}")
    print(f"Part 1 - Execution time: {execution_time_part1:.4f} seconds")
    print(f"Part 2 - Similarity score: {result_part2}")
    print(f"Part 2 - Execution time: {execution_time_part2:.4f} seconds")

if __name__ == "__main__":
    main()