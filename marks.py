import mysql.connector
import random

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="raza.1290",      # Replace with your MySQL password
    database="student_tracker"
)

cursor = db.cursor()

# Get all students
cursor.execute("DELETE FROM marks")
db.commit()
cursor.execute("SELECT id, branch FROM students")
students = cursor.fetchall()


for student in students:

    student_id = student[0]
    branch = student[1]

    # Get subjects of the student's branch
    cursor.execute(
        "SELECT subject_id FROM subjects WHERE branch=%s",
        (branch,)
    )

    subjects = cursor.fetchall()

    for subject in subjects:

        subject_id = subject[0]

        # Decide student category
        category = random.choices(
            ["topper", "average", "weak"],
            weights=[20, 60, 20]
        )[0]

        if category == "topper":

            mid1 = random.randint(17,20)
            mid2 = random.randint(17,20)

            slip1 = random.randint(4,5)
            slip2 = random.randint(4,5)
            slip3 = random.randint(4,5)

            assignment1 = random.randint(9,10)
            assignment2 = random.randint(9,10)

            attendance = random.randint(85,95)

            semester_exam = random.randint(50,60)

        elif category == "average":

            mid1 = random.randint(12,17)
            mid2 = random.randint(12,17)

            slip1 = random.randint(3,5)
            slip2 = random.randint(2,5)
            slip3 = random.randint(3,5)

            assignment1 = random.randint(6,9)
            assignment2 = random.randint(6,9)

            attendance = random.randint(72,85)

            semester_exam = random.randint(36,50)

        else:

            mid1 = random.randint(7,12)
            mid2 = random.randint(7,12)

            slip1 = random.randint(1,4)
            slip2 = random.randint(1,4)
            slip3 = random.randint(1,4)

            assignment1 = random.randint(4,7)
            assignment2 = random.randint(4,7)

            attendance = random.randint(55,75)

            semester_exam = random.randint(25,40)

        # Calculations

        mid_avg = (mid1 + mid2) / 2

        slips = sorted([slip1, slip2, slip3], reverse=True)

        slip_avg = (slips[0] + slips[1]) / 2

        assignment_avg = (assignment1 + assignment2) / 2

        if attendance >= 85:
            attendance_marks = 5
        elif attendance >= 80:
            attendance_marks = 4
        elif attendance >= 75:
            attendance_marks = 3
        elif attendance >= 70:
            attendance_marks = 2
        else:
            attendance_marks = 0

        total = (
            mid_avg
            + slip_avg
            + assignment_avg
            + attendance_marks
            + semester_exam
        )

        # Grade

        if total >= 90:
            grade = "O"
            gp = 10
        elif total >= 80:
            grade = "A+"
            gp = 9
        elif total >= 70:
            grade = "A"
            gp = 8
        elif total >= 60:
            grade = "B+"
            gp = 7
        elif total >= 50:
            grade = "B"
            gp = 6
        elif total >= 40:
            grade = "C"
            gp = 5
        else:
            grade = "F"
            gp = 0

        cursor.execute("""
        INSERT INTO marks(
        student_id,
        subject_id,
        mid1,
        mid2,
        slip1,
        slip2,
        slip3,
        assignment1,
        assignment2,
        attendance,
        semester_exam,
        total_marks,
        grade,
        grade_point
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            student_id,
            subject_id,
            mid1,
            mid2,
            slip1,
            slip2,
            slip3,
            assignment1,
            assignment2,
            attendance,
            semester_exam,
            round(total,2),
            grade,
            gp
        ))

db.commit()

print("✅ Marks Generated Successfully!")

cursor.close()
db.close()