class Turtle:
    def __init__(self, x):
        self.num = x

class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def printNum(self):
        print("水池里公有乌龟 %d 只，小鱼 %d 条" % (self.turtle.num, self.fish.num))

if __name__ == '__main__':
    pool = Pool(1, 20);
    pool.printNum()