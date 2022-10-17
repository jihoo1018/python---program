class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def execute(self):
        num1 = self.num1
        op = self.op
        num2 = self.num2
        
        if op == "+":
            result = num1 +num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%" :
            result = num1 % num2
        else:
            result = "잘못된 연산 입니다."
        print(f"{num1} {op} {num2} = {result}")





if __name__=="__main__":
    num1 = int(input("숫자 : "))
    op = input("+, -, *, /, %")
    num2 = int(input("숫자 : "))
    calculator = Calculator(num1, op, num2)
    calculator.execute()


