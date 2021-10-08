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

    def calc_gap_days(self) -> int:
        gap_days: int = 0
        more_than_next_day: int = 1

        # getting only the project objects into a list 
        project_list: list = []
        for project in self.projects:
            project_list.append(self.projects[project])
        
        # use calc days function to check between start and end dates for gap
        # uses zero offset since extra day doesnt need to be included
        for i in range(len(project_list)-1):
            current_gap: int = project_list[i].calc_days(project_list[i+1].start_date, project_list[i].end_date, 0)
            if current_gap > more_than_next_day:
                gap_days += current_gap
        return gap_days

    def calc_full_days(self) -> int:
        # value to return
        total: int = 0

        # use method for each project to get days and add to total
        for project in self.projects:
            total += self.projects[project].project_full_days()

        return total

    # returns the total for entire project set
    def calc_reimbursement(self) -> int:
        pass
        # return (full_days * self.projects[project].full_rate) + (travel_days * self.projects[project].travel_rate) + (gap_days * self.projects[project].travel_rate)