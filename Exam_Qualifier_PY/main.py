import validation


def get_name():
    return input("Enter first name(s): ")

def get_surname():
    return input("Enter surname: ")

def get_institution():
    return input("Enter name of tertiary institution: ")

def get_course_type():
    return input("Enter course type (year/semester): ")

def get_module_name():
    return input("Enter module you are studying: ")

def get_qualification():
    return input("Enter qualification you are studying for: ")


def are_tests_written(course_type):
    return input("Have you written tests this {} (y/n): ".format(course_type))

def are_projects_written(course_type):
    return input("Did you do any projects this {} (y/n): ".format(course_type))

def are_presentation_written(course_type):
    return input("Did you do any presentations this {} (y/n): ".format(course_type))

def num_tests():
    num_test = input("How many tests have you written?: ")
    if not validation.is_num_valid(num_test):
        print("Invalid input for number of tests")
        num_test = input("How many tests have you written?: ")
    return int(num_test)

def num_projects():
    num_projects = input("How many projects have you done?: ")
    while not validation.is_num_valid(num_projects):
        print("Invalid input for number of project(s)")
        num_projects = input("How many projects have you done?: ")
    #return int(input("How many projects have you done?: "))
    return int(num_projects)

def num_presentations():
    num_presentations = input("How many presentations have you done?: ")
    while not validation.is_num_valid(num_presentations):
        print("Invalid input for number of presentation(s)")
        num_presentations = input("How many presentations have you?: ")
    #return int(input("How many presentations have you done?: "))
    return int(num_presentations)



def get_tests_list(test_count):
    test_list = []
    for x in range(1, test_count+1):
        test_list.append(int(input("Enter mark (out of 100) for your test {}:".format(x) )))
    return test_list

def get_projects_list(project_count):
    project_list = []
    for x in range(1, project_count+1):
        project_list.append(int(input("Enter mark (out of 100) for your project {}:".format(x))))
    return project_list

def get_presentations_list(presentation_count):
    presentation_list = []
    for z in range(1, presentation_count+1):
        presentation_list.append(int(input("Enter mark (out of 100) for your presentation {}".format(z))))
    return presentation_list

def calc_average_test(test_list):
    avg_test = 0
    test_total = 0
    for x in test_list:
        test_total += x
    avg_test = test_total /len(test_list)
    return avg_test


def calc_average_project(project_list):
    avg_project = 0
    project_total =0
    for x in project_list:
        project_total += x

    avg_project = project_total / len(project_list)
    return avg_project

def calc_average_presentation(presentation_list):
    avg_presentation = 0
    presentation_total = 0
    for x in presentation_list:
        presentation_total += x

    avg_presentation = presentation_total / len(presentation_list)
    return avg_presentation

def tests(tot_mark, count, test_question, test_count, test_list, avg_test):
    #test_question = are_tests_written(course_type)
    while not validation.is_input_valid(test_question):
        print("Invalid input for test question!")
        test_question = are_tests_written(course_type)

    if test_question in ["y", "yes", "Y".lower(), "Yes".lower()]:
        test_count = num_tests()
        test_list = get_tests_list(test_count)
        avg_test = calc_average_test(test_list)
        print("Average Test Mark: {}%".format(avg_test))
        tot_mark += avg_test
        count += 1


if __name__ == "__main__":
    tot_mark = 0
    count = 0 
    avg_mark = 0

    test_count = 0
    project_count = 0
    presentation_count = 0

    test_list = []
    project_list = []
    presentation_list = []

    avg_test = 0
    avg_project = 0
    avg_presentation =0
    
    name = get_name()
    surname = get_surname()
    institution = get_institution()
    course_type = get_course_type()
    qualification = get_qualification()
    module = get_module_name()

    test_question = are_tests_written(course_type)
    tests(tot_mark, count, test_question, test_count, test_list, avg_test)
    '''
    test_question = are_tests_written(course_type)
    if not validation.is_input_valid(test_question):
        print("Invalid input for test question!")
        test_question = are_tests_written(course_type)

    if test_question in ["y", "yes", "Y".lower(), "Yes".lower()]:
        test_count = num_tests()
        test_list = get_tests_list(test_count)
        avg_test = calc_average_test(test_list)
        print("Average Test Mark: {}%".format(avg_test))
        tot_mark += avg_test
        count += 1
'''
    project_question = are_projects_written(course_type)
    while not validation.is_input_valid(project_question):
        print("Invalid input for project question!")
        project_question = are_projects_written(course_type)

    if project_question in ["y", "Y".lower(), "yes", "Yes".lower()]:
        project_count = num_projects()
        project_list = get_projects_list(project_count)
        avg_project = calc_average_project(project_list)
        print("Average Project Mark: {}%".format(avg_project))
        tot_mark += avg_project
        count += 1

    presentation_question = are_presentation_written(course_type)
    while not validation.is_input_valid(presentation_question):
        print("Invalid input for presentation question!")
        presentation_question = are_presentation_written(course_type)

    if presentation_question == "y" or presentation_question == "yes":
        presentation_count = num_presentations()
        presentation_list = get_presentations_list(presentation_count)
        avg_presentation = calc_average_presentation(presentation_list)
        print("Average Presentation Mark: {}%".format(avg_presentation))
        tot_mark += avg_presentation
        count+= 1

    avg_mark = (tot_mark / count)

    print("DP Mark: {}%".format(avg_mark))

    if(avg_mark >= 50):
        print("Congrations {} {}, you have qualified to write the exams for {} at {}.".format(name, surname, module, institution))
    else: 
        print("Sorry {} {}, you have failed {} this {} at {}, you will need to repeat next year".format(name, surname, module, course_type, institution))


    
    

    




    

