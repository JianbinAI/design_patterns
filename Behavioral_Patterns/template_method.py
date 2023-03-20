# coding=utf-8

"""
行为型--模板方法模式
内容：
    定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。
    模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
角色：
    抽象类（AbstractClass）：定义抽象的原子操作（钩子操作）；实现一个模板方法作为算法的骨架
    具体类（ConcreteClass）：实现原子操作
适用场景：
    一次性实现一个算法的不变的部分
    各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复
    控制子类扩展
"""

from abc import ABCMeta, abstractmethod


# 抽象类
class IOHandler(metaclass=ABCMeta):
    @abstractmethod
    def open(self, name):
        pass

    @abstractmethod
    def deal(self, change):
        pass

    @abstractmethod
    def close(self):
        pass

    # 这个就是--模板方法
    def process(self, name, change):
        self.open(name)
        self.deal(change)
        self.close()


# 具体类（其他程序员需要实现父类的抽象方法即可）
class FileHandler(IOHandler):
    def open(self, name):
        self.file = open(name,"w")

    def deal(self, change):
        self.file.write(change)

    def close(self):
        self.file.close()


# Client
f = FileHandler()
f.process("abc.txt", "Hello World")