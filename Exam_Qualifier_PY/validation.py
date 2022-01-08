def is_input_valid(question):
    if question not in ["y", "Y".lower(), "yes", "no", "n", "No".lower()]:
        return False
    return True 

def is_num_valid(num):
    if not type(num) == int:
        return False
    return True