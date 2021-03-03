from datetime import date, datetime

class MyCalendar:
    def __init__(self, *args):
        self.datas = []
        self.parse_dates(args)


    def _extract_date(self, date_to_extract):
        if isinstance(date_to_extract, date):
            return date_to_extract
        elif isinstance(date_to_extract, str):
            try:
                return datetime.strptime(date_to_extract, '%d/%m/%Y').date()
            except ValueError:
                return None


    def parse_dates(self, dates_to_parse):
        for item in dates_to_parse:
            date_extracted = self._extract_date(item)
            if date_extracted and date_extracted not in self.datas:
                self.datas.append(date_extracted)


    def add_holiday(self, *args):
        self.parse_dates(args)


    def check_holiday(self, holiday):
        return True if self._extract_date(holiday) in self.datas else False