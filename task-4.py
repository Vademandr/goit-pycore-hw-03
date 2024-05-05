from datetime import datetime, timedelta

def get_upcoming_birthdays(users: dict) -> dict:
    today = datetime.today().date()
    birthday_list = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        days_to_birthday = (birthday_this_year - today).days
        if 0 <= days_to_birthday < 7:
            if birthday_this_year.weekday() >= 5:
                days_to_birthday += 7 - birthday_this_year.weekday()
            congratulation_date = today + timedelta(days=days_to_birthday)
            birthday_list.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return birthday_list

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Yura Matc", "birthday": "2000.05.06"},
    {"name": "Vadym Sokol", "birthday": "1978.05.08"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)