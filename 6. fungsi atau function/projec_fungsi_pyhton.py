def get_grades_from_user():
    grades = []
    ask_for_grades = True
    while ask_for_grades:
        grade = int(input("Masukkan nilai selanjutnya: "))
        if grade == -1:
            ask_for_grades = False
        else:
            if (grade >= 0) and (grade <= 10):
                grades.append(grade)
            else:
                print("Tolong masukkan angka diantara " + \
                      "0 dan 10 (-1 untuk berhenti)")
    return grades

def compute_list_minimum(number_list):
    minimum = number_list[0]
    for number in number_list:
        if number < minimum:
            minimum = number
    return minimum

def compute_list_maximum(number_list):
    maximum = number_list[0]
    for number in number_list:
        if number > maximum:
            maximum = number
    return maximum

def compute_list_average(number_list):
    sum = 0
    for number in number_list:
        sum += number
    average = sum / len(number_list)
    return average

grades = get_grades_from_user()
if len(grades) == 0:
    print("Kamu tidak memasukkan nilai sama sekali!")
    exit()

print(grades)
print("Kamu memberikan " + str(len(grades)) + " nilai.")
minimum = compute_list_minimum(grades)
maximum = compute_list_maximum(grades)
average = compute_list_average(grades)
print("Nilai Terkecil: " + str(minimum) + \
      ", Nilai Terbesar: " + str(maximum) + \
      ", Rata-rata: " + str(average))