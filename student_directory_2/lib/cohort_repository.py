from lib.student import Student
from lib.cohort import Cohort

class CohortRepository():
    def __init__(self, connection):
        self._connection = connection 

    def find_with_student(self, cohort_id):
        rows = self._connection.execute(
            "SELECT cohorts.id as cohort_id, cohorts.name as cohort_name, cohorts.starting_date, students.id as student_id, students.name as student_name " \
            "FROM cohorts JOIN students ON cohorts.id = students.cohort_id " \
            "WHERE cohorts.id = %s", [cohort_id])
        students = []
        for row in rows:
            student = Student(row["student_id"], row["student_name"], row["cohort_id"])
            students.append(student)
        
        return Cohort(rows[0]["cohort_id"], rows[0]["cohort_name"], rows[0]["starting_date"], students)