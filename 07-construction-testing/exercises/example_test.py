import pytest
import System
import Professor
import Student

#Tests if the program can handle a wrong username
# def test_login(grading_system):
#    username = 'thtrhg'
#    password =  'fhjhjdhjdfh'
#    grading_system.login(username,password)

def test_login(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username, password)

def test_check_password(grading_system):
    grading_system.check_password('akend3', None)

def test_change_grade(test_professor):
    test_professor.change_grade('yted9', 'software_engineering', 'assignment1', 0)

def test_create_assignment(test_professor):
    test_professor.create_assignment('assignment3', '04/01/20', 'cloud_computig')

def test_add_student(test_professor):
    test_professor.add_student('', 'comp_sci')

def test_drop_student(test_professor):
    test_professor.drop_student('akend3', 'databases')

def test_submit_assignment(test_student):
    test_student.submit_assignment('comp_sci', 'assignment1', 'Submission for assignment 1', '03/01/20')

def test_check_ontime(test_student):
    test_student.check_ontime('03/01/20', '03/01/20')

def test_check_grades(test_student):
    test_student.check_grades('comp_sci')

def test_view_assignments(test_student):
    test_student.view_assignments(2)

def test_ontime_correct(test_student):
    if test_student.check_ontime('03/04/20', '03/01/20'):
        pytest.fail("Test failed because check_ontime returned true for false input")

def test_ontime_date_format(test_student):
    if test_student.check_ontime('030120', '03/01/20'):
        pytest.fail("Test failed because check_ontime failed to catch improper input formatting")

def test_add_student_without_authority(test_professor):
    try:
        test_professor.add_student('thys7r', 'databases')
        pytest.fail("Test failed because professor was able to add student to a class they don't teach")
    except:
        pytest.fail("Test failed because code threw exception")

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

@pytest.fixture
def test_professor(grading_system):
    testProfessor = Professor.Professor('saab', grading_system.users, grading_system.courses)
    return testProfessor

@pytest.fixture
def test_student(grading_system):
    testStudent = Student.Student('akend3', grading_system.users, grading_system.courses)
    return testStudent
