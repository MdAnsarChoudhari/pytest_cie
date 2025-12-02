import pytest

def student_details(id, name, course, year):
    result=(
        f"Student Name : {name}\n"
        f"Student ID : {id}\n"
        f"Course Enrolled : {course}\n"
        f"Acaemic Year : {year}"
    )

    return result


if __name__=="__main__":
    id="023"
    name="Ansar"
    course="BCA"
    year="2025-26"

    print(student_details(id, name, course, year))