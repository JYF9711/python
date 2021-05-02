#定义类
class People:
    #定义最基本的属性
    name=''
    age=0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight=0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print('%s说:我 %d岁'%(self.name,self.age))

#单继承实例
class Student(People):
    gread=''
    def __init__(self,n,a,w,g):
        #继承父类的构函
        People.__init__(self,n,a,w)
        self.gread=g
    #覆盖父类的方法
    def speak(self):
        print("%s说:我%d岁了,我在读%d年级"%(self.name,self.age,self.gread))
        
#另一个类,多重继承之前的准备
# class Speaker():
#     topic=''
#     name=''
#     def __init__(self,n,t):
#         self.name=n
#         self.topic=t
#     def speak(self):
#         print("我叫%s,我是一个演说家,我讲的主题是%s"%(self.name,self.topic))
#多重继承
class Sample(Student):
    a=''
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
       # Speaker.__init__(self,n,t)
        
test=Sample("Tim",25,80,4,"python")
test.speak()
test.speak()
