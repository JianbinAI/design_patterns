# coding=utf-8

"""
创建型--简单工厂模式
内容：不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例。
角色：
    工厂角色（Creator）
    具体产品角色（Concrete Product）
    抽象产品角色（Product）
优点：
    隐藏了对象创建的实现细节；
    客户端不需要修改代码
缺点：
    违反了单一职责原则，将创建逻辑集中到一个工厂类里；
    当添加新产品时，需要修改工厂类代码，违反了开闭原则
"""

from abc import ABCMeta, abstractmethod


# 抽象产品角色
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

# 具体产品角色
class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print(f"使用花呗支付{money}元.")
        else:
            print(f"使用余额支付{money}元.")

# 具体产品角色
class ApplePay(Payment):
    def pay(self, money):
        print(f"苹果支付{money}元.")


# 工厂角色
class PaymentFactory(object):
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay(use_huabei=False)
        elif method == 'huabei':
            return Alipay(use_huabei=True)
        elif method == 'apple':
            return ApplePay()
        else:
            raise ValueError(f"不支持{method}支付方式。")

# Client
payment = PaymentFactory()
alipay = payment.create_payment('alipay')
alipay.pay(100)
