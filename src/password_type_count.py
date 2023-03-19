import re


def password_type_count(password):
    """Function that counts all types of character in an iterator, sums it and places it in a dictionary."""
    type_count = {'lowercase': len(re.findall(r'[a-z]', password)),
                  'digits': len(re.findall(r'\d', password)),
                  'uppercase': len(re.findall(r'[A-Z]', password)),
                  'symbols': len(re.findall(r'[^A-Za-z\d]', password))
                  }
    return type_count
