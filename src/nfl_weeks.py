from datetime import datetime, timedelta

date_format = '%Y-%m-%d'
tuesday_after_week_1 = datetime(2024, 9, 10)
tuesdays_in_season = [tuesday_after_week_1 + timedelta(days=7*i) for i in range(17)]

def get_current_week(date:str=None):
    week_one = tuesday_after_week_1
    #get date in local time
    today  = datetime.now() - timedelta(hours=4) 
    print(today)
    if today < week_one:
        today = week_one
    closest_tuesday = min((t for t in tuesdays_in_season if t.date() >= today.date()), key=lambda x: abs(x - today))
    return tuesdays_in_season.index(closest_tuesday) + 1 
 

