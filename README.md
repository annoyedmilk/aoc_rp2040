# Advent of Code 2040 - RP2040 MicroPython Solutions
Solutions for Advent of Code 2040 challenges, optimized to run on the RP2040 microcontroller using MicroPython. The solutions focus on minimal memory usage and efficient processing while maintaining reasonable execution times.
## 🎄 Current Progress
| Day | Part 1 | Part 2 |
|-----|---------|---------|
| 1 | ✅ 1151792 (0.34s) | ✅ 21790168 (1.11s) |
| 2 | ✅ 463 (0.99s) | ✅ 514 (1.86s) |
| 3 | ✅ 169021493 (5.37s) | ✅ 111762583 (6.62s) |
| 4 | ✅ 2593 (100.73s) | ✅ 1950 (5.13s) |
| 5 | ✅ 4766 (16.72s) | ✅ 6257 (37.89s) |
## 🔧 Hardware Requirements
- Raspberry Pi Pico (i use the offical Raspberry Pi Pico W)
- MicroPython firmware installed (https://github.com/annoyedmilk/aoc_rp2040/tree/main/firmware)
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
   # Using your preferred method (i use vs code with Raspberry Pi Pico &  MicroPico)
   # Transfer the .py fils and input files to the board (for example from the folder day 1 input.txtx and main.py)
   ```
## 📊 Memory Usage
The solutions are designed to run within the RP2040's 264KB RAM limitation.
- Minimal temporary storage
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
- Thanks to Advent of Code for the challenging puzzles
- The MicroPython community for embedded Python support
- The RP2040 team for an amazing microcontroller
## 📧 Contact
- Creator: annoyedmilk
- GitHub: [annoyedmilk](https://github.com/annoyedmilk)
---
*Happy Coding and Happy Advent of Code!* 🎄✨
