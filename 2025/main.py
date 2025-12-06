import argparse
import importlib
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs")

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-d", "--day", type=int, help="Day number to run")
group.add_argument("-a", "--all", action="store_true", help="Run all days")
parser.add_argument("-t", "--test", action="store_true", help="Run example test")
parser.add_argument(
    "-p", "--part", type=int, choices=[1, 2], help="Optional: Part 1 or 2"
)
parser.add_argument(
    "-e",
    "--example",
    type=int,
    nargs="?",
    const=1,
    default=None,
    help="Optional: Run with example input (default: 1)",
)

args = parser.parse_args()


def get_input_file_name(day, example):
    if not example:
        return Path(INPUT_PATH, f"day_{day:02d}/input.txt")
    else:
        return Path(INPUT_PATH, f"day_{day:02d}/example{example}.txt")


def run_day(day_number, part=None, example=None, test=False):
    try:
        module = importlib.import_module(f"solutions.day_{day_number:02d}")
    except ModuleNotFoundError:
        print(f"Day {day_number} not implemented")
        return False

    if test:
        module.test(part=part, input_path=get_input_file_name(day_number, 1))
    else:
        module.solve(part=part, input_path=get_input_file_name(day_number, example))
    return True


if args.all:
    for day in range(1, 26):
        print(f"--- Day {day} ---")
        run_day(day, args.part, args.example)
        print()
else:
    run_day(args.day, args.part, args.example, args.test)
