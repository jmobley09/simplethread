
from dateutil.parser import parser


class Reimbursement():
    def __init__(self, projects: dict) -> None:
        self.projects: dict = projects

    # helper function for checking for duplicates
    def checkIfDuplicates(self, listOfElems) -> bool:
        if len(listOfElems) == len(set(listOfElems)):
            return False
        else:
            return True

    # determine if there is an overlap based on start dates
    # add all the dates to a list and run through helper to check if duplicates
    # duplicate starte dates = overlap
    def is_overlap(self) -> bool:
        date_list: list = []
        for project in self.projects:
            # converting datetime object to string for easy comparison
            date_list.append(str(self.projects[project].start_date))

        # check for duplicates and return overlap if it exists
        if self.checkIfDuplicates(date_list):
            return True
        else:
            return False

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