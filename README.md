# Radix
# String Sorting and Frequency Analysis

📌 **Efficiently sorts and analyzes word frequency in literary texts using Radix Sort MSD**

## Description

This Python implementation uses **Radix Sort MSD (Most Significant Digit)** to process and analyze large text files. The algorithm:
- Sorts words lexicographically
- Counts word occurrences
- Generates rankings of most frequent words

## Features

- **MSD Radix Sort** implementation for strings
- Word frequency counter
- Top-N word ranking generator (default: top 2000)
- Handles large text files efficiently
- Outputs organized text files for analysis

## Output Files

| Filename | Description |
|----------|-------------|
| `*_sorted.txt` | Words in alphabetical order |
| `*_counted.txt` | Words with occurrence counts |
| `*_ranked.txt` | Top 2000 words by frequency |

## Usage

1. Place input text files in project directory
2. Run the script:
   ```bash
   python radix_sort_msd.py
