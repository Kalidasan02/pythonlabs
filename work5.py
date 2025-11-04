python_students = {"alice","bob","charlie"}
data_science_students = {"david","bob","eve"}
python_students.add("Raju")
data_science_students.remove("eve")  
print(python_students&data_science_students)
print(python_students-data_science_students)
print(python_students|data_science_students)

course = {
    "python": len(python_students),
    "data science":len(data_science_students)
}

for x,y in course.items():
    print(x,y)


expected_growth = {course: x * 2 for course, x in course.items()}
print(expected_growth)