# class counter:
#     def __init__(self):
#         self.count = 0 
#     def increment(self):
#         self.count += 1

# a = counter() # 카운터의 초기값 0
# # 객체 생성, 객체의 참조값을 a에 저장
# b = counter(100) # 초기값 100
# a.increment() # 메소드 접근
# a.count = 100 # 변수 접근

# class Television : 
#     serialNumvber = 0 # 클래스 변수 

#     def __init__(self,channel,volume,on):
#         self.channel = channel
#         self.volume = volume
#         self.on = on # 부울형 변수
#         # 위에 3개가 인스턴스 변수 정의

#     def show(self):
#         print(self.channel,self.volume,self.on)
#     def setChannel(self,channel):
#         self.channel=channel
#     def getChannel(self):
#         return self.channel
# t = Television(9,10,True)
# t.show()
# t.setChannel(11)
# t.show()

# import math 

# class Circle:
#     def __init__(self,radius=0):
#         self.radius = radius
    
#     def getArea(self):
#         return math.pi * self.radius * self.radius

#     def getPerimeter(self):
#         return math.pi * 2 * self.radius
# c = Circle(10)
# print("원의 면적:",c.getArea())
# print("원의 둘레:",c.getPerimeter())

# class Car:
#     def __init__(self,speed,color,model):
#         self.speed = speed
#         self.color = color
#         self.model = model
#     def drive(self):
#         self.speed = 60

# myCar = Car(0,"blue","E-class")

# class Student :
#     def __init__(self,name=None,age=0):
#         self.__name = name
#         self.__age = age
#     def getAge(self):
#         return self.__age
#     def getName(self):
#         return self.__name
#     def setAge(self,age):
#         self.__age=age
#     def setName(self,name):
#         self.__name=name


# msg = "카운트값"+str(self.count)


