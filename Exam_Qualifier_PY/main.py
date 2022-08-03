
from itertools import count

'''
def get_name():
    return input("Enter name: ")

def get_surname():
    return input("Enter surname: ")

def get_institution():
    return input("Enter institution you studying at: ")

def get_qualification():
    return input("Enter qualification you studying for: ")'''

def get_test_validation():
    return input("Have you written tests this semester(y/n)? ")

def count_test():
    return int(input("How many tests did you write? "))

def test_score(count):
    return int(input("Enter score for test {}: ".format(count+1)))

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
def get_project_validation():
    return input("Have you worked on projects this semester(y/n)? ")

def count_project():
    return int(input("How many projects have you worked on? "))

def get_presentation_validation():
    return input("Have you done any presentations this semester(y/n)? ")

def count_presentation():
    return int(input("How many presentations have you done? "))
'''

def get_exam():
    return int(input("Enter exam mark: "))

def get_final_mark(dp_mark, exam):
    return (dp_mark*0.4) + (exam*0.6)

def display():
    validation = get_test_validation()
    print("Total test score out of 100: {}".format(get_total_test(validation)))
    
if __name__=="__main__":
    display()

