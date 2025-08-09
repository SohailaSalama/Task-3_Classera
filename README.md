# Task-3_Classera
Convert SQL Schema to Python ORM Models (LMS System)
# 🏫 Convert SQL Schema to Python ORM Models (LMS System)
---

## 📘 Part 1: SQL Schema  
**You must convert this into ORM models:**

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    enrolled_on DATE NOT NULL
);

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    instructor_id INTEGER REFERENCES instructors(id)
);

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    course_id INTEGER REFERENCES courses(id),
    enrolled_date DATE NOT NULL,
    UNIQUE(student_id, course_id)
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    enrollment_id INTEGER REFERENCES enrollments(id),
    grade CHAR(2),

## 2️⃣ Ensure
- **Data types** and **constraints** are accurately reflected from the SQL schema.  
- Correctly implement **relationships** such as:
  - `ForeignKey`
  - `OneToMany`
  - `ManyToMany`
- Enforce constraints like:
  - `UNIQUE`
  - `NOT NULL`

---

## 3️⃣ Implement CRUD Operations
- Add a new **student**
- Enroll a student in a **course**
- Assign a **grade**
- Get **all students** in a course
- Get **all courses** for an instructor

---

## 4️⃣ Bonus
- Ensure `OneToMany` and `ManyToMany` relationships are implemented correctly  
- Implement `__str__()` methods for each model for **pretty printing**  
- Add **validation logic** (e.g., prevent duplicate enrollments manually)  
- Provide **3 example inserts** for:
  - Students  
  - Instructors  
  - Courses  
  - Enrollments  
  - Grades

---

## 📦 Deliverables
- Python ORM code for **all five tables**  
- Database **initialization script**

