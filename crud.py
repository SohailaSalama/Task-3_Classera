from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Instructor, Course, Enrollment, Grade
from datetime import date

# Connect to DB
engine = create_engine('sqlite:///lms.db')
Session = sessionmaker(bind=engine)
session = Session()

# CRUD Functions
def add_student(name, email):
    student = Student(name=name, email=email, enrolled_on=date.today())
    session.add(student)
    session.commit()
    return student

def enroll_student(student_id, course_id):
    enrollment = Enrollment(student_id=student_id, course_id=course_id, enrolled_date=date.today())
    session.add(enrollment)
    session.commit()
    return enrollment

def assign_grade(enrollment_id, grade):
    g = Grade(enrollment_id=enrollment_id, grade=grade, graded_on=date.today())
    session.add(g)
    session.commit()
    return g

def get_students_in_course(course_id):
    enrollments = session.query(Enrollment).filter_by(course_id=course_id).all()
    return [e.student for e in enrollments]

def get_courses_for_instructor(instructor_id):
    return session.query(Course).filter_by(instructor_id=instructor_id).all()

# Example usage
if __name__ == "__main__":
    # ======== Instructors ========
    instructors_data = [
        ("John Doe", "john@example.com"),
        ("Jane Smith", "jane@example.com"),
        ("Ahmed Ali", "ahmed@example.com")
    ]
    instructors = []
    for name, email in instructors_data:
        instructor = session.query(Instructor).filter_by(email=email).first()
        if not instructor:
            instructor = Instructor(name=name, email=email)
            session.add(instructor)
            session.commit()
        instructors.append(instructor)

    # ======== Courses ========
    courses_data = [
        ("Python 101", "Intro to Python", instructors[0].id),
        ("Data Science Basics", "Learn data analysis and visualization", instructors[1].id),
        ("Web Development", "HTML, CSS, JavaScript", instructors[2].id)
    ]
    courses = []
    for title, desc, instr_id in courses_data:
        course = session.query(Course).filter_by(title=title).first()
        if not course:
            course = Course(title=title, description=desc, instructor_id=instr_id)
            session.add(course)
            session.commit()
        courses.append(course)

    # ======== Students ========
    students_data = [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com"),
        ("Dina", "dina@example.com")
    ]
    students = []
    for name, email in students_data:
        student = session.query(Student).filter_by(email=email).first()
        if not student:
            student = Student(name=name, email=email, enrolled_on=date.today())
            session.add(student)
            session.commit()
        students.append(student)

    # ======== Enrollments & Grades ========
    enrollments_data = [
        (students[0].id, courses[0].id, "A+"),
        (students[1].id, courses[0].id, "B"),
        (students[2].id, courses[1].id, "A"),
        (students[3].id, courses[2].id, "B+"),
        (students[0].id, courses[1].id, "A"),
    ]
    for student_id, course_id, grade_value in enrollments_data:
        enrollment = session.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
        if not enrollment:
            enrollment = Enrollment(student_id=student_id, course_id=course_id, enrolled_date=date.today())
            session.add(enrollment)
            session.commit()
        if not enrollment.grade:
            g = Grade(enrollment_id=enrollment.id, grade=grade_value, graded_on=date.today())
            session.add(g)
            session.commit()

    # ======== Display Data ========
    print("📚 Students in Python 101:")
    for student in get_students_in_course(courses[0].id):
        print(student)

    print("\n📘 Courses taught by Jane Smith:")
    for course in get_courses_for_instructor(instructors[1].id):
        print(course)
