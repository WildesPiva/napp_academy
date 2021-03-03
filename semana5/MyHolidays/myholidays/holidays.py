from datetime import date, datetime

from attr import dataclass

class MyCalendar:
    def __init__(self, *args):
        self.datas = []
        self.parse_dates(args)

    
    def parse_dates(self, dates_to_parse):
        for item in dates_to_parse:
            if isinstance(item, date):
                self.datas.append(item)
            elif isinstance(item, str):
                try:
                    item = datetime.strptime(item, '%d/%m/%Y').date()
                    self.datas.append(item)
                except ValueError:
                    continue


    def add_holiday(self, *args):
        self.parse_dates(args)

            