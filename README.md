# Sorting Algorithms Performance Analysis

This project analyzes and compares the performance of three sorting algorithms: Insertion Sort, Quick Sort, and Merge Sort.

## Features
- Measures execution time and number of comparisons
- Tests algorithms with different input sizes (10-100 and 1000-10000 elements)
- Analyzes performance with different input orders (random, ascending, descending)
- Runs each test 10 times for statistical significance
- Calculates confidence intervals and standard deviations
- Generates comprehensive performance graphs
- Logs detailed numerical results with statistical analysis

## Analytics
- Mean execution time and comparison counts
- Standard deviation for timing and comparisons
- 95% confidence intervals
- Special case analysis for each algorithm
- Performance consistency measurements

## Project Structure
- `main.py` - Entry point that orchestrates the experiment
- `experiment.py` - Core experiment logic and statistical analysis
- `sorting_algorithms.py` - Implementation of sorting algorithms
- `plotting.py` - Visualization of results using matplotlib
- `utils.py` - Utility functions for logging

## Setup and Running

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install matplotlib
```

4. Run the experiment:
```bash
python main.py
```

## Output
- Performance graphs saved as PNG files
- Detailed logs with statistical analysis
- Comparative analysis across different input sizes and orders
- Special case performance evaluations
