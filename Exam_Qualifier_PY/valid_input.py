def validate_input(objective):
    if objective =="" or objective not in ["y","Y","n","N"]:
        print("Please enter either 'y' for yes or 'n' for no")
        return False
    return True
    