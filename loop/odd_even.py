
from random_list import RandomList

class Odd(object):
    def __init__(self) -> None:
        pass



    def print(self):
        rl = RandomList()
        print(rl.get_random(10,100,10))
        for i in rl.get_random(10,100,10):
            if i % 2 == 0:
                print(f"짝수 : {i}")
            else:
                print(f"홀수: {i}")

    # [i for i in rl]
    # print([f"짝수 : {i}" if i %2 == 0 else f"홀수: {i}" for i in rl.get_random(10,100,10)])
    # [i if True else i for i in []]