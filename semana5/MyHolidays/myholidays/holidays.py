from datetime import date, datetime

from attr import dataclass

class MyCalendar:
    def __init__(self, *args):
        self.args = args
        self.datas = []
        self.parse_dates()

    
    def parse_dates(self):
        for item in self.args:
            if isinstance(item, date):
                self.datas.append(item)
            elif isinstance(item, str):
                item = datetime.strptime(item, '%d/%m/%Y').date()
                self.datas.append(item)
            