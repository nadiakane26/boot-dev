from datetime import datetime

def sort_dates(dates):
    """ dates: MONTH_DAY_YEAR format dates as a list of strings."""
    dates.sort(key=lambda date: datetime.strptime(date, "%m-%d-%Y"))
    return dates

# def sort_dates(dates):
#     return sorted(dates, key=format_date)


# def format_date(date):
#     month, day, year = date.split("-")
#     return year + month + day
