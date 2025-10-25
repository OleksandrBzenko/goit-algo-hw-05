from collections import Counter


def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return list(filter(lambda log: log.get("level")== level, logs))

def count_logs_by_level(logs: list) -> dict:
    """Підрахунок записів за рівнями логування."""
    return Counter(log.get("level")for log in logs)
