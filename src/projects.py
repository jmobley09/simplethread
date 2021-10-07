from dateutil import parser

# class for manipulating projects with dates
class Project():
    def __init__(self, start: str, end: str, city: str) -> None:
        self.start = start
        self.end = end
        self.city = city

    def calc_full_days(self) -> int:
        # defining values to avoid magic numbers
        to_minutes: int = 60
        to_hours: int = 60
        to_days: int = 24

        # converting strings into date objects
        start_date: parser = parser.parse(self.start)
        end_date: parser = parser.parse(self.end)

        # return the difference between the dates represented in days
        return round(((end_date - start_date).total_seconds()) / to_minutes / to_hours / to_days) 
