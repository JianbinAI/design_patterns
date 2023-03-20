# coding=utf-8

"""
创建型--单例模式
内容：
    保证一个类只有一个实例，并提供一个访问它的全局访问点。
角色：
    单例（Singleton）
适用场景：
    当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时
优点：
    对唯一实例的受控访问
    单例相当于全局变量，但防止了命名空间被污染
其它：
    与单例模式功能相似的概念：全局变量、静态变量（方法）
单例模式的几种实现方式：
    1. __new__ 方式
"""

# ==========================
# __new__ 方式
# ==========================
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name):
        self.name = name


a = MyClass("a")
b = MyClass('b')
print(a.name)
print(b.name)  # b
print(id(a), id(b))


# ==========================
# 装饰器
# ==========================
# 方式一：
def singleton(cls, *args, **kw):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance


@singleton
class myclass:
    pass

class1 = myclass()
class2 = myclass()

assert class1 == class2


# 方式二：和上面装饰器思路是一样的。只是写到类方法里。
class Foo:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls._instance:
            return cls._instance
        else:
            obj = cls()
            cls._instance = obj
            return obj

# 创建实例
obj = Foo.get_instance()


# ==========================
# 文件单例模式
# ==========================
# step1: 在一个py文件中定义一个单例类并实例化
class Singleton(object):
    def __init__(self):
        pass

    def foo(self):
        pass

    def bar(self):
        pass

instance = Singleton()


# step2: 在其它文件中导入实例化对象，每次都是操作同一个实例
# from Singleton import instance

instance.foo()
instance.bar()