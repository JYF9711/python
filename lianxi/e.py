class MyClass:
    i=1234
#类的定义
    def f(self):
        return 'hello world'

#实例化类
x=MyClass()

#访问类的属性

print("MyClass 类的属性i为:",x.i)
print("MyClass 类的方法f输出为:",x.f())
