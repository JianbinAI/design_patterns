# coding=utf-8

"""
创建型--工厂方法模式
内容：
    定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类。
角色：
    抽象工厂角色（Creator），定义工厂类接口
    具体工厂角色（Concrete Creator），隐藏对象创建细节
    抽象产品角色（Product），定义产品接口
    具体产品角色（Concrete Product），实现产品接口
特点：
    工厂方法模式相比简单工厂模式将每个具体产品都对应了一个具体工厂。
适用场景：
    需要生产多种、大量复杂对象的时候
    需要降低耦合度的时候
    当系统中的产品种类需要经常扩展的时候
优点：
    每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
    隐藏了对象创建的实现细节
缺点：
    每增加一个具体产品类，就必须增加一个相应的具体工厂类
"""

from abc import ABCMeta, abstractmethod


# 抽象产品角色
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

# 具体产品角色
class Alipay(Payment):
    def pay(self, money):
        print(f"支付宝支付{money}元.")

# 具体产品角色
class ApplePay(Payment):
    def pay(self, money):
        print(f"苹果支付支付{money}元.")

# 抽象工厂角色
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

# 具体工厂角色
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

# 具体工厂角色
class ApplePayFactory(PaymentFactory):
    def create_payment(self):
        return ApplePay()

# 先实例化具体工厂类，再由具体工厂类实例化具体产品
af = AlipayFactory()
ali = af.create_payment()
ali.pay(120)