from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student
from datetime import date

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    expected_starting_date = date(2023, 4, 9).strftime('%Y-%m-%d')
    cohort = repository.find_with_student(1)
    assert cohort == Cohort(1, "RA", expected_starting_date, [
        Student(3, "Kieran", 1)
    ])