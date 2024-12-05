# Advent of Code 2024 - RP2040 MicroPython Solutions

Solutions for Advent of Code 2024 challenges, optimized to run on the RP2040 microcontroller using MicroPython. These solutions focus on minimal memory usage and efficient processing while maintaining reasonable execution times.

## 🎄 Current Progress

| Day | Part 1 | Part 2 |
|-----|---------|---------|
| 1 | ✅ 1151792 (0.17s) | ✅ 21790168 (0.55s) |
| 2 | ✅ 463 (0.49s) | ✅ 514 (0.93s) |
| 3 | ✅ 169021493 (2.71s) | ✅ 111762583 (3.31s) |
| 4 | ✅ 2593 (50.73s) | ✅ 1950 (2.57s) |
| 5 | ✅ 4766 (8.26s) | ✅ 6257 (18.77s) |

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
│   ├── main.py
│   └── input.txt
├── day2/
│   ├── main.py
│   └── input.txt
...
└── day5/
    ├── main.py
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
