"""
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
********************************
"""

from glob import escape


class Grade(object):
    def __init__(self, ko, en, ma, name) -> None:
        self.ko = ko
        self.en = en
        self.ma = ma
        self.name = name
        self.add = 0
        self.avg = 0.0
        self.grade = ""

        
    def execute(self): 
        self.get_avg()
        self.get_add()
        self.get_grade()
        self.print_grade()
        self.grade = self.get_grade()


    def get_avg(self):
        ko = self.ko
        en = self.en
        ma = self.ma
        return (ko+en+ma)/3

    def get_add(self):
        ko = self.ko
        en = self.en
        ma = self.ma
        return ko+en+ma

    def get_grade(self):
        avg = self.get_avg()
        grade = ""
        if avg>= 90:
            grade = "A학점"
        elif avg>= 80:
            grade = "B학점"
        elif avg>= 70:
            grade = "C학점"
        elif avg>= 60:
            grade = "D학점"
        elif avg>=50:
            grade = "E학점"
        else:
            grade = "F학점"
        self.grade = grade


    def print_grade(self): 
        title = "### 성적표 ###"
        aster = "*" * 40
        schema = " 이름 국어 영어 수학 총점 평균 학점"
        ko = self.ko
        en = self.en
        ma = self.ma
        name = self.name        
        add = ko + en + ma
        avg = add/3
        grade = self.grade
        answer = f"{name} {ko} {en} {ma} {add} {avg} {grade}"
        print(f"({title}\n {aster}\n {schema}\n {aster}\n {answer}\n {aster} )")

    @staticmethod
    def main():
        name = input("이름: ")
        ko = int(input("국어: "))
        en = int(input("영어: "))
        ma = int(input("수학: "))
        grade = Grade(ko, en, ma, name)
        grade.execute()

Grade.main()