from datetime import datetime

tuesdays_in_seasons = [
    "2023-09-12",
    "2023-09-19",
    "2023-09-26",
    "2023-10-03",
    "2023-10-10",
    "2023-10-17",
    "2023-10-24",
    "2023-10-31",
    "2023-11-07",
    "2023-11-14",
    "2023-11-21",
    "2023-11-28",
    "2023-12-05",
    "2023-12-12",
    "2023-12-19",
    "2023-12-26",
    "2023-01-02",
    
]

def get_current_week():
    week_one = datetime(2023,9,12)
    date = datetime.now() 
    if date < week_one:
        date = week_one
    formatted_date = datetime.strftime(date, '%Y-%m-%d')
    print(formatted_date)
    return tuesdays_in_seasons.index(formatted_date) + 1

