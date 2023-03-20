# coding=utf-8

"""
结构型--适配器模式
内容：
    将一个类的接口转换成客户希望的另一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
    就单来说就是实现接口一致和代码复用，如果接口不一致，写一个转接头。
角色：
    目标接口（Target）
    待适配的类（Adaptee）
    适配器（Adapter）
两种实现方式：
    类适配器：使用多继承
    对象适配器：使用组合
适用场景：
    想使用一个已经存在的类，而它的接口不符合要求
    （对象适配器）想使用一些已经存在的子类，但不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。
"""

from abc import abstractmethod, ABCMeta

# 目标接口
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元"%money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元"%money)

#------待适配类:此处需要吧cost接口适配成pay接口使得高层客户端能统一使用pay调用------
class WechatPay:
    def cost(self, money):
        print("微信支付%s元"%money)


#类适配器
class RealWechatPay(WechatPay, Payment):
    def pay(self, money):
        return self.cost(money)

# 对象适配器
class RealWechatPay2(Payment):
    def __init__(self, payment):
        self.payment = payment  # 需要传入待适配的类的实例（此处是WechatPay()）

    def pay(self, money):
        return self.payment.cost(money)

p = RealWechatPay2(WechatPay())
p.pay(111)
