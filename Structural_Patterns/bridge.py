# coding=utf-8

"""
结构型--桥模式
内容：
    将一事物的两个维度分离，使其都可以独立地变化
角色：
    抽象（Abstraction）
    细化抽象（RefinedAbstraction）
    实现者（Implementor）
    具体实现者（ConcreteImplementor）
应用场景：
    当事物有两个维度上的表现，两个维度（抽象，实现者）都可能扩展时。
优点：
    抽象和实现相分离
    优秀的扩展能力
"""

from abc import ABCMeta, abstractmethod

# 抽象
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

# 实现者
class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass

# 细化抽象者
# 形状上进行扩展（如果需要扩展更多的形状，只需要新增形状的类即可）
class Rectangle(Shape):
    name = '长方形'
    def __init__(self, color):
        super(Rectangle, self).__init__(color)

    def draw(self):
        # 长方形逻辑
        self.color.paint(self)  # 注意理解

class Circle(Shape):
    name = '圆形'

    def __init__(self, color):
        super(Circle, self).__init__(color)

    def draw(self):
        # 圆形逻辑
        self.color.paint(self)

# 具体实现者（写大块逻辑的地方，此处是paint）
# 在颜色上进行扩展(如果需要扩展更多的颜色，只需要新增颜色的类即可）
class Red(Color):
    def paint(self, shape):
        print(f"红色的{shape.name}")


class Blue(Color):
    def paint(self, shape):
        print(f"蓝色的{shape.name}")


# Client
a = Rectangle(Red())  # 红色长方形
a.draw()
b = Circle(Blue())  # 蓝色的圆
b.draw()
