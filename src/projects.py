from dateutil import parser

# class for manipulating projects with dates
class Project():
    def __init__(self, start: str, end: str) -> None:
        self.start = start
        self.end = end

    def calc_total_days(self) -> int:
        # defining values to avoid magic numbers
        to_minutes: int = 60
        to_hours: int = 60
        to_days: int = 24
        date_offset: int = 1

        # converting strings into date objects
        start_date: parser = parser.parse(self.start)
        end_date: parser = parser.parse(self.end)

        # the total between the dates represented in days
        # adding extra 1 to account for the last day not being included
        total_days: int = round(((end_date - start_date).total_seconds()) / to_minutes / to_hours / to_days) + date_offset

        return total_days