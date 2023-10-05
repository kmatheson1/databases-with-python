from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository



# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/student_directory_2.sql")


cohort_repository = CohortRepository(connection)

r1_students = cohort_repository.find_with_student(2)

print(r1_students)