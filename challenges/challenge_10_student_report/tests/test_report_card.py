from challenges.challenge_10_student_report.report_card import generate_report

def test_first_class():
    total, avg, grade = generate_report("A", 70, 65, 80)
    assert total == 215
    assert avg == 215 / 3
    assert grade == "1st Class"


def test_second_class():
    total, avg, grade = generate_report("B", 55, 52, 50)
    assert grade == "2nd Class"


def test_pass_class():
    total, avg, grade = generate_report("C", 35, 40, 38)
    assert grade == "Pass Class"


def test_fail_class():
    total, avg, grade = generate_report("D", 20, 30, 25)
    assert grade == "Fail"
