
from itertools import count
import Exam_Qualifier_PY.test
import Exam_Qualifier_PY.project
import Exam_Qualifier_PY.presentation


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


"""
Test score(s)
"""
'''
def get_test_validation():
    return input("Have you written tests this semester(y/n)? ")

def count_test():
    return int(input("How many tests did you write? "))

def test_score(count):
    return int(input("Enter score (%) for test {}: ".format(count+1)))

def get_total_test(test_validation):
    test_count = 0
    tot_test = 0 
    if test_validation in ["y","Y"]:
        test_count = count_test()
        if test_count <=0:
            return tot_test
        else:
            for i in range(test_count):
                tot_test += test_score(i)
            tot_test = tot_test / test_count
    if test_validation in ["n", "N"]:
        return tot_test
    
    return tot_test
'''

"""
Project score(s)
"""
'''
def get_project_validation():
    return input("Have you worked on projects this semester(y/n)? ")

def count_project():
    return int(input("How many projects have you worked on? "))

def project_score(count):
    return int(input("Enter score (%) for project {}: ".format(count+1)))

def get_total_project(validation):
    project_count = 0
    tot_project = 0
    if validation in ["y","Y"]:
        project_count = count_project()
        if project_count <= 0:
            return tot_project
        else:
            for i in range(project_count):
                tot_project += project_score(i)
            tot_project = tot_project/project_count
    if validation in ["n", "N"]:
        return tot_project
    
    return tot_project
'''
"""
Presentation Score(s)
"""

def get_presentation_validation():
    return input("Have you done any presentations this semester(y/n)? ")

def count_presentation():
    return int(input("How many presentations have you done? "))

def presentation_score(count):
    return int(input("Enter score (%) for presentation {}:".format(count+1)))

def get_total_presentation(validation):
    presentation_count = 0
    tot_presentation = 0
    if validation in ["y","Y"]:
        presentation_count = count_presentation()
        if presentation_count <=0:
            return tot_presentation
        else:
            for i in range(presentation_count):
                tot_presentation += presentation_score(i)
            tot_presentation = tot_presentation/presentation_count
    if validation in ["n","N"]:
        return tot_presentation
    
    return tot_presentation



def get_exam():
    return int(input("Enter exam mark: "))

def get_final_mark(dp_mark, exam):
    return (dp_mark*0.4) + (exam*0.6)

def display():
    tot_dp = 0
    tot_count = 0
    avg_dp = 0
    #print("Total test score out of 100: {}".format(get_total_test(validation)))
    test_validation = Exam_Qualifier_PY.test.get_test_validation()
    if test_validation in ["y","Y"]:
        tot_dp += Exam_Qualifier_PY.test.get_total_test(test_validation)
        tot_count += 1

    project_validation = Exam_Qualifier_PY.project.get_project_validation()
    if project_validation in ["y","Y"]:
        tot_dp += Exam_Qualifier_PY.project.get_total_project(project_validation)
        tot_count += 1

    presentation_validation = get_presentation_validation()
    if presentation_validation in ["y","Y"]:
        tot_dp += get_total_presentation(presentation_validation)
        tot_count += 1
    
    if(tot_count == 0):
        print("Nothing has been recorded")
        exit()

    avg_dp = tot_dp / tot_count    

    exam = get_exam()

    final_mark = get_final_mark(avg_dp, exam)

    print("{}%".format(final_mark))

    

    
if __name__=="__main__":
    display()

