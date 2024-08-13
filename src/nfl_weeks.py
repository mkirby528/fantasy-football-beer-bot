from datetime import datetime, timedelta

date_format = '%Y-%m-%d'
tuesday_after_week_1 = datetime(2024, 9, 10)

tuesdays_in_season = [datetime.strftime(tuesday_after_week_1 + timedelta(days=7*i), date_format) for i in range(17)]

def get_current_week(date:str=None):
    week_one = tuesday_after_week_1
    today =  datetime.now()
    if today < week_one:
        today = week_one
    formatted_date = date or  datetime.strftime(today,date_format)
    return tuesdays_in_season.index(formatted_date) + 1

