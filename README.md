# Advent of Code 2040 - RP2040 MicroPython Solutions

Solutions for Advent of Code 2040 challenges, optimized to run on the RP2040 microcontroller using MicroPython. These solutions focus on minimal memory usage and efficient processing while maintaining reasonable execution times.

## 🎄 Current Progress

| Day | Part 1 | Part 2 |
|-----|---------|---------|
| 1 | ✅ 1151792 (0.34s) | ✅ 21790168 (1.11s) |
| 2 | ✅ 463 (0.99s) | ✅ 514 (1.86s) |
| 3 | ✅ 169021493 (5.37s) | ✅ 111762583 (6.62s) |
| 4 | ✅ 2593 (100.73s) | ✅ 1950 (5.13s) |
| 5 | ✅ 4766 (16.72s) | ✅ 6257 (37.89s) |

## 🔧 Hardware Requirements

- Raspberry Pi Pico (I use the official Raspberry Pi Pico W)
- MicroPython firmware installed (available at https://github.com/annoyedmilk/aoc_rp2040/tree/main/firmware)

## 📦 Installation

1. Install MicroPython on your RP2040 board
   ```bash
   # Download the latest MicroPython firmware for RP2040
   # Flash it to your board using the appropriate method
   ```

2. Clone this repository
   ```bash
   git clone https://github.com/annoyedmilk/aoc_rp2040.git
   ```

3. Copy the solutions to your RP2040
   ```bash
   # Using your preferred method (I use VS Code with the extensions below)
   # Transfer the .py files and input files to the board
   # For example, from the folder day1: input.txt and main.py
   ```

### Required VS Code Extensions
- [Raspberry Pi Pico](https://marketplace.visualstudio.com/items?itemName=raspberry-pi.raspberry-pi-pico) - Official Raspberry Pi extension for VS Code
- [MicroPico](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go) - VS Code extension for MicroPython development on Raspberry Pi Pico

## 📊 Memory Usage

The solutions are designed to run within the RP2040's 264KB RAM limitation:
- Minimal temporary storage
- Optimized data structures
- Efficient memory management

## 🛠️ Code Structure

```
aoc_rp2040/
├── day1/
│   ├── solution.py
│   └── input.txt
├── day2/
│   ├── solution.py
│   └── input.txt
...
└── day5/
    ├── solution.py
    └── input.txt
```

## ✨ Acknowledgments

- Thanks to Advent of Code for providing challenging puzzles
- The MicroPython community for their excellent embedded Python support
- The RP2040 team for creating an amazing microcontroller

## 📧 Contact

- Creator: annoyedmilk
- GitHub: [annoyedmilk](https://github.com/annoyedmilk)

---

*Happy Coding and Happy Advent of Code!* 🎄✨
