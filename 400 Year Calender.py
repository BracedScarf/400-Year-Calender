import datetime
from calendar import month_name

# Utility function to determine if a year is a leap year
def is_leap_year(year):
    """
    Determine if a year is a leap year in the Gregorian calendar.
    Returns True if leap year, False otherwise.
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    return True

# Utility function to get the number of days in a month
def get_days_in_month(month, year):
    """
    Return the number of days in the given month and year.
    Accounts for leap years in February.
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days_in_month[month - 1]

# Utility function to get the first day of the month (0=Sunday, 1=Monday, ..., 6=Saturday)
def get_first_day_of_month(year, month):
    """
    Return the day of the week for the first day of the given month and year.
    Uses datetime to calculate the day (0=Sunday, 1=Monday, ..., 6=Saturday).
    """
    try:
        first_day = datetime.date(year, month, 1)
        weekday = first_day.weekday()  # 0=Monday, ..., 6=Sunday
        return (weekday + 1) % 7 if weekday != 6 else 0  # Adjust to Sunday=0
    except ValueError:
        raise ValueError("Invalid year or month")

# Function to print a single month's calendar
def print_month_calendar(year, month):
    """
    Print a text-based calendar for the given month and year.
    """
    # Print month and year header
    print(f"\n{month_name[month]} {year}".center(20))
    print("Su Mo Tu We Th Fr Sa")

    # Get first day and total days
    first_day = get_first_day_of_month(year, month)
    days = get_days_in_month(month, year)

    # Calculate total positions and lines needed
    max_positions = first_day + days - 1
    total_lines = (max_positions // 7) + (1 if max_positions % 7 else 0)

    # Print calendar
    current_day = 1
    for week in range(total_lines):
        line = ""
        for day in range(7):
            position = week * 7 + day
            if position < first_day or current_day > days:
                line += "   "
            else:
                line += f"{current_day:2} "
                current_day += 1
        print(line)

# Function to print a full year's calendar
def print_year_calendar(year):
    """
    Print calendars for all 12 months of the given year.
    """
    try:
        for month in range(1, 13):
            print_month_calendar(year, month)
    except ValueError as e:
        print(f"Error: {e}")

# Main function to handle user input and program flow
def main():
    """
    Main function to interact with the user and generate calendars.
    """
    while True:
        try:
            # Get year input
            year_input = input("Enter a year (e.g., 2025) or 'quit' to exit: ")
            if year_input.lower() == 'quit':
                break
            year = int(year_input)
            if year < 1582:  # Gregorian calendar starts from 1582
                print("Please enter a year after 1582 (Gregorian calendar).")
                continue

            # Get month input (optional)
            month_input = input("Enter a month (e.g., January) or leave blank for full year: ").strip().lower()
            if month_input:
                # Convert month name to number
                month_names = [m.lower() for m in month_name][1:]  # Skip empty string at index 0
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

# Unit tests for key functions
def run_tests():
    """
    Run unit tests to validate calendar functions.
    """
    # Test leap year function
    assert is_leap_year(2000) == True, "2000 should be a leap year"
    assert is_leap_year(1900) == False, "1900 should not be a leap year"
    assert is_leap_year(2024) == True, "2024 should be a leap year"
    assert is_leap_year(2025) == False, "2025 should not be a leap year"

    # Test days in month function
    assert get_days_in_month(2, 2024) == 29, "February 2024 should have 29 days"
    assert get_days_in_month(2, 2025) == 28, "February 2025 should have 28 days"
    assert get_days_in_month(1, 2025) == 31, "January 2025 should have 31 days"
    assert get_days_in_month(4, 2025) == 30, "April 2025 should have 30 days"

    # Test first day of month (example for known dates)
    assert get_first_day_of_month(2025, 1) == 3, "January 1, 2025 should be Wednesday (3)"
    print("All tests passed!")

if _name_ == "_main_":
    # Run tests before starting the program
    run_tests()
    print("Welcome to the 400-Year Calendar Generator!")
    main()