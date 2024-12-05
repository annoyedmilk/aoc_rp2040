import time
import ure

def parse_mul_instructions(input_file: str) -> int:
    """
    Parse the input file and sum the results of all valid multiplication instructions.
    Only processes mul(X,Y) where X and Y are 1-3 digit numbers.
    Args:
        input_file (str): The path to the input file.
    Returns:
        int: The sum of all multiplication results.
    """
    total_result = 0
    # Pattern to match mul followed by digits,comma,digits in parentheses
    pattern = ure.compile(r"mul\(\d+,\d+\)")
    
    try:
        with open(input_file, 'r') as f:
            content = f.read()
            # Find all potential mul instructions
            pos = 0
            while True:
                match = pattern.search(content[pos:])
                if not match:
                    break
                    
                # Get the full matched string
                instruction = content[pos + match.start():pos + match.end()]
                # Extract numbers between parentheses
                nums = instruction[4:-1].split(',')
                if len(nums) == 2:
                    # Verify numbers are 1-3 digits
                    x, y = nums[0], nums[1]
                    if len(x) <= 3 and len(y) <= 3 and x.isdigit() and y.isdigit():
                        total_result += int(x) * int(y)
                
                pos += match.end()
                
    except Exception as e:
        print("Error:", e)
    return total_result

def parse_conditional_muls(input_file: str) -> int:
    """
    Parse the input file and sum the results of enabled multiplication instructions.
    Handles do() and don't() instructions that enable/disable multiplication.
    Args:
        input_file (str): The path to the input file.
    Returns:
        int: The sum of enabled multiplication results.
    """
    total_result = 0
    # Compile patterns
    mul_pattern = ure.compile(r"mul\(\d+,\d+\)")
    do_pattern = ure.compile(r"do\(\)")
    dont_pattern = ure.compile(r"don't\(\)")
    
    try:
        with open(input_file, 'r') as f:
            content = f.read()
            
            # Find all instructions and their positions
            instructions = []
            
            # Find mul instructions
            pos = 0
            while True:
                match = mul_pattern.search(content[pos:])
                if not match:
                    break
                    
                # Get the full instruction
                full_pos = pos + match.start()
                instruction = content[full_pos:full_pos + match.end() - match.start()]
                # Extract and validate numbers
                nums = instruction[4:-1].split(',')
                if len(nums) == 2:
                    x, y = nums[0], nums[1]
                    if len(x) <= 3 and len(y) <= 3 and x.isdigit() and y.isdigit():
                        instructions.append(('mul', full_pos, int(x), int(y)))
                
                pos += match.end()
            
            # Find do() instructions
            pos = 0
            while True:
                match = do_pattern.search(content[pos:])
                if not match:
                    break
                instructions.append(('do', pos + match.start()))
                pos += match.end()
            
            # Find don't() instructions
            pos = 0
            while True:
                match = dont_pattern.search(content[pos:])
                if not match:
                    break
                instructions.append(('dont', pos + match.start()))
                pos += match.end()
            
            # Sort instructions by position
            instructions.sort(key=lambda x: x[1])
            
            # Process instructions in order
            enabled = True
            for inst in instructions:
                if inst[0] == 'do':
                    enabled = True
                elif inst[0] == 'dont':
                    enabled = False
                elif inst[0] == 'mul' and enabled:
                    total_result += inst[2] * inst[3]
                    
    except Exception as e:
        print("Error:", e)
    return total_result

def main():
    input_file = 'input.txt'
    
    # Solve part 1 and measure how long it takes
    start_time = time.ticks_ms()
    result_part1 = parse_mul_instructions(input_file)
    duration1 = time.ticks_diff(time.ticks_ms(), start_time)
    
    # Solve part 2 and measure how long it takes
    start_time = time.ticks_ms()
    result_part2 = parse_conditional_muls(input_file)
    duration2 = time.ticks_diff(time.ticks_ms(), start_time)
    
    print("Advent of Code 2040 - Day 3")
    print("Solver: annoyedmilk")
    print(f"Part 1 - Sum of all multiplication results: {result_part1}")
    print(f"Part 1 - Execution time: {duration1 / 1000:.4f} seconds")
    print(f"Part 2 - Sum of enabled multiplication results: {result_part2}")
    print(f"Part 2 - Execution time: {duration2 / 1000:.4f} seconds")

if __name__ == "__main__":
    main()