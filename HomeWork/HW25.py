from pprint import pprint as pp
"""
task 1 
"""
lst = []
pp(lst)
file = open('lesson_12.txt', encoding='utf-8')
for line in file.readlines():
    lst.append(line.strip('\n'))
file.close()
pp(lst)
sum_of_averages = 0
list_of_object = []
names_of_averrage = ''
for string_line in lst:
    full_name = string_line[:28].strip()
split_full_name = full_name.split(" ")
first_name = split_full_name[0]
last_name = split_full_name[1]
marks_intgers = [int(x) for x in string_line[28:].strip().split(" ") if x != '']
# marks_intgers = []
# for mark in range(0, len(marks_string)):
# if marks_string[mark] != '':
# marks_string[mark] = int(marks_string[mark])
# marks_intgers.append(marks_string[mark])
averrage_marks = sum(marks_intgers) / len(marks_intgers)
if averrage_marks < 5:
    print(full_name)
sum_of_averages += averrage_marks
list_of_object.append(
    dict(first_name=first_name, last_name=last_name, marks=marks_intgers, marks_averrage=averrage_marks))
total_averages = sum_of_averages / len(lst)
print(total_averages)
# print(first_name, "{}.".format(last_name[0]), averrage_marks)
to_return = ''
for student in list_of_object:
    spesial_full_name = student["first_name"] + " " + "{}.".format(student["last_name"][0])
avereage_special_format = '{:.2f}'.format(student["marks_averrage"])
to_return += '{: <20}'.format(spesial_full_name) + avereage_special_format + '\n'
print(to_return)
new_file = open('new_file_lesson.txt', 'w', encoding='utf-8')
new_file.write(to_return)
new_file.close()
