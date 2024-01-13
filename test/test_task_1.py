from unittest import TestCase
from task_1 import identify_zodiac_sign, perimeter_and_area_square, financial_calculator
import pytest

class TestSomething(TestCase):

    def test_identify_zodiac_sign(self):
        day = 10
        month = 'май'
        expected = 'Телец'
        result = identify_zodiac_sign(day, month)
        self.assertEqual(result, expected)

    def test_perimeter_and_area_square(self):
        a = 10
        expected = (40, 100)
        result = perimeter_and_area_square(a)
        test_perimeter = result[0]
        test_area = result[1]
        self.assertEqual(result, expected)
        self.assertGreater(test_perimeter, 39)
        self.assertGreater(test_area, 99)

    def test_financial_calculator(self):
        salary = 200000
        percent_mortgage = 20
        percent_life = 50
        expected = (480000, 720000)
        result = financial_calculator(salary, percent_mortgage, percent_life)
        self.assertEqual(result, expected)

class TestSomethingWithPytest:
    @pytest.mark.xfail
    def test_identify_zodiac_sign_equal(self):
        day = 10
        month = 'сентябрь'
        result = identify_zodiac_sign(day, month)
        expected = 'Дева'
        assert result == expected

@pytest.mark.xfail
def test_perimeter_and_area_square():
    a = 10
    expected = (40, 100)
    result = perimeter_and_area_square(a)
    test_perimeter = result[0]
    test_area = result[1]
    assert result == expected
    assert test_perimeter > 39
    assert test_area > 99

@pytest.mark.parametrize(
    'salary, percent_mortgage, percent_life, expected',
    (
            (200000, 20, 50, (480000, 720000)),
            (220000, 30, 50, (792000, 528000)),
            (220000, 25, 40, (660000, 924000)),
            (120000, 30, 50, (432000, 288000)),
            (120000, 25, 40, (360000, 504000)),
     )
)
def test_financial_calculator(salary, percent_mortgage, percent_life, expected):
    result = financial_calculator(salary, percent_mortgage, percent_life)
    assert result == expected
