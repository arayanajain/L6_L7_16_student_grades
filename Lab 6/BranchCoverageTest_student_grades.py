
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# Letter grade branches
def test_letter_grade_invalid_negative():
    with pytest.raises(ValueError):
        letter_grade(-5)


def test_letter_grade_invalid_above_100():
    with pytest.raises(ValueError):
        letter_grade(105)


def test_letter_grade_s():
    assert letter_grade(90) == "S"


def test_letter_grade_a():
    assert letter_grade(80) == "A"


def test_letter_grade_b():
    assert letter_grade(70) == "B"


def test_letter_grade_c():
    assert letter_grade(60) == "C"


def test_letter_grade_d():
    assert letter_grade(50) == "D"


def test_letter_grade_e():
    assert letter_grade(40) == "E"


def test_letter_grade_f():
    assert letter_grade(39) == "F"


# Final marks branches
def test_internal_marks_out_of_range():
    with pytest.raises(ValueError):
        final_marks(41, 30, False)


def test_external_marks_out_of_range():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)


def test_final_marks_without_project():
    assert final_marks(30, 40, False) == 70


def test_final_marks_with_project():
    assert final_marks(30, 40, True) == 75


def test_project_marks_capped():
    assert final_marks(40, 60, True) == 100


# Exam eligibility branches
def test_fees_not_paid():
    assert exam_eligibility(90, False, False) == "blocked"


def test_attendance_above_75():
    assert exam_eligibility(80, True, False) == "eligible"


def test_attendance_below_75_with_medical():
    assert exam_eligibility(70, True, True) == "eligible"


def test_attendance_below_75_without_medical():
    assert exam_eligibility(70, True, False) == "detained"


def test_attendance_below_65():
    assert exam_eligibility(60, True, True) == "detained"


def test_attendance_exactly_75():
    assert exam_eligibility(75, True, False) == "eligible"


def test_attendance_exactly_65_with_medical():
    assert exam_eligibility(65, True, True) == "eligible"
