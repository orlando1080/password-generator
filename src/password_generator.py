from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from .password_type_count import password_type_count


def password_generator(length, numbers, capitals, symbols):
    """Function that return random character from a list to create a password."""
    if numbers and capitals and symbols:
        characters = ''.join([punctuation, ascii_lowercase, digits, ascii_uppercase])
        password = ''.join(choice(characters) for _ in range(int(length)))
        type_count = password_type_count(password)
        while any(number < 1 for number in type_count.values()):
            password = ''.join(choice(characters) for _ in range(int(length)))
            type_count = password_type_count(password)
        return password

    elif numbers and capitals:
        characters = ascii_lowercase + ascii_uppercase + digits
        password = "".join(choice(characters) for _ in range(int(length)))
        type_count = password_type_count(password)
        while any(number < 1 for number in sorted(type_count.values())[1:]):
            password = ''.join(choice(characters) for _ in range(int(length)))
            type_count = password_type_count(password)
        return password

    elif capitals and symbols:
        characters = ascii_lowercase + ascii_uppercase + punctuation
        password = "".join(choice(characters) for _ in range(int(length)))
        type_count = password_type_count(password)
        while any(number < 1 for number in sorted(type_count.values())[1:]):
            password = ''.join(choice(characters) for _ in range(int(length)))
            type_count = password_type_count(password)
        return password

    elif numbers and symbols:
        characters = ascii_lowercase + digits + punctuation
        password = "".join(choice(characters) for _ in range(int(length)))
        type_count = password_type_count(password)
        while any(number < 1 for number in sorted(type_count.values())[1:]):
            password = ''.join(choice(characters) for _ in range(int(length)))
            type_count = password_type_count(password)
        return password

    elif numbers:
        characters = ascii_lowercase + digits
        password = "".join(choice(characters) for _ in range(int(length)))
        type_count = password_type_count(password)
        while any(number < 1 for number in sorted(type_count.values())[2:]):
            password = ''.join(choice(characters) for _ in range(int(length)))
            type_count = password_type_count(password)
        return password

    elif capitals:
        characters = ascii_lowercase + ascii_uppercase
        password = "".join(choice(characters) for _ in range(int(length)))
        type_count = password_type_count(password)
        while any(number < 1 for number in sorted(type_count.values())[2:]):
            password = ''.join(choice(characters) for _ in range(int(length)))
            type_count = password_type_count(password)
        return password

    elif symbols:
        characters = ascii_lowercase + punctuation
        password = "".join(choice(characters) for _ in range(int(length)))
        type_count = password_type_count(password)
        while any(number < 1 for number in sorted(type_count.values())[2:]):
            password = ''.join(choice(characters) for _ in range(int(length)))
            type_count = password_type_count(password)
        return password

    else:
        characters = ascii_lowercase
        password = ''.join(choice(characters) for _ in range(int(length)))
        return password
