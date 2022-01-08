def get_name():
    return input("Enter first name: ")

def get_surname():
    return input("Enter surname: ")

def are_tests_written():
    return input("Have you written tests this semester/year (y/n): ")

def are_projects_written():
    return input("Did you do any projects this semester/year (y/n): ")

def are_presentation_written():
    return input("Did you do any presentations this semester/year (y/n): ")

def num_tests():
    return int(input("How many tests have you written?: "))

def num_projects():
    return int(input("How many projects have you done?: "))

def num_presentations():
    return int(input("How many presentations have you done?: "))

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
        presentation_list.append(int(input("Enter mark (our of 100) for your presentation {}".format(z))))
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

    test_question = are_tests_written()
    if test_question == "y" or test_question == "yes" or test_question == "Y".lower() or test_question == "Yes".lower():
        test_count = num_tests()
        test_list = get_tests_list(test_count)
        avg_test = calc_average_test(test_list)
        print("Average Test Mark: {}%".format(avg_test))
        tot_mark += avg_test
        count += 1

    project_question = are_projects_written()
    if project_question == "y" or project_question == "yes":
        project_count = num_projects()
        project_list = get_projects_list(project_count)
        avg_project = calc_average_project(project_list)
        print("Average Project Mark: {}%".format(avg_project))
        tot_mark += avg_project
        count += 1

    presentation_question = are_presentation_written()
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
        print("Congrations {} {}, you have qualified to write the exams.".format(name, surname))
    else: 
        print("Sorry {} {}, you have failed the module, you will need to repeat next year".format(name, surname))


    
    

    




    

