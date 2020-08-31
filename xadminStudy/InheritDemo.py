import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置是：", self.x, self.y)

class GoldFish(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        #Fish.__init__(self) #如果Shark类要使用Fish类的x属性，必须要重写Fish的__init__方法，然后调用move方法才不会报错
        #或者调用下面的super().__init__()方法也行，用super()方法更好，因为不需要写死父类的类名
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("天天想吃肉...")
            self.hungry=False
        else:
            print("吃不下了")

if __name__ == '__main__':
    fish = Fish();
    fish.move();
    fish.move();
    print("---------------")
    gFish = GoldFish()
    gFish.move()
    gFish.move()
    print("---------------")
    shark = Shark()
    shark.eat()
    shark.eat()
    #由于Shark自定义了__init__()方法，里面没有定义x的值，所以运行时会报错:AttributeError: 'Shark' object has no attribute 'x'
    #解决方法：在Shark的__init__()方法里重写父类的__init__方法
    shark.move() 
    shark.move() 