def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temperatures = [8.8, 9.1, 7.5]
student_grades = {"Marry": 9.1, "Sim": 7.4, "John": 1.2}
print(mean(student_grades))
print(mean(monday_temperatures))