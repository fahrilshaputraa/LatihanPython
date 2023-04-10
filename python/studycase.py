# berapa_kali_input = input("Berapa Kali Input Data? : ")
# data = []
# jum = 0
# i = 0

# while i in range(0, berapa_kali_input):
#     user_input = input("Nama : ")
#     user_input2 = int(input("grade : " %(i+1))) 
#     # user_input3 = input("Nilai 2 : ")
#     # user_input4 = input("Nilai 3 : ")
#     data.append(user_input2)
#     jum += data
#     i+=1

#     a = (str([user_input2]))
#     a = []
#     (user_input)
#     (str(a.split(",")))

#     average = (int((user_input2)))/3
#     print(user_input,":", average)


u1 = int(input("Enter the number of student in your class : "))

data = []

def totalGrades(grades):
    grade = 0
    grades = grades.split(",")
    for i in grades:
        grade += float (i)
    grade = grade/len(grades)
    return grade

for i in range(int(u1)):
    name = input("Enter the name of student" + str (i+1) + " : ")
    grade = input("Enter the grade of student " + str (i+1) + "(coma-separated) : ")
    data.append(
        {
            'nama': name,
            'grade': grade,
            'average_grade': totalGrades(grade)
        }
    )

print()
print("Average Grades: ")
for z in data:
    print(z["nama"], ":", z["average_grade"])