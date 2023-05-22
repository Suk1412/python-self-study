 ###名词解释
 #####函数
>是一段执行某个特定任务的可重复使用的代码块。Python 中的函数可以通过 def 关键字定义，并且可以被传递给其他函数或赋值给变量。
>```python
>def add_numbers(x, y):
>    return x + y
>
>result = add_numbers(3, 4)
>print(result) # 输出 7
>```
 #####生成器函数
>生成器函数是一种特殊类型的函数，它可以返回一个生成器对象，该对象可以按需生成一系列值
>```python
>def my_range(n):
>    i = 0
>    while i < n:
>        yield i
>        i += 1
>
>for i in my_range(5):
>    print(i) # 输出 0, 1, 2, 3, 4
>```
 #####方法
>方法是与对象关联的函数。在 Python 中，方法是通过将对象作为第一个参数来调用的函数，该参数通常称为 self。
>```python
>class MyClass:
>    def say_hello(self):
>        print("Hello")
>
>obj = MyClass()
>obj.say_hello()
>```
 #####类
>类是一个包含属性和方法的命名空间，它允许您创建具有相似行为的对象。
>```python
>class Person:
>    def __init__(self, name, age):
>        self.name = name
>        self.age = age
>
>    def say_hello(self):
>        print("Hello, my name is", self.name)
>
>person = Person("Alice", 25)
>person.say_hello() # 输出 Hello, my name is Alice
>```
 #####类方法
>类方法（Class Method）是指在一个类中定义的方法，可以直接通过类名调用，而不需要实例化一个对象。类方法通常被用来处理与整个类相关的操作，而不是针对类的单独实例进行操作。
>在Python中，类方法使用@classmethod装饰器来声明，在方法的第一个参数中一般命名为cls，表示该方法所属的类。
>```python
>class MyClass:
>   @classmethod
>   def my_class_method(cls, arg1, arg2):
>       pass
>
>MyClass.my_class_method(arg1, arg2)
>```
>
###遍历对象
>序列类型（list、tuple、range、str等）：它们支持索引和切片操作，并且元素按照添加顺序排序。
>
>集合类型（set、frozenset、dict的keys()等）：它们不支持索引和切片操作，而是通过迭代器返回元素。其中字典的keys()方法返回的是一个集合类型。
>
>generator类型（生成器）：它们由yield语句生成，在每次迭代时返回一个值。generator本身也是可迭代对象，因此可以嵌套使用yield语句来实现复杂的迭代逻辑。
>
>还有一些内置函数和模块也可以被视为可迭代对象，例如zip、map、filter、re模块的search和finditer方法等