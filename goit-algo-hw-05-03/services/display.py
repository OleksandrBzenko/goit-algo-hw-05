def display_log_counts(counts: dict):
    """Вивід статистики у вигляді таблиці."""
    print("Рівень логування | Кількість")
    print("-----------------| ----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")