from datetime import datetime, timedelta

date_format = '%Y-%m-%d'
tuesday_after_week_1 = datetime(2024, 9, 10)

tuesdays_in_season = [tuesday_after_week_1 + timedelta(days=7*i) for i in range(17)]

def get_current_week(date:str=None):
    week_one = tuesday_after_week_1
    today =  datetime.now()

    if today < week_one:
        today = week_one
    closest_tuesday = min(tuesdays_in_season, key=lambda x: (x>today, abs(x-today)) )
    if closest_tuesday >= today:
        return tuesdays_in_season.index(closest_tuesday) + 1
    else:
        return tuesdays_in_season.index(closest_tuesday)  + 2
    # formatted_date = date or  datetime.strftime(today,date_format)
    # return tuesdays_in_season.index(formatted_date) + 1

