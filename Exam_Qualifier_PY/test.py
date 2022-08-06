
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