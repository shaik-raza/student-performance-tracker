from flask import Flask, render_template, request
from db import db, cursor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():

    roll_no = request.form["roll_no"]

    # ---------------- Student Details ----------------
    cursor.execute("""
        SELECT *
        FROM students
        WHERE roll_no = %s
    """, (roll_no,))

    student = cursor.fetchone()

    if not student:
        return "<h2>Student Not Found</h2>"

    student_id = student[0]
    branch = student[3]

    # ---------------- Student Marks ----------------
    cursor.execute("""
        SELECT
            subjects.subject_name,
            subjects.credits,
            marks.mid1,
            marks.mid2,
            marks.slip1,
            marks.slip2,
            marks.slip3,
            marks.assignment1,
            marks.assignment2,
            marks.attendance,
            marks.semester_exam,
            marks.total_marks,
            marks.grade,
            marks.grade_point

        FROM marks

        JOIN subjects
        ON marks.subject_id = subjects.subject_id

        WHERE marks.student_id = %s
    """, (student_id,))

    marks = cursor.fetchall()

    # ---------------- SGPA ----------------

    total_credit_points = 0
    total_credits = 0
    total_marks = 0

    for row in marks:

        credits = row[1]
        gp = row[13]
        total = row[11]

        total_credit_points += credits * gp
        total_credits += credits
        total_marks += total

    sgpa = round(total_credit_points / total_credits, 2)
    percentage = round(total_marks / len(marks), 2)

    # ---------------- Performance ----------------

    if sgpa >= 9:
        performance = "Excellent ⭐"
    elif sgpa >= 8:
        performance = "Very Good 🌟"
    elif sgpa >= 7:
        performance = "Good 👍"
    elif sgpa >= 6:
        performance = "Average 🙂"
    else:
        performance = "Needs Improvement 📚"

    # ---------------- PASS / FAIL ----------------

    result_status = "PASS"

    for row in marks:
        if row[12] == "F":
            result_status = "FAIL"
            break

    # ====================================================
    #                OVERALL RANK
    # ====================================================

    cursor.execute("""

    SELECT
        marks.student_id,
        ROUND(SUM(subjects.credits*marks.grade_point)/SUM(subjects.credits),2) AS sgpa

    FROM marks

    JOIN subjects
    ON marks.subject_id=subjects.subject_id

    GROUP BY marks.student_id

    ORDER BY sgpa DESC

    """)

    all_students = cursor.fetchall()

    overall_rank = 1

    for record in all_students:

        if record[0] == student_id:
            break

        overall_rank += 1

    total_students = len(all_students)

    # ====================================================
    #                BRANCH RANK
    # ====================================================

    cursor.execute("""

    SELECT
        marks.student_id,
        ROUND(SUM(subjects.credits*marks.grade_point)/SUM(subjects.credits),2) AS sgpa

    FROM marks

    JOIN students
    ON marks.student_id=students.id

    JOIN subjects
    ON marks.subject_id=subjects.subject_id

    WHERE students.branch=%s

    GROUP BY marks.student_id

    ORDER BY sgpa DESC

    """,(branch,))

    branch_students = cursor.fetchall()

    branch_rank = 1

    for record in branch_students:

        if record[0] == student_id:
            break

        branch_rank += 1

    branch_strength = len(branch_students)

    # ====================================================

    is_topper = (branch_rank == 1)

    # ====================================================

    return render_template(
        "result.html",
        student=student,
        marks=marks,
        sgpa=sgpa,
        percentage=percentage,
        performance=performance,
        result=result_status,

        overall_rank=overall_rank,
        total_students=total_students,

        branch_rank=branch_rank,
        branch_strength=branch_strength,

        is_topper=is_topper
    )


if __name__ == "__main__":
    app.run(debug=True)