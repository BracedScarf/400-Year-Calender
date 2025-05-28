import datetime
from calendar import month_name

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    return True

def get_days_in_month(month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days_in_month[month - 1]

def get_first_day_of_month(year, month):
    try:
        first_day = datetime.date(year, month, 1)
        weekday = first_day.weekday()
        return (weekday + 1) % 7 if weekday != 6 else 0
    except ValueError:
        raise ValueError("Invalid year or month")

def print_month_calendar(year, month):
    print(f"\n{month_name[month]} {year}".center(20))
    print("Su Mo Tu We Th Fr Sa")

    first_day = get_first_day_of_month(year, month)
    days = get_days_in_month(month, year)

    # Get today's date
    today = datetime.date.today()
    is_current_month = (today.year == year and today.month == month)

    max_positions = first_day + days - 1
    total_lines = (max_positions // 7) + (1 if max_positions % 7 else 0)

    current_day = 1
    for week in range(total_lines):
        line = ""
        for day in range(7):
            position = week * 7 + day
            if position < first_day or current_day > days:
                line += "   "
            else:
                if is_current_month and current_day == today.day:
                    line += f"[{current_day:2}]"  # Highlight today
                else:
                    line += f"{current_day:2} "
                current_day += 1
        print(line)

def print_year_calendar(year):
    try:
        for month in range(1, 13):
            print_month_calendar(year, month)
    except ValueError as e:
        print(f"Error: {e}")

def main():
    while True:
        try:
            year_input = input("Enter a year (e.g., 2025) or 'quit' to exit: ")
            if year_input.lower() == 'quit':
                break
            year = int(year_input)
            if year < 1582:
                print("Please enter a year after 1582 (Gregorian calendar).")
                continue

            month_input = input("Enter a month (e.g., January) or leave blank for full year: ").strip().lower()
            if month_input:
                month_names = [m.lower() for m in month_name][1:]
                if month_input in month_names:
                    month = month_names.index(month_input) + 1
                    print_month_calendar(year, month)
                else:
                    print("Invalid month name. Please use full month names (e.g., January).")
            else:
                print_year_calendar(year)
        except ValueError:
            print("Please enter a valid year (numeric) and month (if provided).")
        except Exception as e:
            print(f"An error occurred: {e}")

def run_tests():
    assert is_leap_year(2000) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2024) == True
    assert is_leap_year(2025) == False

    assert get_days_in_month(2, 2024) == 29
    assert get_days_in_month(2, 2025) == 28
    assert get_days_in_month(1, 2025) == 31
    assert get_days_in_month(4, 2025) == 30

    assert get_first_day_of_month(2025, 1) == 3
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
    print("Welcome to the 400-Year Calendar Generator!")
    main()
