from projects import Project
from reimbursement import Reimbursement

# dictionary to hold all of the projects
set_dict = {}

# gather information
def collect_project_info() -> None :
    print("Please input your project information")
    project_name: str = input("Project Name:")
    project_start: str = input("Project Start Date:")
    project_end: str = input("Project End Date:")
    project_city_type: str = input("Project City Type (High or Low):")

    # put into the set
    set_dict[project_name] = Project(project_start, project_end, (project_city_type).capitalize())
    additional_project()
# checks for additional projects
def additional_project() -> None:
    yes_list: list = ['Yes', 'YES', 'yes','Y', 'y']
    no_list: list = ['NO', 'no', 'No','n', 'N']
    answer: str = input("Additional Project to add to set?")
    if answer in yes_list:
        collect_project_info()
    elif answer in no_list:
        new_reimbursement: Reimbursement = Reimbursement(set_dict)
        print(f"\nTotal Reimbursement for Set: {new_reimbursement.calc_reimbursement()}\n")

if __name__ == "__main__":
    collect_project_info()