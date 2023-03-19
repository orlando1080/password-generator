def get_validated_input(prompt, valid_responses):
    """Function that validates user entries, will prompt then to enter correct entries if incorrect."""
    while True:
        response = input(prompt).lower()
        if response in valid_responses:
            return response
        else:
            print(f"\nInvalid response. Please enter one of {valid_responses}: ")
