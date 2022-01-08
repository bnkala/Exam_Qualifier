def get_name():
    return input("Enter first name(s): ")

def get_surname():
    return input("Enter surname: ")

def are_tests_written():
    return input("Have you written tests this semester/year: (y/n)")

def are_projects_written():
    return input("Did you do any projects this semester/year: (y/n)")

def are_presentation_written():
    return input("Did you do any presenations this semester/year: (y/n)")

def num_tests():
    return int(input("How many tests have you written? "))

def num_projects():
    return int(input("How many projects have you done? "))

def num_presentations():
    return int(input("How many presentations have you done? "))

def get_tests_list(test_count):
    test_list = []
    for x in range(1, test_count+1):
        test_list.append(int(input("Enter (%) mark for your test {}: ".format(x) )))
    return test_list


if __name__ == "__main__":
    test_list = []
    '''project_list = []
    presentation_list = []
    name = get_name()
    surname = get_surname()
    test_question = are_tests_written()
    project_question = are_projects_written()
    presentation_question = are_presentation_written()'''



    

