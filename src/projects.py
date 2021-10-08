from dateutil import parser

# class for manipulating projects with dates
class Project():
    def __init__(self, start: str, end: str, city_type: str) -> None:
        if city_type == "High":
            self.travel_rate: int = 55
            self.full_rate: int = 85
        elif city_type == "Low":
            self.travel_rate: int = 45
            self.full_rate: int = 75
        else:
            raise ValueError("Invalid City Type")

        # converting strings into date objects
        self.start_date: parser = parser.parse(start)
        self.end_date: parser = parser.parse(end)

    # used to calculate the days between two dates and the offset is used to either subtract or add date that might be needed
    def calc_days(self, date_one: parser, date_two: parser, date_offset: int) -> int:
        # defining values to avoid magic numbers
        to_minutes: int = 60
        to_hours: int = 60
        to_days: int = 24

        # the total between the dates represented in days
        # adding extra 1 to account for the last day not being included
        total_days: int = round(((date_one - date_two).total_seconds()) / to_minutes / to_hours / to_days) + date_offset

        return total_days

    # returns the number of each day in a project
    def project_full_days(self) -> int:
        # offset for helper function
        remove_last_day: int = -1

        days: int = self.calc_days(self.end_date, self.start_date, remove_last_day)

        # cannot be below zero, so only return if above zero
        if days > 0: 
            return days
        else:
            return 0 