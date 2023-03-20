# coding=utf-8

"""
结构型--外观模式
内容：
    为子系统的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
角色：
    外观（facade）
    子系统类（subsystem classes)
优点：
    减少系统相互依赖
    提高了灵活性
    提高了安全性
"""

# 子系统类
class CPU:
    def run(self):
        print("CPU start")

    def stop(self):
        print("CPU stopped")


# 子系统类
class Disk:
    def start(self):
        print('disk start')

    def stop(self):
        print('disk stopped')


# 子系统类
class Memory:
    def run(self):
        print('内存充电')

    def stop(self):
        print('内存断电')

# 外观
class Computer:
    def __init__(self, cpu, disk, memory):
        self.cpu = cpu
        self.disk = disk
        self.memory = memory

    def run(self):
        self.cpu.run()
        self.disk.start()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


# Client
c = Computer(CPU(), Disk(), Memory())
c.run()
c.stop()
