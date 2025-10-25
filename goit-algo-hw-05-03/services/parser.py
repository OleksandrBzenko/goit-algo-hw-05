def parse_log_line(line: str) -> dict:
    """Розбиває рядок логу на компоненти: дата, час, рівень, повідомлення."""
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None
    deta, time, level, message = parts
    return {"date": deta, 
            "time": time, 
            "level": level, 
            "message": message
        }


def load_logs(file_path: str) -> list:
    """Завантажує лог-файл і парсить рядки."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [log for line in file if (log := parse_log_line(line))]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    
