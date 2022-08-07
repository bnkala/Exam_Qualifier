import re

def get_exam():
    return input("Enter exam mark: ")

def validate_exam(exam):
    if not re.match('^[0-9]*$', exam):
        print("Exam mark should be numerical or should not be less than 0.")
        return False
    return True