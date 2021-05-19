#Function Declaration with one argument, a list.
def mean(student_grades):
    the_mean = sum(student_grades) / len(student_grades)
    return the_mean

print(mean([1, 3, 4, 5, 5]))
print(type(mean), type(sum), type(len))
