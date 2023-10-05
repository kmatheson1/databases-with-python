from lib.cohort import Cohort

def test_cohort_constructs():
    cohort = Cohort(1, "Name", "09/12/23")
    assert cohort.id == 1
    assert cohort.name == "Name"
    assert cohort.starting_date == "09/12/23"

def test_equality():
    cohort1 = Cohort(1, "Name", "09/12/23")
    cohort2 = Cohort(1, "Name", "09/12/23")
    assert cohort1 == cohort2

def test_formats():
    cohort = Cohort(1, "Name", "09/12/23")
    assert str(cohort) == 'Cohort(1, Name, 09/12/23)'