import datetime
from datetime import date

class Logic:
    def __init__(self):
        self.date1=None
        self.date2=None



    def set_date1(self,year,month,day):
        self.date1=date(year,month,day)

    def set_date2(self,year,month,day):
        self.date2=date(year,month,day)



    def calculate_duration(self):
        delta=self.date2-self.date1
        total_days=delta.days
        years, days_remaining = divmod(total_days, 365)
        # Calculate the number of months
        months, days_remaining = divmod(days_remaining, 30)
        # Calculate the number of days
        days = days_remaining
        return years, months, days





