import pytest
from dashboard.validations import validate_vat  

@pytest.mark.parametrize("vat_number, expected_result", [
    (173635679, True),  
    (290528089, True),  
    (323399819, True),  
    (529784149, True),  
    (678785937, True),  
    (817607374, True),  
    (943520274, True), 

    (456789123, False),  
    (789123456, False),  
    ("PT1234567", False),
    ("1234567890", False)
])

def test_validations_vat(vat_number, expected_result):
    assert validate_vat(vat_number) == expected_result