import logging
from experiment import SortingExperiment
from plotting import plot_comparison_graphs, plot_individual_algorithm_graphs, plot_special_cases
from utils import setup_logging
from datetime import datetime

def main():
    setup_logging()
    logging.info("Starting sorting experiment")
    experiment = SortingExperiment()
    experiment.run_experiments()
    experiment.verify_results()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plot_comparison_graphs(experiment, timestamp)
    plot_individual_algorithm_graphs(experiment, timestamp)
    plot_special_cases(experiment, timestamp)
    experiment.log_numerical_results()
    logging.info("Experiments completed. Please check the generated graphs and numerical results in the logs.")
    print("\nFor your report, include:")
    print("- The generated graphs (saved as PNG files)")
    print("- The numerical results from the logs (shown above)")
    print("- Analysis comparing the algorithms' performance")

if __name__ == "__main__":
    main()