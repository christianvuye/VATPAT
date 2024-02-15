"""
The algorithm to verify the NIF number in Portugal is as follows:

Ensure the number has 9 digits.

Multiply each of the first 8 digits by a decreasing sequence of multipliers,
starting from 9 (i.e., 9, 8, 7, 6, 5, 4, 3, 2).

Sum the results of these multiplications.

Calculate the remainder of dividing this sum by 11.

If the remainder is 0 or 1, the check digit should be 0. 
Otherwise, subtract the remainder from 11 to get the check digit.

Compare the calculated check digit with the actual ninth digit 
of the NIF number to verify its validity.
"""


"""
NIF numbers (Número de Identificação Fiscal) in Portugal cannot start with a 0. 

Prefixes: The first digit of a NIF number indicates the type of taxpayer:

1: Pessoa singular (individuals)
2: Pessoa singular (individuals)
3: Pessoa singular (individuals) - new from 2019
5: Pessoa coletiva (businesses)
6: Pessoa coletiva (public entities)
8: Empresário em nome individual (sole traders)
9: Pessoa colectiva irregular ou numero provisorio (temporary numbers)

"""

def validate_vat(vat):
    # Ensure VAT is a string to handle leading zeros
    vat = str(vat)
    
    # Check if VAT has exactly 9 digits
    if len(vat) != 9:
        return False

    # Check if VAT has only digits
    if not vat.isdigit():
        return False

    # Check if the first digit is one of the allowed prefixes
    if vat[0] not in ["1", "2", "3", "5", "6", "8", "9"]:
        return False
    
    # Define the sequence of multipliers
    multipliers = [9, 8, 7, 6, 5, 4, 3, 2]
    
    # Calculate the checksum
    checksum = 0
    for i in range(8):
        checksum += int(vat[i]) * multipliers[i]    
    
    # Calculate the remainder of the checksum divided by 11
    remainder = checksum % 11
    
    # Determine the check digit
    if remainder < 2:
        check_digit = 0
    else:
        check_digit = 11 - remainder
       
    # Verify if the last digit matches the check digit
    is_valid = int(vat[-1]) == check_digit

    # Return the boolean result True or False
    return is_valid
 


