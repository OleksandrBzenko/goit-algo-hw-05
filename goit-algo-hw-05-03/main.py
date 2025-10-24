import sys
from services import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py path/to/logfile.log [level]")
        return
    
    file_path = sys.argv[1]
    logs = load_logs(file_path)
    if logs is None:
        return # зупинка, якщо файл не знайдено або помилка
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # показати логи певного рівня, в даному випадку 2й арг. коман. радка
    if len(sys.argv) > 2:
        level = sys.argv[2]
        filtered = filter_logs_by_level(logs, level)
        print(f"\nЛоги рівня '{level.upper()}':")
        for log in filtered:
            print("f{log['date]} {log['time]} {log['message]}")





if __name__ == "__main__":
    main()