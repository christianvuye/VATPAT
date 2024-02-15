import pytest
from dashboard.validations import validate_vat  

@pytest.mark.parametrize("vat_number, expected_result", [
    (501964843, True),  # Valid case for non-residents
    (123456789, False),  # Invalid case, incorrect prefix
    (201234567, True),  # Valid case for individuals
    (301234567, True),  # Valid new case for individuals from 2019
    (501234567, True),  # Valid case for businesses
    (601234567, True),  # Valid case for public entities
    (801234567, True),  # Valid case for sole traders
    (901234567, True),  # Valid case for temporary numbers
    (12345678, False),  # Invalid, too short
    (1234567890, False),  # Invalid, too long
])
def test_validations_vat(vat_number, expected_result):
    assert validate_vat(vat_number) == expected_result