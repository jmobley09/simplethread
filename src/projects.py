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