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