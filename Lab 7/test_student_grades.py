
"""Property-based and example-based tests for student_grades.py."""

from hypothesis import given, strategies as st

from student_grades import average_marks, parse_srn, short_name


@given(st.one_of(st.text(), st.none()))
def test_average_marks_no_crash(value):
    result = average_marks(value)
    assert result is None or isinstance(result, float)


@given(st.one_of(st.text(), st.none()))
def test_parse_srn_no_crash(value):
    result = parse_srn(value)

    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 3
        and isinstance(result[0], str)
        and isinstance(result[1], int)
        and isinstance(result[2], str)
    )


@given(st.one_of(st.text(), st.none()))
def test_short_name_no_crash(value):
    result = short_name(value)
    assert result is None or isinstance(result, str)


def test_average_marks_valid_and_invalid_inputs():
    assert average_marks("78,85,92") == 85.0
    assert average_marks("70,80,90") == 80.0

    assert average_marks("") is None
    assert average_marks("10,,20") is None
    assert average_marks("10,abc,20") is None
    assert average_marks("-1,20") is None
    assert average_marks("101,20") is None
    assert average_marks(None) is None


def test_parse_srn_valid_and_invalid_inputs():
    assert parse_srn("PES1UG23CS123") == ("PES1", 23, "CS")

    assert parse_srn("PES1UG23CS12") is None
    assert parse_srn("PES1UGXXCS123") is None
    assert parse_srn("not-an-srn") is None
    assert parse_srn(None) is None


def test_short_name_valid_and_invalid_inputs():
    assert short_name("ravi kumar") == "R. Kumar"
    assert short_name("  ravi   kumar  ") == "R. Kumar"

    assert short_name("") is None
    assert short_name("ravi") is None
    assert short_name("ravi kumar singh") is None
    assert short_name(None) is None
