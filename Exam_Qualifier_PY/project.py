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