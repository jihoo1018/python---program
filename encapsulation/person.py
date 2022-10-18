"""
이름, 주민번호(950101 - 1), 주소를 입력받아서
회원 명부를 관리하는 어플을 제작하고자 한다.

출력되는 결과는 다음과 같다.
### 자기소개 어플 ###
********************************
이름: 홍길동
나이: 25살 (만나이)
성별: 남성
주소: 서울
********************************
"""
from datetime import datetime

class Person(object):
    def __init__(self, name, ssn, address) -> None:
        self.name = name
        self.ssn = ssn
        self.address = address
        self.age = 0
        self.gender = ""

    def set_age(self):
        ssn = self.ssn
        birth_year = int(ssn [0:2])
        if birth_year < 23:
            a3 = birth_year+2000
        else :
            a3 = birth_year+1900
        age = datetime.today().year - a3
        self.age = age


    def set_gender(self):
        ssn = self.ssn
        a2 = int(ssn[7])
        if a2 == 1 or a2 == 3:
            gender = "남자"
        elif a2 == 2 or a2 ==4:
            gender = "여자"
        else:
            gender = "잘못된 입력값입니다."
        self.gender = gender

    def execute(self):
        self.print_context()
        self.set_gender()
        self.set_age()
        self.person = self.print_context()



    def print_context(self):
        title = "### 자기소개 어플 ###"
        aster = "*"*40
        name = self.name
        age = self.age
        gender = self.gender
        address = self.address
        print(f"({title}\n {aster}\n {name}\n {age}\n {gender}\n {address})")



    @staticmethod
    def main():
        name = input("이름: ")
        ssn = input("주민번호: ")
        address = input("주소: ")
        person = Person(name, ssn, address)
        person.execute()

Person.main()

