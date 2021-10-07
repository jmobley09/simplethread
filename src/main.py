from projects import Project
from reimbursement import Reimbursement

if __name__ == "__main__":
    project_set_1: dict = {
        "project_1": Project("9/1/20", "9/3/20", "Low")
    } #total = 165
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
    reimbursement_2 = Reimbursement(project_set_2)
    reimbursement_3 = Reimbursement(project_set_3)
    reimbursement_4 = Reimbursement(project_set_4)
    # print(reimbursement_1.calc_gap_days())
    # print(reimbursement_2.calc_gap_days())
    # print(reimbursement_3.calc_gap_days())
    print(reimbursement_4.calc_gap_days())