import gc
import time

def read_input_stream(filename: str):
    """Generator-based input reader to minimize memory usage."""
    current_nums = []
    num = 0
    with open(filename, 'rb') as f:
        while True:
            c = f.read(1)
            if not c:  # EOF
                if num > 0:
                    current_nums.append(num)
                if current_nums:
                    yield current_nums
                break

            b = c[0]
            
            if ord('0') <= b <= ord('9'):
                num = num * 10 + (b - ord('0'))
                continue
                
            if num > 0:
                current_nums.append(num)
                num = 0

            if b == ord('\n'):
                if current_nums:
                    yield current_nums
                    current_nums = []
                    gc.collect()  # Help free memory after each line
            elif b in (ord('|'), ord(','), ord('\r')):
                continue
            elif b == ord(' ') and not current_nums:
                return  # End of rules section

def process_rules(filename: str):
    """Process rules one at a time to save memory."""
    rules = []
    for nums in read_input_stream(filename):
        if len(nums) == 2:
            rules.append((nums[0], nums[1]))
        else:
            break
    return rules

def is_update_valid(rules: list[tuple[int, int]], update: list[int]) -> bool:
    """Memory-efficient validity check."""
    for b, a in rules:
        if b in update and a in update:
            a_pos = update.index(a)
            for j in range(a_pos + 1, len(update)):
                if update[j] == b:
                    return False
    return True

def get_middle_page(update: list[int]) -> int:
    """Get middle page number."""
    return update[len(update) // 2]

def solve_part1(rules, updates_gen):
    """Solve part 1 separately."""
    total = 0
    for update in updates_gen:
        if len(update) != 2:  # Skip rule pairs
            if is_update_valid(rules, update):
                total += get_middle_page(update)
    return total

def solve_part2(rules, updates_gen):
    """Solve part 2 separately."""
    total = 0
    for update in updates_gen:
        if len(update) != 2:  # Skip rule pairs
            if not is_update_valid(rules, update):
                reordered = []
                remaining = update.copy()
                
                while remaining:
                    for page in update:
                        if page not in remaining:
                            continue
                        can_add = True
                        for b, a in rules:
                            if a == page and b in remaining:
                                can_add = False
                                break
                        if can_add:
                            reordered.append(page)
                            remaining.remove(page)
                            break
                
                total += get_middle_page(reordered)
    return total

def main():
    input_file = 'input.txt'
    gc.enable()  # Ensure garbage collection is enabled
    
    # Clear memory before starting
    gc.collect()
    
    try:
        # Process rules first
        rules = process_rules(input_file)
        gc.collect()
        
        # Part 1
        start_time1 = time.ticks_ms()
        result_part1 = solve_part1(rules, read_input_stream(input_file))
        duration1 = time.ticks_diff(time.ticks_ms(), start_time1)
        
        gc.collect()  # Clean up between parts
        
        # Part 2
        start_time2 = time.ticks_ms()
        result_part2 = solve_part2(rules, read_input_stream(input_file))
        duration2 = time.ticks_diff(time.ticks_ms(), start_time2)
        
        print("Advent of Code 2040 - Day 5")
        print("Solver: annoyedmilk")
        print(f"Part 1 - Sum of middle pages in valid updates: {result_part1}")
        print(f"Part 1 - Execution time: {duration1 / 1000:.4f} seconds")
        print(f"Part 2 - Sum of middle pages in reordered updates: {result_part2}")
        print(f"Part 2 - Execution time: {duration2 / 1000:.4f} seconds")
        
    except MemoryError as e:
        print("Memory error occurred:", e)
        print("Free memory:", gc.mem_free())
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()