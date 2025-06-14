import random
import time
import logging
import statistics
import math
from sorting_algorithms import InsertionSort, QuickSort, MergeSort

class SortingExperiment:
    def __init__(self):
        self.algorithms = [InsertionSort(), QuickSort(), MergeSort()]
        self.large_sizes = list(range(1000, 10001, 1000))
        self.small_sizes = list(range(10, 101, 10))
        self.orders = ['random', 'ascending', 'descending']
        self.results = {algo.name: {} for algo in self.algorithms}
        self.colors = {
            'Insertion Sort': '#1f77b4',
            'Quick Sort': '#ff7f0e',
            'Merge Sort': '#2ca02c'
        }
        self.line_styles = {
            'random': '-',
            'ascending': '--',
            'descending': ':'
        }

    def generate_data(self, size, order):
        data = list(range(size))
        if order == 'random':
            random.shuffle(data)
        elif order == 'descending':
            data.reverse()
        return data

    def verify_sorted(self, arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    def calculate_confidence_interval(self, data, confidence=0.95):
        n = len(data)
        if n < 2:
            return 0.0, 0.0
        mean = statistics.mean(data)
        stdev = statistics.stdev(data)
        t_value = 2.262  
        margin = t_value * stdev / math.sqrt(n)
        return mean - margin, mean + margin

    def run_experiments(self):
        logging.info("Starting experiments for large lists")
        for size in self.large_sizes:
            for order in self.orders:
                data = self.generate_data(size, order)
                for algo in self.algorithms:
                    key = f"{order}_{size}"
                    self.results[algo.name][key] = {'time': [], 'comparisons': []}
                    for _ in range(10):  
                        start_time = time.perf_counter()
                        sorted_arr = algo.sort_timing(data.copy())
                        end_time = time.perf_counter()
                        if not self.verify_sorted(sorted_arr):
                            logging.error(f"{algo.name} failed to sort {order} list of size {size}")
                        self.results[algo.name][key]['time'].append((end_time - start_time) * 1000)
                        algo.reset_comparisons()
                        sorted_arr = algo.sort_counting(data.copy())
                        self.results[algo.name][key]['comparisons'].append(algo.comparisons)
                        if not self.verify_sorted(sorted_arr):
                            logging.error(f"{algo.name} failed to sort {order} list of size {size}")
                    logging.info(f"Completed experiments for {algo.name}, {order}, size {size}")

        logging.info("Starting experiments for small lists")
        for size in self.small_sizes:
            for order in self.orders:
                data = self.generate_data(size, order)
                for algo in self.algorithms:
                    key = f"{order}_{size}_small"
                    self.results[algo.name][key] = {'time': [], 'comparisons': []}
                    for _ in range(10):  
                        start_time = time.perf_counter()
                        sorted_arr = algo.sort_timing(data.copy())
                        end_time = time.perf_counter()
                        if not self.verify_sorted(sorted_arr):
                            logging.error(f"{algo.name} failed to sort {order} list of size {size} (small)")
                        self.results[algo.name][key]['time'].append((end_time - start_time) * 1000)
                        algo.reset_comparisons()
                        sorted_arr = algo.sort_counting(data.copy())
                        self.results[algo.name][key]['comparisons'].append(algo.comparisons)
                        if not self.verify_sorted(sorted_arr):
                            logging.error(f"{algo.name} failed to sort {order} list of size {size} (small)")
                    logging.info(f"Completed experiments for {algo.name}, {order}, size {size} (small)")

    def verify_results(self):
        logging.info("Verifying experiment results")
        for algo in self.algorithms:
            for order in self.orders:
                for size in self.large_sizes:
                    key = f"{order}_{size}"
                    if key not in self.results[algo.name]:
                        logging.warning(f"Missing results for {algo.name}, {order}, size {size}")
                for size in self.small_sizes:
                    key = f"{order}_{size}_small"
                    if key not in self.results[algo.name]:
                        logging.warning(f"Missing results for {algo.name}, {order}, size {size} (small)")

    def log_numerical_results(self):
        logging.info("\n\n=== Numerical Results for Report ===")
        
        logging.info("\nLarge Lists (1000-10000 elements):")
        for order in self.orders:
            logging.info(f"\nOrder: {order.capitalize()}")
            logging.info(f"{'Size':<10} {'Algorithm':<15} {'Avg Time (ms)':<15} {'Time StdDev':<15} {'Time CI (95%)':<20} {'Avg Comparisons':<15} {'Comp StdDev':<15} {'Comp CI (95%)':<20}")
            for size in self.large_sizes:
                key = f"{order}_{size}"
                for algo in self.algorithms:
                    if key in self.results[algo.name]:
                        times = self.results[algo.name][key]['time']
                        comps = self.results[algo.name][key]['comparisons']
                        avg_time = statistics.mean(times)
                        time_std = statistics.stdev(times) if len(times) > 1 else 0.0
                        time_ci = self.calculate_confidence_interval(times)
                        avg_comps = statistics.mean(comps)
                        comp_std = statistics.stdev(comps) if len(comps) > 1 else 0.0
                        comp_ci = self.calculate_confidence_interval(comps)
                        logging.info(f"{size:<10} {algo.name:<15} {avg_time:<15.2f} {time_std:<15.2f} {f'[{time_ci[0]:.2f}, {time_ci[1]:.2f}]':<20} {avg_comps:<15.0f} {comp_std:<15.0f} {f'[{comp_ci[0]:.0f}, {comp_ci[1]:.0f}]':<20}")

        logging.info("\nSmall Lists (10-100 elements):")
        for order in self.orders:
            logging.info(f"\nOrder: {order.capitalize()}")
            logging.info(f"{'Size':<10} {'Algorithm':<15} {'Avg Time (ms)':<15} {'Time StdDev':<15} {'Time CI (95%)':<20} {'Avg Comparisons':<15} {'Comp StdDev':<15} {'Comp CI (95%)':<20}")
            for size in self.small_sizes:
                key = f"{order}_{size}_small"
                for algo in self.algorithms:
                    if key in self.results[algo.name]:
                        times = self.results[algo.name][key]['time']
                        comps = self.results[algo.name][key]['comparisons']
                        avg_time = statistics.mean(times)
                        time_std = statistics.stdev(times) if len(times) > 1 else 0.0
                        time_ci = self.calculate_confidence_interval(times)
                        avg_comps = statistics.mean(comps)
                        comp_std = statistics.stdev(comps) if len(comps) > 1 else 0.0
                        comp_ci = self.calculate_confidence_interval(comps)
                        logging.info(f"{size:<10} {algo.name:<15} {avg_time:<15.4f} {time_std:<15.4f} {f'[{time_ci[0]:.4f}, {time_ci[1]:.4f}]':<20} {avg_comps:<15.0f} {comp_std:<15.0f} {f'[{comp_ci[0]:.0f}, {comp_ci[1]:.0f}]':<20}")

        logging.info("\nSpecial Case Comparisons:")
        logging.info("\nInsertion Sort Best vs Worst Case:")
        logging.info(f"{'Size':<10} {'Order':<15} {'Avg Time (ms)':<15} {'Time StdDev':<15} {'Time CI (95%)':<20}")
        for size in self.large_sizes:
            for order in ['ascending', 'descending']:
                key = f"{order}_{size}"
                if key in self.results['Insertion Sort']:
                    times = self.results['Insertion Sort'][key]['time']
                    avg_time = statistics.mean(times)
                    time_std = statistics.stdev(times) if len(times) > 1 else 0.0
                    time_ci = self.calculate_confidence_interval(times)
                    logging.info(f"{size:<10} {order.capitalize():<15} {avg_time:<15.2f} {time_std:<15.2f} {f'[{time_ci[0]:.2f}, {time_ci[1]:.2f}]':<20}")

        logging.info("\nQuick Sort Pivot Impact:")
        logging.info(f"{'Size':<10} {'Order':<15} {'Avg Time (ms)':<15} {'Time StdDev':<15} {'Time CI (95%)':<20}")
        for size in self.large_sizes:
            for order in ['random', 'ascending']:
                key = f"{order}_{size}"
                if key in self.results['Quick Sort']:
                    times = self.results['Quick Sort'][key]['time']
                    avg_time = statistics.mean(times)
                    time_std = statistics.stdev(times) if len(times) > 1 else 0.0
                    time_ci = self.calculate_confidence_interval(times)
                    logging.info(f"{size:<10} {order.capitalize():<15} {avg_time:<15.2f} {time_std:<15.2f} {f'[{time_ci[0]:.2f}, {time_ci[1]:.2f}]':<20}")