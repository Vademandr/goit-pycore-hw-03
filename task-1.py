from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        old_date_obj = datetime.strptime(date, "%Y.%m.%d")
        current_date = datetime.today()
        numbers_day = current_date - old_date_obj
        return numbers_day.days
    except ValueError:
        return "Invalid date format. Enter date in 'YYYY-MM-DD' format."

print(get_days_from_today('2021.10.09'))