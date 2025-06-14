import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
import logging

def plot_comparison_graphs(experiment, timestamp):
    logging.info("Generating comparison graphs")
    for order in experiment.orders:
        for metric, ylabel in [('time', 'Time (ms)'), ('comparisons', 'Comparisons')]:
            plt.figure(figsize=(10, 6))
            lines = []
            labels = []
            for algo in experiment.algorithms:
                algo_name = algo.name
                color = experiment.colors[algo_name]
                sizes = []
                values = []
                for size in experiment.large_sizes:
                    key = f"{order}_{size}"
                    if key in experiment.results[algo_name]:
                        sizes.append(size)
                        values.append(sum(experiment.results[algo_name][key][metric]) / len(experiment.results[algo_name][key][metric]))
                line, = plt.plot(sizes, values, color=color, linestyle=experiment.line_styles[order], linewidth=2)
                lines.append(line)
                labels.append(algo_name)
            
            plt.yscale('log')
            plt.title(f"Algorithm Comparison\n{order.capitalize()} Order - {ylabel}", pad=20)
            plt.xlabel("List Size (elements)", fontsize=12)
            plt.ylabel(ylabel, fontsize=12)
            plt.legend(lines, labels, fontsize=10, framealpha=0.9)
            plt.grid(True, which="both", alpha=0.3)
            filename = f"comparison_{metric}_{order}_{timestamp}.png"
            plt.savefig(filename, dpi=150, bbox_inches='tight')
            logging.info(f"Saved graph: {filename}")
            plt.close()

            plt.figure(figsize=(10, 6))
            lines = []
            labels = []
            for algo in experiment.algorithms:
                algo_name = algo.name
                color = experiment.colors[algo_name]
                sizes = []
                values = []
                for size in experiment.small_sizes:
                    key = f"{order}_{size}_small"
                    if key in experiment.results[algo_name]:
                        sizes.append(size)
                        values.append(sum(experiment.results[algo_name][key][metric]) / len(experiment.results[algo_name][key][metric]))
                line, = plt.plot(sizes, values, color=color, linestyle=experiment.line_styles[order], linewidth=2)
                lines.append(line)
                labels.append(algo_name)
            
            plt.yscale('log')
            plt.title(f"Algorithm Comparison (Small Lists)\n{order.capitalize()} Order - {ylabel}", pad=20)
            plt.xlabel("List Size (elements)", fontsize=12)
            plt.ylabel(ylabel, fontsize=12)
            plt.legend(lines, labels, fontsize=10, framealpha=0.9)
            plt.grid(True, which="both", alpha=0.3)
            filename = f"comparison_{metric}_{order}_small_{timestamp}.png"
            plt.savefig(filename, dpi=150, bbox_inches='tight')
            logging.info(f"Saved graph: {filename}")
            plt.close()

def plot_individual_algorithm_graphs(experiment, timestamp):
    logging.info("Generating individual algorithm graphs")
    for algo in experiment.algorithms:
        for metric, ylabel in [('time', 'Time (ms)'), ('comparisons', 'Comparisons')]:
            plt.figure(figsize=(10, 6))
            for order in experiment.orders:
                sizes = []
                values = []
                for size in experiment.large_sizes:
                    key = f"{order}_{size}"
                    if key in experiment.results[algo.name]:
                        sizes.append(size)
                        values.append(sum(experiment.results[algo.name][key][metric])/len(experiment.results[algo.name][key][metric]))
                plt.plot(sizes, values, 
                        linestyle=experiment.line_styles[order],
                        linewidth=2,
                        label=f"{order.capitalize()} Order")
            
            plt.title(f"{algo.name} Performance\n{ylabel}", pad=20)
            plt.xlabel("List Size (elements)", fontsize=12)
            plt.ylabel(ylabel, fontsize=12)
            plt.legend(fontsize=10, framealpha=0.9)
            plt.grid(True, alpha=0.3)
            filename = f"individual_{algo.name.lower().replace(' ', '_')}_{metric}_{timestamp}.png"
            plt.savefig(filename, dpi=150, bbox_inches='tight')
            logging.info(f"Saved graph: {filename}")
            plt.close()

            plt.figure(figsize=(10, 6))
            for order in experiment.orders:
                sizes = []
                values = []
                for size in experiment.small_sizes:
                    key = f"{order}_{size}_small"
                    if key in experiment.results[algo.name]:
                        sizes.append(size)
                        values.append(sum(experiment.results[algo.name][key][metric])/len(experiment.results[algo.name][key][metric]))
                plt.plot(sizes, values, 
                        linestyle=experiment.line_styles[order],
                        linewidth=2,
                        label=f"{order.capitalize()} Order")
            
            plt.title(f"{algo.name} Performance (Small Lists)\n{ylabel}", pad=20)
            plt.xlabel("List Size (elements)", fontsize=12)
            plt.ylabel(ylabel, fontsize=12)
            plt.legend(fontsize=10, framealpha=0.9)
            plt.grid(True, alpha=0.3)
            filename = f"individual_{algo.name.lower().replace(' ', '_')}_{metric}_small_{timestamp}.png"
            plt.savefig(filename, dpi=150, bbox_inches='tight')
            logging.info(f"Saved graph: {filename}")
            plt.close()

def plot_special_cases(experiment, timestamp):
    logging.info("Generating special case graphs")
    plt.figure(figsize=(10, 6))
    for order in ['ascending', 'descending']:
        sizes = []
        values = []
        for size in experiment.large_sizes:
            key = f"{order}_{size}"
            if key in experiment.results['Insertion Sort']:
                sizes.append(size)
                values.append(sum(experiment.results['Insertion Sort'][key]['time'])/len(experiment.results['Insertion Sort'][key]['time']))
        plt.plot(sizes, values, 
                linestyle=experiment.line_styles[order],
                linewidth=2,
                label=f"{order.capitalize()} Order")
    
    plt.title("Insertion Sort: Best vs Worst Case\nTime (ms)", pad=20)
    plt.xlabel("List Size (elements)", fontsize=12)
    plt.ylabel("Time (ms)", fontsize=12)
    plt.legend(fontsize=10, framealpha=0.9)
    plt.grid(True, alpha=0.3)
    filename = f"special_insertion_sort_best_worst_{timestamp}.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    logging.info(f"Saved graph: {filename}")
    plt.close()

    plt.figure(figsize=(10, 6))
    for order in ['random', 'ascending']:
        sizes = []
        values = []
        for size in experiment.large_sizes:
            key = f"{order}_{size}"
            if key in experiment.results['Quick Sort']:
                sizes.append(size)
                values.append(sum(experiment.results['Quick Sort'][key]['time'])/len(experiment.results['Quick Sort'][key]['time']))
        plt.plot(sizes, values, 
                linestyle=experiment.line_styles[order],
                linewidth=2,
                label=f"{order.capitalize()} Order")
    
    plt.title("Quick Sort: Pivot Impact\nTime (ms)", pad=20)
    plt.xlabel("List Size (elements)", fontsize=12)
    plt.ylabel("Time (ms)", fontsize=12)
    plt.legend(fontsize=10, framealpha=0.9)
    plt.grid(True, alpha=0.3)
    filename = f"special_quick_sort_pivot_impact_{timestamp}.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    logging.info(f"Saved graph: {filename}")
    plt.close()

    plt.figure(figsize=(10, 6))
    for order in experiment.orders:
        sizes = []
        values = []
        for size in experiment.large_sizes:
            key = f"{order}_{size}"
            if key in experiment.results['Merge Sort']:
                sizes.append(size)
                values.append(sum(experiment.results['Merge Sort'][key]['time'])/len(experiment.results['Merge Sort'][key]['time']))
        plt.plot(sizes, values, 
                linestyle=experiment.line_styles[order],
                linewidth=2,
                label=f"{order.capitalize()} Order")
    
    plt.title("Merge Sort: Consistency\nTime (ms)", pad=20)
    plt.xlabel("List Size (elements)", fontsize=12)
    plt.ylabel("Time (ms)", fontsize=12)
    plt.legend(fontsize=10, framealpha=0.9)
    plt.grid(True, alpha=0.3)
    filename = f"special_merge_sort_consistency_{timestamp}.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    logging.info(f"Saved graph: {filename}")
    plt.close()