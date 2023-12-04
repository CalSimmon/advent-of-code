import os
import subprocess
import argparse
from time import time
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
    tries = args.tries if args.tries != None else 3 
    total_year = 0.0
    year_path = Path(BASE_DIR, args.year)
    day_title_data = []
    day_exec_data = []
    for day in os.listdir(year_path):
        total_day_runs = 0
        for _ in range(tries):
            start = time()
            subprocess.run(['python3', Path(year_path, day) / 'solution.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            total_day_runs += time() - start
        day_average = (total_day_runs / tries)
        day_title_data.append(day)
        day_exec_data.append(day_average)
        total_year += day_average
        print("{}_{} took an average of {:.4f} seconds to run.".format(args.year, day, day_average))
    print("--------\n{} took a total of {:.4f} seconds to run.".format(args.year, total_year))

    plt.bar(day_title_data, day_exec_data)
    plt.xlabel('Day')
    plt.ylabel('Execution Time (s)')
    plt.title(f'Execution Time per Day for {args.year}')
    formatted_date_time = datetime.now().strftime('%Y%m%d_T%H%M%S')
    plt.savefig(f'{Path(SCRIPT_DIR, f"graphs/{formatted_date_time}-{args.year}_execution_times.png")}')

if __name__ == "__main__":
    main()