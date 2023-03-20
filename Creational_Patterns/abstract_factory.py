# coding=utf-8

"""
创建型--抽象工厂模式
内容:
    定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象。
    例：生产一部手机，需要手机壳、CPU、操作系统三类对象进行组装，其中每类对象都有不同的种类。对每个具体工厂，
    分别生产一部手机所需要的三个对象。
角色:
    抽象工厂角色（Creator）
    具体工厂角色（Concrete Creator）
    抽象产品角色（Product）
    具体产品角色（Concrete Product）
    客户端（Client）
特点:
    相比工厂方法模式，抽象工厂模式中的每个具体工厂都生产一套产品。该模式只负责生成，组装由客户端负责
使用场景:
    系统要独立于产品的创建与组合时
    强调一系列相关的产品对象的设计以便进行联合使用时
    提供一个产品类库，想隐藏产品的具体实现时
优点:
    将客户端与类的具体实现相分离
    每个工厂创建了一个完整的产品系列，使得易于交换产品系列
    有利于产品的一致性（即产品之间的约束关系）
缺点:
    难以支持新种类的（抽象）产品。比如加一个电池，所有都要大改。
"""

from abc import abstractmethod, ABCMeta

# ------抽象产品------

class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass

class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# ------抽象工厂------

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# ------具体产品------

class SmallShell(PhoneShell):
    def show_shell(self):
        print("普通手机小手机壳")

class BigShell(PhoneShell):
    def show_shell(self):
        print("普通手机大手机壳")

class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙CPU")


class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")


class Android(OS):
    def show_os(self):
        print("Android系统")


class IOS(OS):
    def show_os(self):
        print("iOS系统")


# ------具体工厂------
# 创建一系列相关或相互依赖的对象，有利于产品一致性，比如Iphone不能用联发科，Mi不能用IOS
class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return BigShell()


class HuaweiFactory(PhoneFactory):
    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return SmallShell()


class IPhoneFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()


# ------客户端------
# 负责具体组装
class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print("手机信息:")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()


def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)


p1 = make_phone(HuaweiFactory())
p1.show_info()