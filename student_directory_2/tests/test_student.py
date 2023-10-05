from lib.student import Student


def test_student_constructs():
    student = Student(1, "Name", 1)
    assert student.id == 1
    assert student.name == "Name"
    assert student.cohort_id == 1

def test_equality():
    student1 = Student(1, "Name", 1)
    student2 = Student(1, "Name", 1)
    assert student1 == student2

def test_formats():
    student1 = Student(1, "Name", 1)
    assert str(student1) == "Student(1, Name, 1)"