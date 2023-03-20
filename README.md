[toc]

# Python设计模式

## 1. 设计模式简介

1994 年，由 Erich Gamma、Richard Helm、Ralph Johnson 和 John Vlissides 四人合著出版了一本名为 **Design Patterns - Elements of Reusable Object-Oriented Software（中文译名：设计模式 - 可复用的面向对象软件元素）** 的书，该书首次提到了软件开发中设计模式的概念。

四位作者合称 **GOF（四人帮，全拼 Gang of Four）**。他们所提出的设计模式主要是基于以下的面向对象设计原则。

- 对接口编程而不是对实现编程。
- 优先使用对象组合而不是继承。

设计模式（design pattern）是一套被反复使用的、多数人知晓的、经过分类编目的、代码设计经验的总结。使用设计模式是为了重用代码、让代码更容易被他人理解、保证代码可靠性。 毫无疑问，设计模式于己于他人于系统都是多赢的，设计模式使代码编制真正工程化，设计模式是软件工程的基石，如同大厦的一块块砖石一样。项目中合理地运用设计模式可以完美地解决很多问题，每种模式在现实中都有相应的原理来与之对应，每种模式都描述了一个在我们周围不断重复发生的问题，以及该问题的核心解决方案，这也是设计模式能被广泛应用的原因。

## 2. 设计模式的六大原则

###  2.1 开闭原则（Open Close Principle）

开闭原则的意思是：**对扩展开放，对修改关闭**。在程序需要进行拓展的时候，不能去修改原有的代码，实现一个热插拔的效果。简言之，是为了使程序的扩展性好，易于维护和升级。想要达到这样的效果，我们需要使用接口和抽象类，后面的具体设计中我们会提到这点。

### 2.2 里氏代换原则（Liskov Substitution Principle）

里氏代换原则是面向对象设计的基本原则之一。 里氏代换原则中说，任何基类可以出现的地方，子类一定可以出现。LSP 是继承复用的基石，只有当派生类可以替换掉基类，且软件单位的功能不受到影响时，基类才能真正被复用，而派生类也能够在基类的基础上增加新的行为。里氏代换原则是对开闭原则的补充。实现开闭原则的关键步骤就是抽象化，而基类与子类的继承关系就是抽象化的具体实现，所以里氏代换原则是对实现抽象化的具体步骤的规范。

### 2.3 依赖倒转原则（Dependence Inversion Principle）

这个原则是开闭原则的基础，具体内容：针对接口编程，依赖于抽象而不依赖于具体。

### 2.4 接口隔离原则（Interface Segregation Principle）

这个原则的意思是：使用多个隔离的接口，比使用单个接口要好。它还有另外一个意思是：降低类之间的耦合度。由此可见，其实设计模式就是从大型软件架构出发、便于升级和维护的软件设计思想，它强调降低依赖，降低耦合。

### 2.5 迪米特法则，又称最少知道原则（Demeter Principle）

最少知道原则是指：一个实体应当尽量少地与其他实体之间发生相互作用，使得系统功能模块相对独立。

### 2.6 合成复用原则（Composite Reuse Principle）

合成复用原则是指：尽量使用合成/聚合的方式，而不是使用继承。

## 3. 设计模式的分类

### 3.1 创建型模式

这些设计模式提供了一种在创建对象的同时隐藏创建逻辑的方式，而不是使用 new 运算符直接实例化对象。这使得程序在判断针对某个给定实例需要创建哪些对象时更加灵活。

#### 3.1.1 工厂模式（Factory Pattern）

**内容：**不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例。
**角色：**
    工厂角色（Creator）
    具体产品角色（Concrete Product）
    抽象产品角色（Product）
**优点：**
    隐藏了对象创建的实现细节；
    客户端不需要修改代码
**缺点：**
    违反了单一职责原则，将创建逻辑集中到一个工厂类里；
    当添加新产品时，需要修改工厂类代码，违反了开闭原则

[示例-简单工厂模式](./Creational_Patterns/simple_factory.py)

```python
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
```

#### 3.1.2 工厂方法模式（Factory Method Pattern）

**内容：**
    定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类。
**角色：**
    抽象工厂角色（Creator），定义工厂类接口
    具体工厂角色（Concrete Creator），隐藏对象创建细节
    抽象产品角色（Product），定义产品接口
    具体产品角色（Concrete Product），实现产品接口
**特点：**
    工厂方法模式相比简单工厂模式将每个具体产品都对应了一个具体工厂。
**适用场景：**
    需要生产多种、大量复杂对象的时候
    需要降低耦合度的时候
    当系统中的产品种类需要经常扩展的时候
**优点：**
    每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
    隐藏了对象创建的实现细节
**缺点：**
    每增加一个具体产品类，就必须增加一个相应的具体工厂类

```python
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
```

#### 3.1.3 抽象工厂模式（Abstract Factory Pattern）

**内容:**
    定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象。
    例：生产一部手机，需要手机壳、CPU、操作系统三类对象进行组装，其中每类对象都有不同的种类。对每个具体工厂，
    分别生产一部手机所需要的三个对象。
**角色:**
    抽象工厂角色（Creator）
    具体工厂角色（Concrete Creator）
    抽象产品角色（Product）
    具体产品角色（Concrete Product）
    客户端（Client）
**特点:**
    相比工厂方法模式，抽象工厂模式中的每个具体工厂都生产一套产品。该模式只负责生成，组装由客户端负责
**使用场景:**
    系统要独立于产品的创建与组合时
    强调一系列相关的产品对象的设计以便进行联合使用时
    提供一个产品类库，想隐藏产品的具体实现时
**优点:**
    将客户端与类的具体实现相分离
    每个工厂创建了一个完整的产品系列，使得易于交换产品系列
    有利于产品的一致性（即产品之间的约束关系）
**缺点:**
    难以支持新种类的（抽象）产品。比如加一个电池，所有都要大改。

```python
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
```

#### 3.1.4 单例模式（Singleton Pattern）

**内容：**
    保证一个类只有一个实例，并提供一个访问它的全局访问点。
**角色：**
    单例（Singleton）
**适用场景：**
    当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时
**优点：**
    对唯一实例的受控访问
    单例相当于全局变量，但防止了命名空间被污染

```python
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
```

#### 3.1.5 建造者模式（Builder Pattern）

**内容：**
    将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。

**角色：**
    抽象建造者（Builder）
    具体建造者（Concrete Builder），隐藏内部结构
    指挥者（Director），隐藏装配过程
    产品（Product）
**特点：**
    建造者模式与抽象工厂模式相似，也用来创建复杂对象。主要区别是建造者模式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象。

**使用场景：**
    当创建复杂对象的算法（Director）应该独立于该对象的组成部分以及它们的装配方式（Builder）时
    当构造过程允许被构造的对象有不同的表示时（不同Builder）。
**优点：**
    隐藏了一个产品的内部结构和装配过程
    将构造代码与表示代码分开
    可以对构造过程进行更精细的控制

```python
from abc import abstractmethod, ABCMeta

#------产品------
# 游戏角色
class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.arm = arm
        self.leg = leg
        self.body = body

    def __str__(self):
        return f"{self.face}, {self.arm}, {self.body}, {self.leg}"


#------建造者------
# 抽象建造者
class PlayerBuilder(metaclass=ABCMeta): # 捏脸
    @abstractmethod
    def build_face(self):
        pass
    @abstractmethod
    def build_arm(self):
        pass
    @abstractmethod
    def build_leg(self):
        pass
    @abstractmethod
    def build_body(self):
        pass
    @abstractmethod
    def get_player(self):
        pass

# 具体建造者
class BeautifulWomanBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()
    def build_face(self):
        self.player.face = "漂亮脸蛋"
    def build_arm(self):
        self.player.arm = "细胳膊"
    def build_body(self):
        self.player.body = "细腰"
    def build_leg(self):
        self.player.leg = "长腿"
    def get_player(self):
        return self.player

#------指挥者------
class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_arm()
        builder.build_leg()
        builder.build_face()
        return builder.get_player()


# Client
director = PlayerDirector() # setp1: 实例化指挥者
builder = BeautifulWomanBuilder() # step2: 实例化建造者
p = director.build_player(builder) # step3: 指挥者指挥建造者创建游戏角色
print(p)
```

#### 3.1.6 原型模式（Prototype Pattern）

待更新……

### 3.2 结构型模式

这些设计模式关注类和对象的组合。继承的概念被用来组合接口和定义组合对象获得新功能的方式。

#### 3.2.1 适配器模式（Adapter Pattern）

**内容：**
    将一个类的接口转换成客户希望的另一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
    就单来说就是实现接口一致和代码复用，如果接口不一致，写一个转接头。
**角色：**
    目标接口（Target）
    待适配的类（Adaptee）
    适配器（Adapter）
**两种实现方式：**
    类适配器：使用多继承
    对象适配器：使用组合
**适用场景：**
    想使用一个已经存在的类，而它的接口不符合要求
    （对象适配器）想使用一些已经存在的子类，但不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。

```python
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
```

#### 3.2.2 桥接模式（Bridge Pattern）

**内容：**
    将一事物的两个维度分离，使其都可以独立地变化
**角色：**
    抽象（Abstraction）
    细化抽象（RefinedAbstraction）
    实现者（Implementor）
    具体实现者（ConcreteImplementor）
**应用场景：**
    当事物有两个维度上的表现，两个维度（抽象，实现者）都可能扩展时。
**优点：**
    抽象和实现相分离
    优秀的扩展能力

```python
from abc import ABCMeta, abstractmethod

# 抽象
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

# 实现者
class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass

# 细化抽象者
# 形状上进行扩展（如果需要扩展更多的形状，只需要新增形状的类即可）
class Rectangle(Shape):
    name = '长方形'
    def __init__(self, color):
        super(Rectangle, self).__init__(color)

    def draw(self):
        # 长方形逻辑
        self.color.paint(self)  # 注意理解

class Circle(Shape):
    name = '圆形'

    def __init__(self, color):
        super(Circle, self).__init__(color)

    def draw(self):
        # 圆形逻辑
        self.color.paint(self)

# 具体实现者（写大块逻辑的地方，此处是paint）
# 在颜色上进行扩展(如果需要扩展更多的颜色，只需要新增颜色的类即可）
class Red(Color):
    def paint(self, shape):
        print(f"红色的{shape.name}")


class Blue(Color):
    def paint(self, shape):
        print(f"蓝色的{shape.name}")


# Client
a = Rectangle(Red())  # 红色长方形
a.draw()
b = Circle(Blue())  # 蓝色的圆
b.draw()
```

#### 3.2.3 过滤器模式（Filter、Criteria Pattern）

待更新……

#### 3.2.4 组合模式（Composite Pattern）

**内容：**
    将对象组合成树形结构以表示“部分-整体”的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。
    其实就是用设计模式的方式来表达树形结构，一个节点是一个部分，一个子树是一个整体。
**角色：**
    抽象组件（Component）：抽象组件中定义的方法，叶子和复合组件都要实现
    叶子组件（Leaf）
    复合组件（Composite）：非叶子组件
    客户端（Client）
**适用场景：**
    表示对象的“部分-整体”层次结构（特别是结构是递归的）
    希望用户忽略组合对象与单个对象的不同，用户统一地使用组合结构中的所有对象
**优点：**
    定义了包含基本对象和组合对象的类层次结构
    简化客户端代码，即客户端可以一致地使用组合对象和单个对象
    更容易增加新类型的组件

```python
from abc import abstractmethod, ABCMeta


# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def add(self, graphic):
        pass

    def getchildren(self):
        pass

# 图元
# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(self)

    def add(self, graphic):
        raise TypeError

    def getchildren(self):
        raise TypeError

    def __str__(self):
        return "点(%s, %s)" % (self.x, self.y)

# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        print(self)

    def add(self, graphic):
        raise TypeError

    def getchildren(self):
        raise TypeError

    def __str__(self):
        return "线段[%s, %s]" % (self.p1, self.p2)

# 复合组件
class Picture(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic):
        self.children.append(graphic)

    def getchildren(self):
        return self.children

    def draw(self):
        print("------复合图形------")
        for g in self.children:
            g.draw()
        print("------END------")


pic1 = Picture()
point = Point(2,3)
pic1.add(point)
pic1.add(Line(Point(1,2), Point(4,5)))
pic1.add(Line(Point(0,1), Point(2,1)))

pic2 = Picture()
pic2.add(Point(-2,-1))
pic2.add(Line(Point(0,0), Point(1,1)))

pic = Picture()
pic.add(pic1)
pic.add(pic2)

pic.draw()
# pic1.draw()
# point.draw()
```

#### 3.2.5 装饰器模式（Decorator Pattern）

待更新……

#### 3.2.6 外观模式（Facade Pattern）

**内容：**
    为子系统的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
**角色：**
    外观（facade）
    子系统类（subsystem classes)
**优点：**
    减少系统相互依赖
    提高了灵活性
    提高了安全性

```python
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
```

#### 3.2.7 享元模式（Flyweight Pattern）

待更新……

#### 3.2.8 代理模式（Proxy Pattern）

### 3.3 行为型模式

这些设计模式特别关注对象之间的通信。

#### 3.3.1 责任链模式（Chain of Responsibility Pattern）

#### 3.3.2 命令模式（Command Pattern）

#### 3.3.3 解释器模式（Interpreter Pattern）

#### 3.3.4 迭代器模式（Iterator Pattern）

#### 3.3.5 中介者模式（Mediator Pattern）

#### 3.3.6 备忘录模式（Memento Pattern）

#### 3.3.7 观察者模式（Observer Pattern）

#### 3.3.8 状态模式（State Pattern）

#### 3.3.9 空对象模式（Null Object Pattern）

#### 3.3.10 策略模式（Strategy Pattern）

#### 3.3.11 模板模式（Template Pattern）

#### 3.3.12 访问者模式（Visitor Pattern）

