""" 设计模式 """

class DesignerNotebook():
    
    def work(self):
        exec(self.p)
        
    def get_text(self):
        return self.p

class Singleton(DesignerNotebook):
    # 全局只初始化一次 一个类只能存在一个实例 底层内存共享
    def update(self,class_name):
        self.p = f"""
class {class_name}:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self,value = None):
        # 只有第一次初始化时设置值，后续的初始化调用不会更改实例的值
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.value = value
"""   
        print(self.p)
        return self.p

class Factoryfs():
    """
    """
    def update(self,FactoryClassName,EnumClassName,Option1,Option2):
        self.p = f"""
from enum import Enum
from typing import List, Any

class {EnumClassName}(Enum):
    {Option1} = '{Option1}'
    {Option2} = '{Option2}'
    # 添加更多选项

class {FactoryClassName}:
    def __new__(cls, type: {EnumClassName}) -> Any:
        assert type.value in [i.value for i in {EnumClassName}]
        instance = None

        if type.value == '{Option1}':

            # instance = SomeClass(param1=value1, param2=value2)
            pass

        elif type.value == '{Option2}':

            # instance = AnotherClass(param1=value1, param2=value2)
            pass


        else:
            raise Exception('Unknown type')

        return instance
"""   
        print(self.p)
        return self.p
    
    


class Adapter():
    """
使用效果就是直接调用老接口的对象的话对方咩有这个方法,
那么就将老接口传入一个适配器,这样,老接口就有了新方法 有点像电源适配器,或者插头转换器
## 适配器模式


    """
    def update(self):
        self.p = """
class NewPrinter(ABC):
    def print_content(self,content):
        raise NotImplementedError
    
class Adapter(NewPrinter):
    def __init__(self, old_function):
        self.old_function = old_function
        
    def print_content(self, content):
        self.old_function.print(content)


"""   
        print(self.p)
        return self.p
    





class 装饰器():
    """
使用效果就是直接调用老接口的对象的话对方咩有这个方法,
那么就将老接口传入一个适配器,这样,老接口就有了新方法 有点像电源适配器,或者插头转换器


    """
    def update(self,decorator):
        self.p = f"""
import functools

def {decorator}(a = None):

    def outer_packing(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(a,'a')
            print(func.__name__)  # 函数名
            print(args)  # (1, 2)
            print(kwargs)  # 'c': 3
            return result
        return wrapper
    return outer_packing

"""   
        print(self.p)
        return self.p
    



# 迭代器

class 组合模式():
    """
# 理解了,是一种高级复杂的模式,类似于文件系统 文件是叶子 文件夹是节点,节点可以包括节点 节点也可以包括叶子,也会产生多级嵌套 
# 可以使用这种
# 使用组合模式
file1 = File("file1.txt")
file2 = File("file2.txt")

directory1 = Directory("dir1")
directory1.add(file1)

directory2 = Directory("dir2")
directory2.add(file2)
directory2.add(directory1)

print(directory2.operation())


    """
    def update(self,class_name):
        self.p = """
from abc import ABC, abstractmethod

# Component 接口
class FileSystemComponent(ABC):
    @abstractmethod
    def operation(self):
        pass

# Leaf 类
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"File: {self.name}"

# Composite 类
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def operation(self):
        results = [f"Directory: {self.name}"]
        for child in self.children:
            results.append(child.operation())
        return "\n".join(results)

"""   
        print(self.p)
        return self.p
    



class 组合模式():
    """
# 理解了,是一种高级复杂的模式,类似于文件系统 文件是叶子 文件夹是节点,节点可以包括节点 节点也可以包括叶子,也会产生多级嵌套 
# 可以使用这种
# 使用组合模式
file1 = File("file1.txt")
file2 = File("file2.txt")

directory1 = Directory("dir1")
directory1.add(file1)

directory2 = Directory("dir2")
directory2.add(file2)
directory2.add(directory1)

print(directory2.operation())


    """
    def update(self,class_name):
        self.p = """
from abc import ABC, abstractmethod

# Component 接口
class FileSystemComponent(ABC):
    @abstractmethod
    def operation(self):
        pass

# Leaf 类
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"File: {self.name}"

# Composite 类
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def operation(self):
        results = [f"Directory: {self.name}"]
        for child in self.children:
            results.append(child.operation())
        return "\n".join(results)

"""   
        print(self.p)
        return self.p
    






## 外观模式



```python

## 外观模式

# 子系统类
class TV:
    def on(self):
        print("TV is on")

    def off(self):
        print("TV is off")

class SoundSystem:
    def on(self):
        print("Sound system is on")

    def off(self):
        print("Sound system is off")

    def set_volume(self, volume):
        print(f"Sound system volume set to {volume}")

class DVDPlayer:
    def on(self):
        print("DVD player is on")

    def off(self):
        print("DVD player is off")

    def play(self, movie):
        print(f"Playing movie: {movie}")

# 外观类
class HomeTheaterFacade:
    def __init__(self, tv: TV, sound_system: SoundSystem, dvd_player: DVDPlayer):
        self._tv = tv
        self._sound_system = sound_system
        self._dvd_player = dvd_player

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self._tv.on()
        self._sound_system.on()
        self._sound_system.set_volume(20)
        self._dvd_player.on()
        self._dvd_player.play(movie)

    def end_movie(self):
        print("Shutting down the home theater...")
        self._tv.off()
        self._sound_system.off()
        self._dvd_player.off()

# 使用外观模式
tv = TV()
sound_system = SoundSystem()
dvd_player = DVDPlayer()

home_theater = HomeTheaterFacade(tv, sound_system, dvd_player)
home_theater.watch_movie("Inception")
home_theater.end_movie()

## 外观模式其实就是常用的综合类嘛
# main的类别 work的工作  自动化工作流的想法










class Book:
    def __init__(self):
        pass

    def design(self):
        return """
1. 依赖注入（Dependency Injection）
依赖注入是一种设计模式，通过将类的依赖项注入到类的实例中，而不是由类自行创建或管理其依赖项。这种模式促进了代码的松耦合和可测试性。

2. 生产者-消费者模式（Producer-Consumer Pattern）
前面已经介绍过，该模式解决了生产者和消费者之间的同步问题，常用于多线程环境下的数据共享和同步。

3. 发布-订阅模式（Publish-Subscribe Pattern）
发布-订阅模式允许发送者（发布者）和接收者（订阅者）之间的松耦合，发布者发布消息，订阅者订阅消息，消息通过消息通道传递。常用于事件驱动系统和消息队列系统。

4. 资源池模式（Object Pool Pattern）
资源池模式管理一个对象池，这些对象可以被重复使用，而不是每次都重新创建和销毁。这种模式适用于管理连接池、线程池、内存池等。

4. 黑板模式（Blackboard Pattern）
黑板模式用于解决复杂问题，涉及多个专家系统或知识源。所有组件都通过一个共享的黑板进行通信和协作。
"""





## 备忘录模式


```python

# @title 备忘录模式
#@markdown Please enter your details below:
# 主要用于实现状态回滚功能,回滚操作
class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state

    def set_state(self, state: str):
        self._state = state

class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state

    def create_memento(self) -> Memento:
        return Memento(self._state)

    def set_memento(self, memento: Memento):
        self._state = memento.get_state()

class Caretaker:
    def __init__(self):
        self._memento = None

    def save(self, memento: Memento):
        self._memento = memento

    def retrieve(self) -> Memento:
        return self._memento

# 客户端代码
if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker()

    # 设置和保存状态
    originator.set_state("State 1")
    print(f"Current State: {originator.get_state()}")
    caretaker.save(originator.create_memento())

    # 修改状态
    originator.set_state("State 2")
    print(f"Current State: {originator.get_state()}")

    # 恢复到先前的状态
    originator.set_memento(caretaker.retrieve())
    print(f"Restored State: {originator.get_state()}")

```




### 享元模式




```python
## 享元模式
享元模式（Flyweight Pattern）是一种结构型设计模式，它通过共享细粒度对象来减少内存消耗并提高性能。享元模式特别适用于大量相似对象的场景，它通过共享相同的对象来减少重复实例的数量，从而节省内存。

class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        # 在给定位置绘制树
        print(f"Drawing tree '{self.name}' of color '{self.color}' with texture '{self.texture}' at ({x}, {y})")

class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]

class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas):
        self.tree_type.draw(canvas, self.x, self.y)

class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)

# 使用享元模式
forest = Forest()
forest.plant_tree(1, 1, "Oak", "Green", "Rough")
forest.plant_tree(2, 3, "Pine", "Green", "Smooth")
forest.plant_tree(4, 5, "Oak", "Green", "Rough")  # 共享已有的树种类

forest.draw("Canvas")

# 单例模式的加强版
#共享一部分内容 而平移另一部分内容
# 有点像图章,制作好了一个图章以后, 就可以到处印了
# 如果想要新的图章,就定义新图章

```



```
桥接模式






```python

## 桥接模式

from abc import ABC, abstractmethod

# Implementor 接口
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

# Concrete Implementor A
class RedColor(Color):
    def fill(self):
        return "Filling with red color"

# Concrete Implementor B
class GreenColor(Color):
    def fill(self):
        return "Filling with green color"

# Abstraction 类
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

# Refined Abstraction A
class Circle(Shape):
    def draw(self):
        return f"Circle drawn. {self.color.fill()}"

# Refined Abstraction B
class Square(Shape):
    def draw(self):
        return f"Square drawn. {self.color.fill()}"

# 使用桥接模式
red = RedColor()
green = GreenColor()

circle = Circle(red)
square = Square(green)

print(circle.draw())
print(square.draw())
# 桥接模式通过组合关系（而非继承关系）来连接抽象和实现，从而实现更灵活的代码结构。

# 就要像你绘制好一幅地图,然后一个一个往前搭建
# 就好像枪械与配件一样, 我们定义枪的抽象,但是告诉你枪旁边的配件曹的尺寸,这样,你的配件就可以适应所有类型的枪,而不用管枪是谁生产的,同时,一把枪也可以适配大量的配件,而不用考虑配件是谁产的,什么性能
# 类似于现在的type-c 协议 http协议一样



```

原型模式

wod

---


```
```python

## 原型模式

通过复制现有对象的实例来创建新的对象，而不是通过类实例化。原型模式使得创建对象更加灵活，可以快速生成对象并避免子类化。它通常通过实现一个原型接口或抽象类，包含一个用于克隆对象的方法。

import copy

# 原型接口
class Shape:
    def __init__(self, id):
        self.id = id

    def clone(self):
        return copy.deepcopy(self)

# 具体原型
class Circle(Shape):
    def __init__(self, id, radius):
        super().__init__(id)
        self.radius = radius

    def __str__(self):
        return f"Circle [ID={self.id}, Radius={self.radius}]"

class Rectangle(Shape):
    def __init__(self, id, width, height):
        super().__init__(id)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle [ID={self.id}, Width={self.width}, Height={self.height}]"

# 客户端代码
circle1 = Circle("1", 10)
print(circle1)  # 输出: Circle [ID=1, Radius=10]

circle2 = circle1.clone()
circle2.id = "2"
circle2.radius = 20
print(circle2)  # 输出: Circle [ID=2, Radius=20]

rectangle1 = Rectangle("1", 30, 40)
print(rectangle1)  # 输出: Rectangle [ID=1, Width=30, Height=40]

rectangle2 = rectangle1.clone()
rectangle2.id = "2"
rectangle2.width = 50
rectangle2.height = 60
print(rectangle2)  # 输出: Rectangle [ID=2, Width=50, Height=60]


对象的创建成本较高：
当创建对象的成本较高时（例如涉及复杂的初始化过程），通过克隆现有对象可以提高性能。
系统需要独立于其产品类的实例化：
当系统需要独立于其产品类的实例化时，原型模式通过克隆对象可以实现这一点。
对象的结构复杂，且希望避免重复创建复杂对象的结构：
通过克隆现有对象，可以避免重复创建复杂对象的结构。
需要生成对象的不同状态或组合：
当需要生成不同状态或组合的对象时，原型模式可以快速生成这些对象，而不必通过构造函数重新创建。


原型模式就是deepcopy



```

代理模式




```python

## 代理模式
代理模式的分类
远程代理（Remote Proxy）：控制对远程对象的访问。
虚拟代理（Virtual Proxy）：控制对资源消耗大的对象的访问，可以延迟对象的创建。
保护代理（Protection Proxy）：控制对原始对象的访问权限。
智能代理（Smart Proxy）：在访问对象时执行一些附加操作，例如记录访问日志、引用计数等。



from abc import ABC, abstractmethod

# 抽象主题
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# 真实主题
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")

# 代理
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()




# 使用代理模式
proxy_image = ProxyImage("test_image.jpg")


# 其实就是延迟加载的逻辑
proxy_image.display()

proxy_image.display()

```


访问者模式


```python



#@title 访问者模式（Visitor）
访问者模式表示一个作用于某对象结构中的各元素的操作，它使你可以在不改变各元素的类的前提下定义作用于这些元素的新操作。


from abc import ABC, abstractmethod
from typing import List

# 访问者接口
class Visitor(ABC):
    @abstractmethod
    def visit_file(self, file: 'File'):
        pass

    @abstractmethod
    def visit_directory(self, directory: 'Directory'):
        pass

# 具体访问者：计算文件系统的总大小
class SizeVisitor(Visitor):
    def __init__(self):
        self.total_size = 0

    def visit_file(self, file: 'File'):
        self.total_size += file.size
        print(f"File: {file.name}, Size: {file.size}")

    def visit_directory(self, directory: 'Directory'):
        print(f"Directory: {directory.name}")
        for element in directory.elements:
            element.accept(self)

# 元素接口
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

# 具体元素：文件
class File(Element):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def accept(self, visitor: Visitor):
        visitor.visit_file(self)

# 具体元素：文件夹
class Directory(Element):
    def __init__(self, name: str):
        self.name = name
        self.elements: List[Element] = []

    def add(self, element: Element):
        self.elements.append(element)

    def accept(self, visitor: Visitor):
        visitor.visit_directory(self)

# 客户端代码
if __name__ == "__main__":
    # 创建文件和文件夹结构
    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    dir1 = Directory("dir1")
    dir1.add(file1)
    dir1.add(file2)

    file3 = File("file3.txt", 300)
    root = Directory("root")
    root.add(dir1)
    root.add(file3)

    # 使用访问者计算总大小
    size_visitor = SizeVisitor()
    root.accept(size_visitor)
    print(f"Total Size: {size_visitor.total_size}")

```

## 命令模式



```python

## 命令模式

命令模式（Command Pattern）是一种行为型设计模式，它将请求封装为对象，使得可以使用不同的请求、队列或日志来参数化其他对象。命令模式还支持撤销操作。



from abc import ABC, abstractmethod

# 命令接口
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# 接收者
class Light:
    def on(self):
        print("Light is ON")
    
    def off(self):
        print("Light is OFF")

# 具体命令 - 打开灯
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.on()

# 具体命令 - 关闭灯
class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.off()

# 调用者
class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command: Command):
        self.command = command
    
    def press_button(self):
        if self.command:
            self.command.execute()

# 客户端代码
if __name__ == "__main__":
    # 创建接收者
    light = Light()

    # 创建具体命令
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # 创建调用者
    remote = RemoteControl()

    # 设置命令并执行
    remote.set_command(light_on)
    remote.press_button()  # 输出：Light is ON

    remote.set_command(light_off)
    remote.press_button()  # 输出：Light is OFF


命令模式的优点和缺点
优点：

解耦请求发送者和接收者：请求发送者只需知道命令对象，而不需要知道接收者是谁或如何处理请求。
支持撤销和恢复操作：通过存储命令对象，可以轻松实现撤销和恢复功能。
支持命令队列：命令对象可以排队执行，使得系统可以支持请求的日志记录和事务管理。
增加新的命令容易：添加新的命令只需实现命令接口，不需要修改现有的代码。
缺点：

增加了系统的复杂性：需要额外的类来实现命令模式，可能会增加系统的复杂性。
命令对象的管理：在大型系统中，管理大量的命令对象可能会变得困难。
命令模式的应用场景
GUI开发：如菜单项和按钮的操作，通过命令模式实现可以方便地实现撤销和恢复功能。
事务系统：如数据库事务，通过命令模式实现可以方便地支持事务的提交和回滚。
任务队列：如任务调度系统，通过命令模式可以将任务对象放入队列中，并按顺序执行。
日志和审计：通过命令模式，可以记录所有操作，以便于审计和回放。
通过命令模式，可以将请求的发送者和接收者解耦，使得系统更加灵活和可扩展。命令模式特别适用于需要支持撤销、恢复和事务管理的系统。

```












###########################
###############

观察者

```python

# @title 观察者模式（Observer）

#@markdown 其实就是监听跟随

from abc import ABC, abstractmethod
from typing import List

# 主题接口
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: 'Observer'):
        pass

    @abstractmethod
    def detach(self, observer: 'Observer'):
        pass

    @abstractmethod
    def notify(self):
        pass

# 具体主题
class WeatherData(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature: float = 0.0

    def attach(self, observer: 'Observer'):
        self._observers.append(observer)

    def detach(self, observer: 'Observer'):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float):
        print(f"WeatherData: setting temperature to {temperature}")
        self._temperature = temperature
        self.notify()

# 观察者接口
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass

# 具体观察者
class TemperatureDisplay(Observer):
    def __init__(self, name: str):
        self._name = name
        self._temperature = 0.0

    def update(self, temperature: float):
        self._temperature = temperature
        print(f"{self._name} Display: temperature updated to {self._temperature}")

# 客户端代码
if __name__ == "__main__":
    weather_data = WeatherData()
    print('################')
    temp_display1 = TemperatureDisplay("Main")
    temp_display2 = TemperatureDisplay("Secondary")
    print('################')
    weather_data.attach(temp_display1)
    weather_data.attach(temp_display2)
    print('################')
    weather_data.set_temperature(25.0)
    weather_data.set_temperature(30.0)
    print('################')
    weather_data.detach(temp_display1)
    weather_data.set_temperature(35.0)




```


建造者模式


```python

## 建造者模式

目的是将构建过程与表示分开

# 产品
class House:
    def __init__(self):
        self.foundation = None
        self.structure = None
        self.roof = None
        self.interior = None

    def __str__(self):
        return f"House with {self.foundation}, {self.structure}, {self.roof}, and {self.interior}"

# 生成器接口
class HouseBuilder:
    def build_foundation(self):
        pass

    def build_structure(self):
        pass

    def build_roof(self):
        pass

    def build_interior(self):
        pass

    def get_house(self):
        pass

# 具体生成器
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        self.house.foundation = "Concrete foundation"

    def build_structure(self):
        self.house.structure = "Wood and brick structure"

    def build_roof(self):
        self.house.roof = "Shingle roof"

    def build_interior(self):
        self.house.interior = "Modern interior"

    def get_house(self):
        return self.house

# 指挥者
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_foundation()
        self.builder.build_structure()
        self.builder.build_roof()
        self.builder.build_interior()
        return self.builder.get_house()

# 客户端代码
builder = ConcreteHouseBuilder()
director = Director(builder)
house = director.construct_house()
print(house)  # 输出: House with Concrete foundation, Wood and brick structure, Shingle roof, and Modern interior


特别适合流程, 工作流




```


解释器



```python

## 解释器模式（Interpreter）

解释器模式为一种语言定义一个解释器，该解释器使用一系列的表达式来表示文法规则。每种表达式都实现了一个解释操作。


from abc import ABC, abstractmethod

# 上下文类，存储变量的值
class Context:
    def __init__(self):
        self.data = {}
    
    def set(self, variable, value):
        self.data[variable] = value
    
    def get(self, variable):
        return self.data.get(variable)

# 抽象表达式类
class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Context):
        pass

# 终结符表达式：表示变量
class VariableExpression(Expression):
    def __init__(self, name):
        self.name = name
    
    def interpret(self, context: Context):
        return context.get(self.name)

# 终结符表达式：表示数字
class NumberExpression(Expression):
    def __init__(self, number):
        self.number = number
    
    def interpret(self, context: Context):
        return self.number

# 非终结符表达式：加法表达式
class AddExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context):
        return self.left.interpret(context) + self.right.interpret(context)

# 非终结符表达式：减法表达式
class SubtractExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context):
        return self.left.interpret(context) - self.right.interpret(context)

# 客户端代码
if __name__ == "__main__":
    # 创建上下文并设置变量的值
    context = Context()
    context.set("x", 10)
    context.set("y", 20)

    # 创建表达式
    expression = AddExpression(
        SubtractExpression(
            NumberExpression(5),
            VariableExpression("x")
        ),
        VariableExpression("y")
    )

    # 解释并计算表达式的值
    result = expression.interpret(context)
    print(f"Result of the expression: {result}")  # 输出：Result of the expression: 15


解释器模式的应用场景
编译器：编译器中的语法解析器使用解释器模式来解析和解释代码。
脚本语言：解释脚本语言，如正则表达式解析器、SQL解析器等。
配置文件解析：解析和评估简单的配置文件或命令行参数。
机器人指令解释：机器人或自动化系统中的命令解释和执行。

没太懂

```


## 责任链



```python
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class InfoHandler(Handler):
    def handle(self, request):
        if request == "INFO":
            print("InfoHandler: Handling INFO level request")
        else:
            super().handle(request)

class DebugHandler(Handler):
    def handle(self, request):
        if request == "DEBUG":
            print("DebugHandler: Handling DEBUG level request")
        else:
            super().handle(request)

class ErrorHandler(Handler):
    def handle(self, request):
        if request == "ERROR":
            print("ErrorHandler: Handling ERROR level request")
        else:
            super().handle(request)

# 客户端代码
if __name__ == "__main__":
    # 创建具体处理者
    info_handler = InfoHandler()
    debug_handler = DebugHandler()
    error_handler = ErrorHandler()

    # 设置处理链
    info_handler.set_next(debug_handler).set_next(error_handler)

    # 提交请求
    requests = ["INFO", "DEBUG", "ERROR", "UNKNOWN"]
    for req in requests:
        print(f"Client: Submitting {req} request")
        info_handler.handle(req)
        print()


```

OA 审批流程,权限验证





```python



## 中介者模式（Mediator）

简单来说就是群聊, 广播

from abc import ABC, abstractmethod

# 中介者接口
class Mediator(ABC):
    @abstractmethod
    def send(self, message: str, colleague: 'Colleague'):
        pass

# 具体中介者
class ConcreteMediator(Mediator):
    def __init__(self):
        self._colleagues = []

    def add_colleague(self, colleague: 'Colleague'):
        self._colleagues.append(colleague)
        colleague.set_mediator(self)

    def send(self, message: str, colleague: 'Colleague'):
        for c in self._colleagues:
            if c != colleague:
                c.receive(message)

# 同事对象接口
class Colleague(ABC):
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator: Mediator):
        self._mediator = mediator

    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self, message: str):
        pass

# 具体同事对象
class ConcreteColleague(Colleague):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def send(self, message: str):
        print(f"{self._name} sends message: {message}")
        self._mediator.send(message, self)

    def receive(self, message: str):
        print(f"{self._name} receives message: {message}")

# 客户端代码
if __name__ == "__main__":
    # 创建中介者
    mediator = ConcreteMediator()

    # 创建同事对象
    colleague1 = ConcreteColleague("User1")
    colleague2 = ConcreteColleague("User2")
    colleague3 = ConcreteColleague("User3")

    # 将同事对象添加到中介者
    mediator.add_colleague(colleague1)
    mediator.add_colleague(colleague2)
    mediator.add_colleague(colleague3)

    # 发送消息
    colleague1.send("Hello everyone!")


```



```python





#@title 状态模式（State）
#状态模式允许对象在其内部状态发生改变时改变其行为，对象看起来好像修改了它的类。状态模式将状态转换行为封装到不同的状态类中，使得状态的切换更加灵活和可扩展。
#应用场景：状态机、游戏中的对象状态变化、工作流引擎等。
#开关灯的场景状态等,米家工作流.

from abc import ABC, abstractmethod

# 抽象状态
class State(ABC):
    @abstractmethod
    def handle(self, context: 'Context'):
        pass

# 具体状态：灯打开
class OnState(State):
    def handle(self, context: 'Context'):
        print("Light is already on. Turning it off.")
        context.set_state(OffState())

# 具体状态：灯关闭
class OffState(State):
    def handle(self, context: 'Context'):
        print("Light is off. Turning it on.")
        context.set_state(OnState())

# 上下文
class Context:
    def __init__(self, state: State):
        self._state = state

    def request(self):
        self._state.handle(self)

    def set_state(self, state: State):
        self._state = state

# 客户端代码
if __name__ == "__main__":
    # 创建上下文和初始状态
    context = Context(OffState())

    # 改变状态
    context.request()
    context.request()
    context.request()




# @title 策略模式（Strategy）
策略模式定义一系列算法，并将每个算法封装起来，使它们可以相互替换。策略模式使得算法可以在不影响客户端的情况下发生变化。

应用场景：排序算法、加密算法、日志策略等。
策略模式做的情况是,可以在不需要关闭服务的情况下,动态的变换策略
和工厂模式有点像

from abc import ABC, abstractmethod
from typing import List

# 策略接口
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass

# 具体策略：快速排序
class QuickSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        print("Using QuickSort")
        return sorted(data)  # 这里使用Python内置排序作为简化的快速排序实现

# 具体策略：插入排序
class InsertionSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        print("Using InsertionSort")
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

# 上下文
class SortContext:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data: List[int]) -> List[int]:
        return self._strategy.sort(data)

# 客户端代码
if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]

    context = SortContext(QuickSortStrategy())
    print(context.sort(data))

    context.set_strategy(InsertionSortStrategy())
    print(context.sort(data))




#@title 模板方法模式（Template Method）
模板方法模式在一个方法中定义了算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以在不改变算法结构的情况下，重新定义算法的某些步骤。

应用场景：算法框架、工作流程、游戏开发中的AI行为等。

#### 就是标准的抽象类思想

from abc import ABC, abstractmethod

# 抽象类
class DataProcessor(ABC):
    def process_data(self):
        self.read_data()
        self.process()
        self.save_data()

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def process(self):
        pass

    def save_data(self):
        print("Saving processed data.")

# 具体类
class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from a CSV file.")

    def process(self):
        print("Processing data from a CSV file.")

class JSONDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from a JSON file.")

    def process(self):
        print("Processing data from a JSON file.")

# 客户端代码
if __name__ == "__main__":
    csv_processor = CSVDataProcessor()
    csv_processor.process_data()

    json_processor = JSONDataProcessor()
    json_processor.process_data()




```

