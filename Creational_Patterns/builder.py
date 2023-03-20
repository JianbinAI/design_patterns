# coding=utf-8

"""
创建型--建造者模式
内容：
    将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。

角色：
    抽象建造者（Builder）
    具体建造者（Concrete Builder），隐藏内部结构
    指挥者（Director），隐藏装配过程
    产品（Product）
特点：
    建造者模式与抽象工厂模式相似，也用来创建复杂对象。主要区别是建造者模式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象。

使用场景：
    当创建复杂对象的算法（Director）应该独立于该对象的组成部分以及它们的装配方式（Builder）时
    当构造过程允许被构造的对象有不同的表示时（不同Builder）。
优点：
    隐藏了一个产品的内部结构和装配过程
    将构造代码与表示代码分开
    可以对构造过程进行更精细的控制
"""

from abc import abstractmethod, ABCMeta

#------产品------
# 游戏角色
class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.arm = arm
        self.leg = leg
        self.body = body

    def __str__(self):
        return f"{self.face}, {self.arm}, {self.body}, {self.leg}"


#------建造者------
# 抽象建造者
class PlayerBuilder(metaclass=ABCMeta): # 捏脸
    @abstractmethod
    def build_face(self):
        pass
    @abstractmethod
    def build_arm(self):
        pass
    @abstractmethod
    def build_leg(self):
        pass
    @abstractmethod
    def build_body(self):
        pass
    @abstractmethod
    def get_player(self):
        pass

# 具体建造者
class BeautifulWomanBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()
    def build_face(self):
        self.player.face = "漂亮脸蛋"
    def build_arm(self):
        self.player.arm = "细胳膊"
    def build_body(self):
        self.player.body = "细腰"
    def build_leg(self):
        self.player.leg = "长腿"
    def get_player(self):
        return self.player

#------指挥者------
class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_arm()
        builder.build_leg()
        builder.build_face()
        return builder.get_player()


# Client
director = PlayerDirector() # setp1: 实例化指挥者
builder = BeautifulWomanBuilder() # step2: 实例化建造者
p = director.build_player(builder) # step3: 指挥者指挥建造者创建游戏角色
print(p)