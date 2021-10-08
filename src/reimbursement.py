class Reimbursement():
    def __init__(self, projects: dict) -> None:
        self.projects: dict = projects
        self.full_days_high: int = 0
        self.full_days_low: int = 0
        self.travel_days_high: int = 0
        self.travel_days_low: int = 0

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

    def calc_full_days(self) -> None:
        # use method for each project to get days and add to total
        for project in self.projects:
            if self.projects[project].city_type == "High":
                self.full_days_high += self.projects[project].project_full_days()
            if self.projects[project].city_type == "Low":
                self.full_days_low += self.projects[project].project_full_days()

    # if there are multiple projects calculates gaps and adds to appropiate total
    def calc_gap(self) -> None:
        # calc days offset
        more_than_next_day: int = 1

        # getting only the project objects into a list 
        project_list: list = []
        for project in self.projects:
            project_list.append(self.projects[project])

        # use calc days function to check between start and end dates for gap
        # uses zero offset since extra day doesnt need to be included
        for i in range(len(project_list)-1):
            current_gap: int = project_list[i].calc_days(project_list[i+1].start_date, project_list[i].end_date, 0)
            # if there is a gap more than a day each side needs to be added to travel
            # each needs to be calculated seperately to ensure proper rate
            if current_gap > more_than_next_day:
                # adding travel day for end of project
                if project_list[i].city_type == "High":
                   self.travel_days_high += 1
                elif project_list[i].city_type == "Low":
                    self.travel_days_low += 1
                # adding travel day for start of next project
                if project_list[i+1].city_type == "High":
                   self.travel_days_high += 1
                elif project_list[i+1].city_type == "Low":
                    self.travel_days_low += 1
            else:
                # check if either project has a high cost, if so adds the full day at that default
                if project_list[i].city_type == "High" or project_list[i+1].city_type == "High":
                   self.full_days_high += 2
                elif project_list[i].city_type == "Low" and project_list[i+1].city_type == "Low":
                    self.full_days_low += 2

    # adds in the first and last day to the appropiate total   
    def calc_travel_days(self) -> None:
        # defining to avoid magic numbers
        first_project: int = 0
        last_project: int = -1

        # getting only the project objects into a list 
        project_list: list = []
        for project in self.projects:
            project_list.append(self.projects[project])

        # determine first type so that first project in set can be travel day
        if project_list[first_project].city_type == "High":
                   self.travel_days_high += 1
        elif project_list[first_project].city_type == "Low":
                    self.travel_days_low += 1

        # determine last type so that last project in set can be travel day
        if project_list[last_project].city_type == "High":
                   self.travel_days_high += 1
        elif project_list[last_project].city_type == "Low":
                    self.travel_days_low += 1
        
    # returns the total for entire project set
    def calc_reimbursement(self) -> int:
        self.calc_full_days()
        self.calc_gap()
        self.calc_travel_days()
        # return (full_days * self.projects[project].full_rate) + (travel_days * self.projects[project].travel_rate) + (gap_days * self.projects[project].travel_rate)