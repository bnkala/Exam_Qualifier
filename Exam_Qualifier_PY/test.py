import validation
import main

def are_tests_written(course_type):
    return input("Have you written tests this {} (y/n): ".format(course_type))

'''
def tests(tot_mark, count, test_question, test_count, test_list, avg_test, course_type):
    while not validation.is_input_valid(test_question):
        print("Invalid input for test question!")
        test_question = are_tests_written(course_type)

    if test_question in ["y", "yes", "Y".lower(), "Yes".lower()]:
        test_count = main.num_tests()
        test_list = main.get_tests_list(test_count)
        avg_test = main.calc_average_test(test_list)
        print("Average Test Mark: {}%".format(avg_test))
        tot_mark += avg_test
        count += 1'''