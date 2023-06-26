# LIST COMPREHENSION:
# numbers = [1, 2, 3]

# new_list = []
# for n in list:
#     add_1 = n+1
#     new_list.append(add_1)
# => can be written as
# new_list = [new_item for item in list] //template
# new_list = [n+1 for n in numbers] //actual code

# for x in y:
# y is a sequence, i.e., lists, strings, tuples, range

# DOUBLE a range 
# range_list = [item*2 for item in range(1,5)]
# print(range_list)

# CONDITIONAL LIST COMPREHENSION
# new_list = [new_item for item in list if test] //template
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# uppercaselong_names = [name.upper() for name in names if len(name) > 5]
# print(uppercaselong_names)

# DICTIONARY COMPREHENSION
# new_dict = {new_key:new_value for item in list}
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
# student_scores  = {student: random.randint(40, 100) for student in names}
# print(student_scores)

# .items() creates a view of dictionary where each key-value pair is stored, as tuples in a list
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

import pandas 
passed_students = {
    "student": ["Angela", "Eleanor", "Freddie"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(passed_students)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)

# Loop through rows of a data frame 
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)


