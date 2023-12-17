import os
import shutil
import argparse
import requests
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
TEMPLATES_DIR = Path(__file__).resolve().parents[1] / 'templates'

def get_year_options() -> list:
    return list(range(2016, datetime.today().year + 1))

def get_day_options() -> list:
    return list(range(1, 32))

def parse_args() -> argparse.Namespace:
    # Create an instance of ArgumentParser and add the year and day argument
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int, choices=get_year_options(), metavar='YEAR')
    parser.add_argument('day', type=int, choices=get_day_options(), metavar='DAY')
    args = parser.parse_args()

    return args

def add_files(path, year, day):
    inputs_path = Path(path, 'inputs')
    inputs_path.mkdir(parents=True, exist_ok=False)
    with open(Path(inputs_path, 'input.txt'), 'w') as f:
        f.write(pull_input(year, day))
    example_files =['example1.txt', 'example2.txt']
    for file in example_files:
        open(Path(inputs_path, file), 'x').close()
    shutil.copy(Path(TEMPLATES_DIR, '2023_day_template.py'), Path(path, 'solution.py'))

def pull_input(year, day):
    session_cookie = os.getenv("AOC_SESSION_COOKIE")
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session_cookie}
    response = requests.get(url, cookies=cookies)
    
    return response.text.strip('\n')


### Entry Point ###
def main():
    args = parse_args()
    new_day_path = Path(BASE_DIR, str(args.year), f"day_{str(args.day).zfill(2)}")
    try:
        new_day_path.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Folder already exists.  Please delete or choose a different day.")
        exit(1)
    add_files(new_day_path, args.year, args.day)
    

if __name__ == "__main__":
    main()