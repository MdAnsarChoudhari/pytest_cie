from student import student_details

def test_student_details():
    expected_output=(
        "Student Name : John Doe\n"
        "Student ID : S1234\n"
        "Course Enrolled : Computer Science\n"
        "Acaemic Year : 2024-25"
    )

    assert student_details("S1234", "John Doe", "Computer Science", "2024-25")==expected_output