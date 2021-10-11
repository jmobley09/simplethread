import pytest
from src.projects import Project
from src.reimbursement import Reimbursement

test_project_set_1: dict = {
        "project_1": Project("9/1/20", "9/3/20", "Low")
    } #total = 165
test_project_set_2: dict = {
        "project_1": Project("9/1/20", "9/1/20", "Low"),
        "project_2": Project("9/2/20", "9/6/20", "High"),
        "project_3": Project("9/6/20", "9/8/20", "Low")
    } #total = 590
test_project_set_3: dict = {
        "project_1": Project("9/1/20", "9/3/20", "Low"),
        "project_2": Project("9/5/20", "9/7/20", "High"),
        "project_3": Project("9/8/20", "9/8/20", "High")
    } #total = 445
test_project_set_4: dict = {
        "project_1": Project("9/1/20", "9/1/20", "Low"),
        "project_2": Project("9/1/20", "9/1/20", "High"),
        "project_3": Project("9/2/20", "9/2/20", "High"),
        "project_4": Project("9/2/20", "9/3/20", "High")
    } #total = 185
test_project_set_5: dict = {
        "project_1": Project("9/1/20", "9/3/20", "High")
    } #total = 165
class TestReimbursement():
    
    def test_calc_full_days(self):
        test_reimbursement: Reimbursement = Reimbursement(test_project_set_1)
        test_reimbursement.calc_full_days()
        assert test_reimbursement.full_days_low == 1

    # below tests the gap calulator and checks if the returned days is correct
    def test_calc_gap(self):
        test_reimbursement: Reimbursement = Reimbursement(test_project_set_3)
        test_reimbursement.calc_gap()
        assert test_reimbursement.travel_days_low == 1
        assert test_reimbursement.travel_days_high == 1

    def test_calc_gap_none(self):
        test_reimbursement: Reimbursement = Reimbursement(test_project_set_1)
        test_reimbursement.calc_gap()
        assert test_reimbursement.travel_days_low == 0

    # below test only calculates the travel days that not calculated by the gap function
    def test_calc_non_gap_travel_days_high(self):
        test_reimbursement: Reimbursement = Reimbursement(test_project_set_5)
        test_reimbursement.calc_travel_days()
        assert test_reimbursement.travel_days_high == 2

    def test_calc_non_gap_travel_days_low(self):
        test_reimbursement: Reimbursement = Reimbursement(test_project_set_1)
        test_reimbursement.calc_travel_days()
        assert test_reimbursement.travel_days_low == 2

    def test_calc_non_gap_travel_days_both(self):
        test_reimbursement: Reimbursement = Reimbursement(test_project_set_3)
        test_reimbursement.calc_travel_days()
        assert test_reimbursement.travel_days_low == 1
        assert test_reimbursement.travel_days_high == 1

    # below is testing the different sets going through the calculator
    def test_single_set(self):
        test_reimbursement_1: Reimbursement = Reimbursement(test_project_set_1)
        assert test_reimbursement_1.calc_reimbursement() == 165

    def test_concurrent_set(self):
        test_reimbursement_2: Reimbursement = Reimbursement(test_project_set_2)
        assert test_reimbursement_2.calc_reimbursement() == 590

    def test_gap_set(self):
        test_reimbursement_3: Reimbursement = Reimbursement(test_project_set_3)
        assert test_reimbursement_3.calc_reimbursement() == 445

    def test_overlap_set(self):
        test_reimbursement_4: Reimbursement = Reimbursement(test_project_set_4)
        assert test_reimbursement_4.calc_reimbursement() == 185