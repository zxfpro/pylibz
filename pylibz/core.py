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
    
    


class 适配器():
    """
使用效果就是直接调用老接口的对象的话对方咩有这个方法,
那么就将老接口传入一个适配器,这样,老接口就有了新方法 有点像电源适配器,或者插头转换器
## 适配器模式


    """
    def update(self,class_name):
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
    