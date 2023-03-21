- [Python设计模式](#python----)
  * [1. 设计模式简介](#1-------)
  * [2. 设计模式的六大原则](#2----------)
    + [2.1 开闭原则（Open Close Principle）](#21------open-close-principle-)
    + [2.2 里氏代换原则（Liskov Substitution Principle）](#22--------liskov-substitution-principle-)
    + [2.3 依赖倒转原则（Dependence Inversion Principle）](#23--------dependence-inversion-principle-)
    + [2.4 接口隔离原则（Interface Segregation Principle）](#24--------interface-segregation-principle-)
    + [2.5 迪米特法则，又称最少知道原则（Demeter Principle）](#25----------------demeter-principle-)
    + [2.6 合成复用原则（Composite Reuse Principle）](#26--------composite-reuse-principle-)
  * [3. 设计模式的分类](#3--------)
    + [3.1 创建型模式（Creational Patterns）](#31-------creational-patterns-)
      - [3.1.1 工厂模式（Factory Pattern）](#311------factory-pattern-)
      - [3.1.2 工厂方法模式（Factory Method Pattern）](#312--------factory-method-pattern-)
      - [3.1.3 抽象工厂模式（Abstract Factory Pattern）](#313--------abstract-factory-pattern-)
      - [3.1.4 单例模式（Singleton Pattern）](#314------singleton-pattern-)
      - [3.1.5 建造者模式（Builder Pattern）](#315-------builder-pattern-)
      - [3.1.6 原型模式（Prototype Pattern）](#316------prototype-pattern-)
    + [3.2 结构型模式（Structural Patterns）](#32-------structural-patterns-)
      - [3.2.1 适配器模式（Adapter Pattern）](#321-------adapter-pattern-)
      - [3.2.2 桥接模式（Bridge Pattern）](#322------bridge-pattern-)
      - [3.2.3 组合模式（Composite Pattern）](#323------composite-pattern-)
      - [3.2.4 外观模式（Facade Pattern）](#324------facade-pattern-)
      - [3.2.5 代理模式（Proxy Pattern）](#325------proxy-pattern-)
      - [3.2.6 过滤器模式（Filter、Criteria Pattern）](#326-------filter-criteria-pattern-)
      - [3.2.7 装饰器模式（Decorator Pattern）](#327-------decorator-pattern-)
      - [3.2.8 享元模式（Flyweight Pattern）](#328------flyweight-pattern-)
    + [3.3 行为型模式（Behavioral Patterns）](#33-------behavioral-patterns-)
      - [3.3.1 责任链模式（Chain of Responsibility Pattern）](#331-------chain-of-responsibility-pattern-)
      - [3.3.2 策略模式（Strategy Pattern）](#332------strategy-pattern-)
      - [3.3.3 模板模式（Template Pattern）](#333------template-pattern-)
      - [3.3.4 观察者模式（Observer Pattern）](#334-------observer-pattern-)
      - [3.3.5 命令模式（Command Pattern）](#335------command-pattern-)
      - [3.3.6 解释器模式（Interpreter Pattern）](#336-------interpreter-pattern-)
      - [3.3.7 迭代器模式（Iterator Pattern）](#337-------iterator-pattern-)
      - [3.3.8 中介者模式（Mediator Pattern）](#338-------mediator-pattern-)
      - [3.3.9 备忘录模式（Memento Pattern）](#339-------memento-pattern-)
      - [3.3.10 状态模式（State Pattern）](#3310------state-pattern-)
      - [3.3.11 空对象模式（Null Object Pattern）](#3311-------null-object-pattern-)
      - [3.3.12 访问者模式（Visitor Pattern）](#3312-------visitor-pattern-)

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

### 3.1 创建型模式（Creational Patterns）

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

[示例--简单工厂模式](./Creational_Patterns/simple_factory.py)

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

[示例--工厂方法模式](./Creational_Patterns/factory_method.py)

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

[示例--抽象工厂模式](./Creational_Patterns/abstract_factory.py)

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

[示例--单例模式](./Creational_Patterns/singleton.py)

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

[示例--建造者模式](./Creational_Patterns/builder.py)

#### 3.1.6 原型模式（Prototype Pattern）

待更新……

### 3.2 结构型模式（Structural Patterns）

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

[示例--适配器模式](./Structural_Patterns/adapter.py)

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

[示例--桥接模式](./Structural_Patterns/bridge.py)

#### 3.2.3 组合模式（Composite Pattern）

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

[示例--组合模式](./Structural_Patterns/composite.py)

#### 3.2.4 外观模式（Facade Pattern）

**内容：**
    为子系统的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。

**角色：**
    外观（facade）
    子系统类（subsystem classes)

**优点：**
    减少系统相互依赖
    提高了灵活性
    提高了安全性

[示例--外观模式](./Structural_Patterns/facade.py)

#### 3.2.5 代理模式（Proxy Pattern）

**内容：**
    为其他对象提供一种代理以控制对这个对象的访问。

**角色：**
    抽象实体（Subject）
    实体（RealSubject）
    代理（Proxy）

**使用场景：**
    远程代理：为远程的对象提供代理。
    理虚代理：根据需要创建很大的对象。
    保护代理：控制对原始对象的访问，用于对象有不同访问权限时

**优点：**
    远程代理：可以隐藏对象位于远程地址空间的事实。高层代码不需要亲自访问远程的对象，也不需要知道对象在本地还是远程
    虚代理：可以进行优化，例如根据要求创建对象。比如手机滑屏，未显示区域会提前加载，但是图像又很耗费内存，因此加载的是图像代理，当到达某个临界值，才加载真实图像。再比如浏览器的无图模式，点击时才创建图片。保护代理：允许在访问一个对象时有一些附加的内务处理

[示例--代理模式](./Structural_Patterns/agent.py)

#### 3.2.6 过滤器模式（Filter、Criteria Pattern）

待更新……

#### 3.2.7 装饰器模式（Decorator Pattern）

待更新……

#### 3.2.8 享元模式（Flyweight Pattern）

待更新……

### 3.3 行为型模式（Behavioral Patterns）

这些设计模式特别关注对象之间的通信。

#### 3.3.1 责任链模式（Chain of Responsibility Pattern）

**内容：**
    使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，
    并沿着这条链传递该请求，直到有一个对象处理它为止。

**角色：**
    抽象处理者（Handler）
    具体处理者（ConcreteHandler）
    客户端（Client）

**适用场景：**
    有多个对象可以处理一个请求，哪个对象处理由运行时决定
    在不明确接收者的情况下，向多个对象中的一个提交一个请求

**优点：**
    降低耦合度：一个对象无需知道是其他哪一个对象处理其请求

[示例--责任链模式](./Behavioral_Patterns/chain_of_responsibility.py)

#### 3.3.2 策略模式（Strategy Pattern）

**内容：**
    定义一系列的算法，把它们一个个封装起来，并且使它们可相互替换。本模式使得算法可独立于使用它的客户而变化。

**角色：**
    抽象策略（Strategy）
    具体策略（ConcreteStrategy）
    上下文（Context）：连接策略类和高层代码，可以选择策略。比如打车时，高峰期和平时，应该选择不同的策略。

**适用场景：**
    许多相关的类仅仅是行为有异
    需要使用一个算法的不同变体
    算法使用了客户端无需知道的数据。比如算法中需要当前时间，那么在Context中自动生成传入。
    一个类中的多种行为以多个条件语句的形式存在，可以将这些行为封装在不同的策略类中。

**优点：**
    定义了一系列可重用的算法和行为
    消除了一些条件语句
    可以提供相同行为的不同实现

**缺点：**
    客户必须了解不同的策略

[示例--策略模式](./Behavioral_Patterns/strategy.py)

#### 3.3.3 模板模式（Template Pattern）

**内容：**
    定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。
    模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

**角色：**
    抽象类（AbstractClass）：定义抽象的原子操作（钩子操作）；实现一个模板方法作为算法的骨架
    具体类（ConcreteClass）：实现原子操作

**适用场景：**
    一次性实现一个算法的不变的部分
    各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复
    控制子类扩展

[示例--模板方法模式](./Behavioral_Patterns/template_method.py)

#### 3.3.4 观察者模式（Observer Pattern）

[示例--观察者模式](./Behavioral_Patterns/observer.py)

#### 3.3.5 命令模式（Command Pattern）

待更新……

#### 3.3.6 解释器模式（Interpreter Pattern）

待更新……

#### 3.3.7 迭代器模式（Iterator Pattern）

待更新……

#### 3.3.8 中介者模式（Mediator Pattern）

待更新……

#### 3.3.9 备忘录模式（Memento Pattern）

待更新……

#### 3.3.10 状态模式（State Pattern）

待更新……

#### 3.3.11 空对象模式（Null Object Pattern）

待更新……

#### 3.3.12 访问者模式（Visitor Pattern）

待更新……
