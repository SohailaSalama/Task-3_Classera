from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, UniqueConstraint, CHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    enrolled_on = Column(Date, nullable=False)

    enrollments = relationship("Enrollment", back_populates="student")

    def __str__(self):
        return f"Student(id={self.id}, name='{self.name}')"

class Instructor(Base):
    __tablename__ = 'instructors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)

    courses = relationship("Course", back_populates="instructor")

    def __str__(self):
        return f"Instructor(id={self.id}, name='{self.name}')"

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    description = Column(Text)
    instructor_id = Column(Integer, ForeignKey('instructors.id'))

    instructor = relationship("Instructor", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")

    def __str__(self):
        return f"Course(id={self.id}, title='{self.title}')"

class Enrollment(Base):
    __tablename__ = 'enrollments'
    __table_args__ = (UniqueConstraint('student_id', 'course_id', name='_student_course_uc'),)

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    enrolled_date = Column(Date, nullable=False)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
    grade = relationship("Grade", back_populates="enrollment", uselist=False)

    def __str__(self):
        return f"Enrollment(student_id={self.student_id}, course_id={self.course_id})"

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    enrollment_id = Column(Integer, ForeignKey('enrollments.id'))
    grade = Column(CHAR(2))
    graded_on = Column(Date)

    enrollment = relationship("Enrollment", back_populates="grade")

    def __str__(self):
        return f"Grade(enrollment_id={self.enrollment_id}, grade='{self.grade}')"
