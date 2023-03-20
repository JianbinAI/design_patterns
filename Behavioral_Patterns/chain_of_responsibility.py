# coding=utf-8

"""
行为型--责任链模式
内容：
    使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，
    并沿着这条链传递该请求，直到有一个对象处理它为止。
角色：
    抽象处理者（Handler）
    具体处理者（ConcreteHandler）
    客户端（Client）
适用场景：
    有多个对象可以处理一个请求，哪个对象处理由运行时决定
    在不明确接收者的情况下，向多个对象中的一个提交一个请求
优点：
    降低耦合度：一个对象无需知道是其他哪一个对象处理其请求
"""

from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManagerHandler(Handler):
    def handle_leave(self, day):
        if day < 10:
            print("总经理批准%d天假"%day)
        else:
            print("总经理叫你辞职！")


class DepartmentManagerHandler(Handler):
    def __init__(self):
        self.superior = GeneralManagerHandler()

    def handle_leave(self, day):
        if day < 7:
            print("部门经理批准%d天假"%day)
        else:
            print("部门经理无权准假")
            self.superior.handle_leave(day)


class ProjectDirectorHandler(Handler):
    def __init__(self):
        self.superior = DepartmentManagerHandler()

    def handle_leave(self, day):
        if day < 3:
            print("项目主管批准%d天假"%day)
        else:
            print("项目主管无权准假")
            self.superior.handle_leave(day)

# 只需要向直接上级请假即可
day = 11
h = ProjectDirectorHandler()
h.handle_leave(day)