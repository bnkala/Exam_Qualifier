
from itertools import count
import test
import project
import presentation
import exam as Exam


"""
Info
"""
def get_name():
    return input("Enter name: ")

def get_surname():
    return input("Enter surname: ")

def get_institution():
    return input("Enter institution you studying at: ")

def get_qualification():
    return input("Enter qualification you studying for: ")

def get_course_type():
    return input("Enter type of course you are studying (year/semester): ")

def get_module():
    return input("Enter module you are studying: ")

def get_email():
    return input("Enter personal email: ")

def get_final_mark(dp_mark, exam):
    return (dp_mark*0.4) + (exam*0.6)

def get_status(final):
    if (final >= 75):
        return "Congratulations you passed with a distinction!"
    elif (final >= 50):
        return "Congratulations you passed the module"
    else:
        return "I'm sorry, you failed the module, you have to repeat it next year"

def display():
    tot_dp = 0
    tot_count = 0
    avg_dp = 0
    
    test_validation = test.get_test_validation()
    if test_validation in ["y","Y"]:
        tot_dp += test.get_total_test(test_validation)
        tot_count += 1

    project_validation = project.get_project_validation()
    if project_validation in ["y","Y"]:
        tot_dp += project.get_total_project(project_validation)
        tot_count += 1

    presentation_validation = presentation.get_presentation_validation()
    if presentation_validation in ["y","Y"]:
        tot_dp += presentation.get_total_presentation(presentation_validation)
        tot_count += 1
    
    if(tot_count <= 0):
        print("Nothing has been recorded")
        exit()

    avg_dp = tot_dp / tot_count 

    if(avg_dp < 40):
        print("Sorry, you failed the module, you have to repeat it next year")
        exit()   
        
    exam = Exam.get_exam()

    while Exam.validate_exam(exam) == False:
        exam = Exam.get_exam()
    
    exam = int(exam)

    final_mark = get_final_mark(avg_dp, exam)
    status = get_status(final_mark)
    print("{}%".format(final_mark))
    print(status)

    

    
if __name__=="__main__":
    display()

