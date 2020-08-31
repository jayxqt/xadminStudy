class Ball:
    ##在对象初始化的时候调用
    def __init__(self, name):
        self.name = name 
    def kick(self):
        print("我是球%s, 谁踢了我" % self.name)

class Person:
    #变量名前面加上双下划线，此变量就变成了私有变量
    __name = "jay"
    def getName(self):
        return self.__name

# 括号的list表示继承list类，继承后就有了list的特性
class MyList(list):
    # pass是一个占位符，表示跳过什么都不做
    pass

if __name__ == '__main__':
    c = Ball("土豆")
    c.kick()
    print("------------")
    p = Person();
    print(p._Person__name) #私有变量变为了 _类名__变量名，python内部给改了类名
    print(p.getName())
    print("------------")
    list1 = MyList()
    list1.append(2)
    list1.append(4)
    list1.append(1)
    print(list1)
    list1.sort(key=None, reverse=False);
    print(list1)
    print("------------")