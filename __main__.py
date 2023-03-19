from src.get_validated_input import get_validated_input
from src.get_validated_password_length_input import get_validated_password_length_input
from src.password_generator import password_generator


def main():
    """Function that runs the main script, asks the user what type of password that they want to create."""
    numbers_required = True
    capitals_required = True
    symbols_required = True

    length_of_password = get_validated_password_length_input('\nWhat is the length of the password that you want to'
                                                             ' create? (Min: 8, Max: 128): ')

    answer_for_numbers_required = get_validated_input('\nDo you want to include numbers in your password? [y/n]: ',
                                                      ['y', 'n'])
    if answer_for_numbers_required == 'n':
        numbers_required = False

    answer_for_capitals_required = get_validated_input('\nDo you want to include capital letters in your password? ['
                                                       'y/n]: ', ['y', 'n'])
    if answer_for_capitals_required == 'n':
        capitals_required = False

    answer_for_symbols_required = get_validated_input('\nDo you want to symbols in your password? [y/n]: ', ['y', 'n'])
    if answer_for_symbols_required == 'n':
        symbols_required = False

    password = password_generator(length_of_password, numbers_required, capitals_required, symbols_required)

    if password:
        print(f'\nHere is your password: {password}')
    else:
        print('\nThere has been an error please try again.')


if __name__ == '__main__':
    main()
