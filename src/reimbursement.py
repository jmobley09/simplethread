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
            return (True, )
        else:
            return False

    def calc_gap_days(self):
        gap_day: int = 0

    # returns the total for entire project set
    def calc_reimbursement(self) -> int:
        pass
        # return (full_days * self.projects[project].full_rate) + (travel_days * self.projects[project].travel_rate) + (gap_days * self.projects[project].travel_rate)

    # print(new_reimbursement.calc_days(project_set["project_2"].start_date, project_set["project_1"].end_date, -1)) #used for gap
    # print(new_reimbursement.calc_days(project_set["project_2"].end_date, project_set["project_2"].start_date, -1)) #used for full days