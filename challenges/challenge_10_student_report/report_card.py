def generate_report(name, s1, s2, s3):
    total = s1 + s2 + s3
    average = total / 3

    if average >= 60:
        grade = "1st Class"
    elif average >= 50:
        grade = "2nd Class"
    elif average >= 35:
        grade = "Pass Class"
    else:
        grade = "Fail"

    return total, average, grade


if __name__ == "__main__":
    name = input("Enter student name: ").strip()
    s1 = float(input("Enter subject 1 marks: "))
    s2 = float(input("Enter subject 2 marks: "))
    s3 = float(input("Enter subject 3 marks: "))

    total, avg, grade = generate_report(name, s1, s2, s3)

    print("Total:", total)
    print("Average:", avg)
    print("Class Secured:", grade)
