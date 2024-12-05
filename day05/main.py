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

def solve_parts(filename: str) -> tuple[int, int]:
    """Solve both parts in a single pass to save memory."""
    rules = process_rules(filename)
    gc.collect()  # Collect after processing rules
    
    total_part1 = 0
    total_part2 = 0
    
    # Skip rules section
    found_updates = False
    for update in read_input_stream(filename):
        if not found_updates:
            if len(update) != 2:
                found_updates = True
            else:
                continue
        
        # Part 1 processing
        if is_update_valid(rules, update):
            total_part1 += get_middle_page(update)
        else:
            # Part 2 processing - only for invalid updates
            reordered = []
            remaining = update.copy()
            
            while remaining:
                for page in update:  # use original update for order
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
            
            total_part2 += get_middle_page(reordered)
        
        gc.collect()  # Collect after processing each update
    
    return total_part1, total_part2

def main():
    input_file = 'input.txt'
    gc.enable()  # Ensure garbage collection is enabled
    
    # Clear memory before starting
    gc.collect()
    
    start_time = time.ticks_ms()
    try:
        result_part1, result_part2 = solve_parts(input_file)
        duration = time.ticks_diff(time.ticks_ms(), start_time)
        
        print("Advent of Code 2040 - Day 5")
        print("Solver: annoyedmilk (RP2040 Optimized)")
        print(f"Part 1 - Sum of middle pages in valid updates: {result_part1}")
        print(f"Part 2 - Sum of middle pages in reordered updates: {result_part2}")
        print(f"Total execution time: {duration / 1000:.4f} seconds")
        
    except MemoryError as e:
        print("Memory error occurred:", e)
        print("Free memory:", gc.mem_free())
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()