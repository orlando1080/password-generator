def get_validated_password_length_input(prompt):
    """Function to validate user input for length of password."""
    while True:
        response = input(prompt)
        valid_responses = response.isdigit() and 128 >= int(response) >= 8
        if valid_responses:
            return response
        else:
            print(f"\nEnter a value between 8-128.")

