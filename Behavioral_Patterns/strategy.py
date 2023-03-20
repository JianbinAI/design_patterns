# coding=utf-8

"""
行为型--策略模式
内容：
    定义一系列的算法，把它们一个个封装起来，并且使它们可相互替换。本模式使得算法可独立于使用它的客户而变化。
角色：
    抽象策略（Strategy）
    具体策略（ConcreteStrategy）
    上下文（Context）：连接策略类和高层代码，可以选择策略。比如打车时，高峰期和平时，应该选择不同的策略。
适用场景：
    许多相关的类仅仅是行为有异
    需要使用一个算法的不同变体
    算法使用了客户端无需知道的数据。比如算法中需要当前时间，那么在Context中自动生成传入。
    一个类中的多种行为以多个条件语句的形式存在，可以将这些行为封装在不同的策略类中。
优点：
    定义了一系列可重用的算法和行为
    消除了一些条件语句
    可以提供相同行为的不同实现
缺点：
    客户必须了解不同的策略
"""
from abc import ABCMeta, abstractmethod
import random


# 抽象策略
class Sort(metaclass=ABCMeta):
    @abstractmethod
    def sort(self, data):
        pass

# 快排策略
class QuickSort(Sort):
    def quick_sort(self, data, left, right):
        if left < right:
            mid = self.partition(data, left, right)
            self.quick_sort(data, left, mid - 1)
            self.quick_sort(data, mid + 1, right)

    def partition(self, data, left, right):
        tmp = data[left]
        while left < right:
            while left < right and data[right] >= tmp:
                right -= 1
            data[left] = data[right]
            while left < right and data[left] <= tmp:
                left += 1
            data[right] = data[left]
        data[left] = tmp
        return left

    def sort(self, data):
        print("快速排序")
        return self.quick_sort(data, 0, len(data) - 1)


# 归并策略
class MergeSort(Sort):
    def merge(self, data, low, mid, high):
        i = low
        j = mid + 1
        ltmp = []
        while i <= mid and j <= high:
            if data[i] <= data[j]:
                ltmp.append(data[i])
                i += 1
            else:
                ltmp.append(data[j])
                j += 1

        while i <= mid:
            ltmp.append(data[i])
            i += 1

        while j <= high:
            ltmp.append(data[j])
            j += 1

        data[low:high + 1] = ltmp

    def merge_sort(self, data, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(data, low, mid)
            self.merge_sort(data, mid + 1, high)
            self.merge(data, low, mid, high)

    def sort(self, data):
        print("归并排序")
        return self.merge_sort(data, 0, len(data) - 1)


class Context:
    def __init__(self, data, strategy=None):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        if self.strategy:
            self.strategy.sort(self.data)
        else:
            raise TypeError


li = list(range(100000))
random.shuffle(li)

context = Context(li, MergeSort())
context.do_strategy()

random.shuffle(context.data)

context.set_strategy(QuickSort())
context.do_strategy()
