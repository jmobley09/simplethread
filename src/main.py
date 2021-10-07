from projects import Project
from reimbursement import Reimbursement

if __name__ == "__main__":
    project_set_1: dict = {
        "project_1": Project("9/1/20", "9/3/20", "Low")
    }
    project_set_2: dict = {
        "project_1": Project("9/1/20", "9/1/20", "Low"),
        "project_2": Project("9/2/20", "9/6/20", "High"),
        "project_3": Project("9/6/20", "9/8/20", "Low")
    }
    project_set_3: dict = {
        "project_1": Project("9/1/20", "9/3/20", "Low"),
        "project_2": Project("9/5/20", "9/7/20", "High"),
        "project_3": Project("9/8/20", "9/8/20", "High")
    }
    project_set_4: dict = {
        "project_1": Project("9/1/20", "9/1/20", "Low"),
        "project_2": Project("9/1/20", "9/1/20", "High"),
        "project_3": Project("9/2/20", "9/2/20", "High"),
        "project_4": Project("9/2/20", "9/3/20", "High")
    }

    reimbursement_1 = Reimbursement(project_set_1)
    # print(new_reimbursement.calc_days(project_set["project_2"].start_date, project_set["project_1"].end_date, -1)) #used for gap
    # print(new_reimbursement.calc_days(project_set["project_2"].end_date, project_set["project_2"].start_date, -1)) #used for full days