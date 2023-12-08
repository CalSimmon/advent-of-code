import os
import subprocess
import argparse
from time import perf_counter
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = Path(__file__).resolve().parents[2]

def get_year_options() -> list:
    return [year for year in os.listdir(BASE_DIR) if year.isdigit()]

def parse_args() -> argparse.Namespace:
    # Create an instance of ArgumentParser and add the year argument
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=str, choices=get_year_options(), metavar='YEAR', help='The year of AoC that you want to check')
    parser.add_argument('-t', '--tries', type=int, nargs='?', metavar='TRIES', help='The number of times you want to try each script')
    args = parser.parse_args()

    return args

### Entry Point ###
def main():
    args = parse_args()
    tries = args.tries if args.tries != None else 3  # Set a default number of tries
    total_year = 0.0
    year_path = Path(BASE_DIR, args.year)  # Create a path for the year based on year argument
    day_title_data = []
    day_exec_data = []
    for day in os.listdir(year_path):
        if os.path.isdir(Path(year_path, day)):  # Ensure that the day is actually a folder
            total_day_runs = 0
            script_path = Path(year_path, day) / 'solution.py'
            for _ in range(tries):  # Run each script a number of times based on the tries argument and get average of all runs
                start = perf_counter()
                subprocess.run(['python3', script_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                total_day_runs += perf_counter() - start
            day_average = (total_day_runs / tries)
            day_title_data.append(day.replace('day_', ''))
            day_exec_data.append(day_average)
            total_year += day_average
            print("{}_{} took an average of {:.4f} seconds to run.".format(args.year, day, day_average))
    print("--------\n{} took a total of {:.4f} seconds to run.".format(args.year, total_year))

    # Set up graph and output to both the graphs folder for history and to the year folder for GitHub
    plt.bar(day_title_data, day_exec_data)
    plt.xlabel('Day')
    plt.ylabel('Execution Time (s)')
    plt.title(f'Execution Time per Day for {args.year}')
    formatted_date_time = datetime.now().strftime('%Y%m%d_T%H%M%S')
    plt.savefig(f'{Path(SCRIPT_DIR, f"graphs/{formatted_date_time}-{args.year}_execution_times.png")}')
    plt.savefig(f'{Path(BASE_DIR, f"{args.year}/{args.year}-current_execution_times.png")}')

if __name__ == "__main__":
    main()