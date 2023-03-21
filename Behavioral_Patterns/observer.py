# coding=utf-8

"""
行为型--观察者模式
内容：
    定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时, 所有依赖于它的对象都得到通知并被自动更新。
    观察者模式又称“发布-订阅”模式。

    比如，我们根据excel表格数据生成饼状图、柱状图、折线图，一旦我们更新了excel表格数据，那么这些图表也会随之更新。
    这些图表就是观察者。
角色：
    抽象主体（Subject）
    具体主体（ConcreteSubject）——发布者
    抽象观察者（Observer）
    具体观察者（ConcreteObserver）——订阅者
适用场景：
    当一个抽象模型有两方面，其中一个方面依赖于另一个方面。将这两者封装在独立对象中以使它们可以各自独立地改变和复用
    当对一个对象的改变需要同时改变其它对象，而不知道具体有多少对象有待改变
    当一个对象必须通知其它对象，而它又不能假定其它对象是谁。换言之，你不希望这些对象是紧密耦合的。
优点：
    目标和观察者之间的抽象耦合最小
    支持广播通信
"""

from abc import ABCMeta, abstractmethod


# 抽象观察者/订阅者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):  # notice 是 Notification的实例
        pass


# 抽象发布者
class Notification(object):
    def __init__(self):
        self.observers = []

    def attach(self, obs):  # 增加观察者
        self.observers.append(obs)

    def detach(self, obs):  # 移除观察者
        self.observers.remove(obs)

    def notify(self):  # 通知/广播
        for obj in self.observers:
            obj.update(self)


# 具体的发布者--具体的天气通知
class WeatherNotifications(Notification):
    def __init__(self, weather_info=None):
        super().__init__()
        self.__weather_info = weather_info

    def detach(self, obs):
        super().detach(obs)

    @property
    def weather_info(self):
        return self.__weather_info

    @weather_info.setter
    def weather_info(self, info):
        self.__weather_info = info
        self.notify() # 自动传入消息对象self


# 具体观察者/订阅者
class Subscriber(Observer):
    def __init__(self):
        self.weather_info = None

    def update(self, notification):
        self.weather_info = notification.weather_info


# Client
# 实例化天气消息发布者
notice = WeatherNotifications()

# 实例化订阅者
Lena = Subscriber()
Ayhan = Subscriber()

# 为天气消息发布者添加订阅对象
notice.attach(Lena)
notice.attach(Ayhan)

# 发布天气消息
notice.weather_info = '今天阳光明媚'
# 订阅者收到消息
print(Lena.weather_info)  # 今天阳光明媚
print(Ayhan.weather_info)  # 今天阳光明媚

# 移除订阅者
notice.detach(Ayhan)
# 发布最新消息
notice.weather_info = '暴风雨即将来临'
print(Lena.weather_info)  # 暴风雨即将来临
print(Ayhan.weather_info)  # 今天阳光明媚
