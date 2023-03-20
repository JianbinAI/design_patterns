# coding=utf-8

"""
结构型--代理模式
内容：
    为其他对象提供一种代理以控制对这个对象的访问。
角色：
    抽象实体（Subject）
    实体（RealSubject）
    代理（Proxy）
使用场景：
    远程代理：为远程的对象提供代理。
    理虚代理：根据需要创建很大的对象。
    保护代理：控制对原始对象的访问，用于对象有不同访问权限时
优点：
    远程代理：可以隐藏对象位于远程地址空间的事实。高层代码不需要亲自访问远程的对象，也不需要知道对象在本地还是远程
    虚代理：可以进行优化，例如根据要求创建对象。比如手机滑屏，未显示区域会提前加载，但是图像又很耗费内存，
        因此加载的是图像代理，当到达某个临界值，才加载真实图像。再比如浏览器的无图模式，点击时才创建图片。
    保护代理：允许在访问一个对象时有一些附加的内务处理
"""

from abc import ABCMeta, abstractmethod


# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass
    def set_content(self, content):
        pass


# 实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        print("读取%s文件内容"%filename)
        f = open(filename)
        self.__content = f.read()
        f.close()

    def get_content(self):
        return self.__content

    def set_content(self, content):
        f = open(self.filename, 'w')
        f.write(content)
        self.__content = content
        f.close()


# 代理
# ProxyA 就是给真实对象套了一个马甲，和使用真实对象没区别
class ProxyA(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        return self.subj.set_content(content)


# 虚代理：创建时不会立即加载真实对象，而是在调用后才加载（手机的无图模式就是这个原理）
class ProxyB(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

x = ProxyB('abc.txt')
#print(x.get_content())


# 保护代理：控制对真实对象的修改
class ProxyC(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        self.subj.get_content()

    def set_content(self, content):
        raise PermissionError

filename = "abc.txt"
username = input()
if username!="admin":
    p = ProxyC(filename)
else:
    p = ProxyA(filename)

print(p.get_content())
