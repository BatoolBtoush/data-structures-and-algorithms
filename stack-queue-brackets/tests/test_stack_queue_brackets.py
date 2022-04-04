import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_case_one():

    actual = validate_brackets("{}")
    expected = True
    assert actual == expected


def test_case_two():

    actual = validate_brackets("")
    expected = True
    assert actual == expected


def test_case_three():

    actual = validate_brackets("()[[Batool]]")
    expected = True
    assert actual == expected


def test_case_four():

    actual = validate_brackets("[({}]")
    expected = False
    assert actual == expected


def test_case_five():

    actual = validate_brackets("{(})")
    expected = False
    assert actual == expected


def test_case_six():

    actual = validate_brackets("{}{Bat}[Batool](())")
    expected = True
    assert actual == expected


def test_case_seven():
    with pytest.raises(Exception):
        validate_brackets({{}})
