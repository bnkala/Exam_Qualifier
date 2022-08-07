
from itertools import count
import test
import project
import presentation
import exam as Exam
import personal_info


def get_final_mark(dp_mark, exam):
    return (dp_mark*0.4) + (exam*0.6)

def get_status(final,name,surname,module):
    if (final >= 75):
        return "Congratulations {} {}!!! You passed {} with a distinction!".format(name,surname,module)
    elif (final >= 50):
        return "Congratulations {} {}!!! You passed {}!".format(name,surname,module)
    else:
        return "I'm sorry {} {}, you failed {}, you have to repeat it next year".format(name,surname,module)

def display():
    tot_dp = 0
    tot_count = 0
    avg_dp = 0

    name = personal_info.get_name()
    surname = personal_info.get_surname()
    #institution = personal_info.get_institution()
    #qualification = personal_info.get_qualification()
    course_type = personal_info.get_course_type()
    module = personal_info.get_module()
    #email = personal_info.get_email()

    
    
    test_validation = test.get_test_validation(course_type)
    if test_validation in ["y","Y"]:
        tot_dp += test.get_total_test(test_validation)
        tot_count += 1

    project_validation = project.get_project_validation(course_type)
    if project_validation in ["y","Y"]:
        tot_dp += project.get_total_project(project_validation)
        tot_count += 1

    presentation_validation = presentation.get_presentation_validation(course_type)
    if presentation_validation in ["y","Y"]:
        tot_dp += presentation.get_total_presentation(presentation_validation)
        tot_count += 1
    
    if(tot_count <= 0):
        print("Nothing has been recorded")
        exit()

    avg_dp = tot_dp / tot_count 

    if(avg_dp < 40):
        print("{}%".format(avg_dp))
        print("Sorry, you failed the module, you have to repeat it next year")
        exit()   
        
    exam = Exam.get_exam()

    while Exam.validate_exam(exam) == False:
        exam = Exam.get_exam()
    
    exam = int(exam)

    final_mark = get_final_mark(avg_dp, exam)
    status = get_status(final_mark, name, surname, module)
    print("{}%".format(final_mark))
    print(status)

    
if __name__=="__main__":
    display()

