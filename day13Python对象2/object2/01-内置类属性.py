"""__author__ = 余婷"""
class Color:
    """颜色类"""
    red = (255, 0 , 0)
"""
内置类属性：python中每个类都拥有内置的类属性
__name__
__doc__
__dict__
__module__
__bases__
"""
class Animal:
    """动物类"""
    pass


class Cat(Animal):

    """说明文档:猫类"""
    number = 0


    def __init__(self, name='', color=''):
        self.name = name
        self.color = color

    def run(self):
        print('%s在跑' % self.name)

    @staticmethod
    def shout():
        print('喵~')

    @classmethod
    def get_number(cls):
        print('猫的数量:%d' % cls.number)


if __name__ == '__main__':
    cat1 = Cat('小花', 'white')

    """
    1.类.__name__
    获取类的名字(字符串)
    """
    print(Cat.__name__)

    """
    2.类.__doc__
    获取类的说明文档
    """
    print(Cat.__doc__)
    print(list.__doc__)

    """
    3.类.__dict__  获取类中所有的类属性和对应的值，以键值对的形式存到字典中
      对象.__dict__ 将对象的属性和对应的值，转换成字典的元素（常用,记住）
    """
    print(Cat.__dict__)
    print(cat1.__dict__)

    """
    4.类.__module__: 获取当前类所在的模块的名字
    
    """
    print(Cat.__module__)
    print(Color.__module__)

    """
    5.类.__bases__: 获取当前类的父类
    """
    print(Cat.__bases__)


