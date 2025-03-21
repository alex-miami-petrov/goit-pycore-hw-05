from datetime import datetime
from functools import wraps
import argparse, sys
from collections import defaultdict

def log_parser_decorator(level: str = None):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(line: str):
            log_data = func(line)
            return log_data
        return wrapper
    return actual_decorator

def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)
    if len(parts) >= 4:
        return {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": parts[3].strip(),
        }
    return {}

@log_parser_decorator()
def process_log_line(line: str) -> dict:
    return parse_log_line(line)

def load_and_process_logs(filepath: str, level: str = None):
    log_counts = defaultdict(int)
    log_details = defaultdict(list)
    try:
        with open(filepath, "r") as f:
            for line in f:
                log_data = process_log_line(line)
                if log_data:
                    log_counts[log_data["level"]] += 1
                    if level is None or log_data["level"] == level:
                        log_details[log_data["level"]].append(f"{log_data['date']} {log_data['time']} - {log_data['message']}")

        print("{:<16} | {:<8}".format("Рівень логування", "Кількість"))
        print("-----------------|----------")
        for log_level, count in log_counts.items():
            print("{:<16} | {:<8}".format(log_level, count))

        if level:
            print(f"\nДеталі логів для рівня '{level}':")
            for detail in log_details[level]:
                print(detail)

    except FileNotFoundError:
        print(f"Помилка: Файл '{filepath}' не знайдено.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Аналізатор логів")
    parser.add_argument("log_file", help="Шлях до логу")
    parser.add_argument("level", nargs="?", help="Фільтрувати логи за рівнем")

    args = parser.parse_args()

    load_and_process_logs(args.log_file, args.level.upper() if args.level else None)

if __name__ == "__main__":
    main()