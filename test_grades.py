
from grades import compute_hw_average


def test_zero_grades():
    grades = []
    assert compute_hw_average(grades) == 0


def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades) == 42

def test_two_grades():
    #added new documentation
    grades = [41,43]
    assert compute_hw_average(grades) == 42
