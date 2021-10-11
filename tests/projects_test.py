import pytest
from src.projects import Project

test_start: str = '9/1/15'
test_end: str = '9/3/15'
test_city: str = 'High'
test_project: Project = Project(test_start, test_end, test_city)

class TestProjects():
    def test_city_validation_error(self):
        with pytest.raises(ValueError) as e_info: 
            test_error = Project(test_start, test_end, 'test')
            
        assert "Invalid City Type" in str(e_info.value)

    # test that calc days returns antipated value given to dates
    def test_calc_days(self):
        test_offset: int = 0
        assert test_project.calc_days(test_project.end_date, test_project.start_date, test_offset) == 2

    def test_project_full_days(self):
        returned_days = test_project.project_full_days()
        assert returned_days == 1
