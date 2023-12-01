import os
import subprocess
import argparse
from time import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

def get_year_options() -> list:
    return [year for year in os.listdir(BASE_DIR) if year.isdigit()]

def parse_args() -> argparse.Namespace:
    # Create an instance of ArgumentParser and add the year argument
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=str, choices=get_year_options(), metavar='YEAR')
    args = parser.parse_args()

    return args

### Entry Point ###
def main():
    args = parse_args()
    total_year = 0.0
    year_path = Path(BASE_DIR, args.year)
    for day in os.listdir(year_path):
        start = time()
        subprocess.run(['python3', Path(year_path, day) / 'solution.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time_taken = time() - start
        total_year += time_taken
        print("{}_{} took {:.4f} seconds to run.".format(args.year, day, time_taken))
    print("--------\n{} took a total of {:.4f} seconds to run.".format(args.year, total_year))

if __name__ == "__main__":
    main()