import assignment

def test_name_type():
    assert isinstance(assignment.name, str) # 문자열인지 확인 

def test_age_type():
    assert isinstance(assignment.age, int) # 정수인지 확인

def test_numbers_content():
    assert 2 in assignment.numbers # 숫자 2가 리스트에 포함되어 있는지 확인
    assert len(assignment.numbers) == 3 # 리스트의 길이가 3인지 확인

def test_is_student():
    assert assignment.is_student is True # 학생 여부가 True인지 확인

