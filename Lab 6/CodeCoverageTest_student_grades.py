
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# Letter grade tests
def test_s_grade():
    assert letter_grade(95) == "S"


def test_a_grade():
    assert letter_grade(85) == "A"


def test_b_grade():
    assert letter_grade(75) == "B"


def test_c_grade():
    assert letter_grade(65) == "C"


def test_d_grade():
    assert letter_grade(55) == "D"


def test_e_grade():
    assert letter_grade(45) == "E"


def test_f_grade():
    assert letter_grade(30) == "F"


def test_invalid_negative_marks():
    with pytest.raises(ValueError):
        letter_grade(-1)


def test_invalid_marks_above_100():
    with pytest.raises(ValueError):
        letter_grade(101)


# Final marks tests
def test_final_marks_without_project():
    assert final_marks(30, 50, False) == 80


def test_final_marks_with_project():
    assert final_marks(30, 50, True) == 85


def test_final_marks_capped_at_100():
    assert final_marks(40, 60, True) == 100


def test_invalid_internal_marks():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)


def test_invalid_external_marks():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)


# Exam eligibility tests
def test_exam_eligible():
    assert exam_eligibility(80, True, False) == "eligible"


def test_exam_detained():
    assert exam_eligibility(60, True, False) == "detained"


def test_exam_blocked_due_to_fees():
    assert exam_eligibility(90, False, False) == "blocked"


def test_exam_eligible_with_medical():
    assert exam_eligibility(70, True, True) == "eligible"
