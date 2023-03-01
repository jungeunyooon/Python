# class Rocket:
#     def __init__(self,x=0,y=0):
#         self.x= 0
#         self.y= 0

#     def moveUp(self,y):
#         self.y = y +1 

# myRocket = Rocket()
# print("로켓의 높이:",myRocket.y)

# myRocket.moveUp
# print("로켓의 높이 :",myRocket.y)

# class Box:
#     def __init__(self,l,h,d):
#         self.length = l
#         self.height = h
#         self.depth = d
    
#     def __str__(self):
#         return "("+str(self.length)+","+str(self.height)+","+str(self.depth)+")"  

#     def getLength(self):
#         return self.length

#     def getHeight(self):
#         return self.height


#     def getDepth(self):
#         return self.depth

    
# b1 = Box(100,100,100)
# print(b1)
# print("상자의 부피는",b1.getHeight()*b1.getLength()*b1.getDepth())

# class Rectangle:
#     def __init__(self,x,y,w,h):
#         self.x = x
#         self.y = y
#         self.width = w
#         self.height = h

#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y
#     def getWidth(self,x,y):
#         self.width = x*y
#         return self.width
#     def getArea(self,w,h):
#         self.area = w*h
#         return self.area
#     def overlap(r1,r2):
#         if r1!=r2 : 
#             pass
#         else :
#             return print("r1과 r2는 서로 겹칩니다")

# r1 = Rectangle(0,0,100,100)
# r2 = Rectangle(10,10,100,100)
# r1.overlap(r2)

# class Triangle:
#     def __init__(self,angle1,angle2,angle3):
#         self.angle1=angle1
#         self.angle2=angle2
#         self.angle3=angle3
#     numberOfSides=3
#     def checkAngles(self):
#          if self.angle1+self.angle2+self.angle3 ==180:
#              return True
#          else:
#              return False

# triangle=Triangle(90,30,60)
# print(triangle.checkAngles())

# class Person():
#     def __init__(self, name,
#                  mobile=None, office=None, email=None):
#         self.name = name
#         self.mobile = mobile
#         self.office = office
#         self.email = email

#     def setMobile(self, number):
#         self.mobile = number

#     def setOffice(self, number):
#         self.office = number

#     def setEmail(self, address):
#         self.email = address
#     def __str__(self):
#         s = ''
#         s += self.name + '\n'
#         s += "office phone:"+self.office + '\n'
#         s += "email address:"+self.email + '\n'
#         return s

# class PhoneBook():
#     def __init__(self):        
#         self.contacts = {}

#     def add(self, name, mobile=None, office=None,
#             email=None):
#         p = Person(name, mobile, office, email)
#         self.contacts[name] = p
#     def __str__(self):
#         s = ''
#         for p in sorted(self.contacts):
#             s += str(self.contacts[p]) + '\n'
#         return s

# obj = PhoneBook()
# obj.add("Kim", office="1234567", email="kim@company.com")
# obj.add("Park", office="2345678", email="park@company.com")
# print(obj)

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def setX(self,x):
#         self.x = x
#     def setY(self,y):
#         self.y = y
    
#     def __str__(self,x,y):
#         s = "( "+ x + "," + y + ")" # 이게 아니라
#         return "(%d, %d)" % (self.x, self.y) # 이거야

# class Point3(Point):
#     def __init__(self,x,y,z):
#         super().__init__(x,y)
#         self.z = z
#     def __str__(self) :
#        return "(%d, %d, %d)" % (self.x, self.y, self.z)

# my_point=Point3(1,2,3)
# print(my_point)    

# import cmath 			# complex math 모듈 
# class Function:
#     def __init__(self):
#         pass
#     def value(self, x):
#         pass

# class Quadratic(Function):
#     def __init__(self, a, b, c):
#         self.a=a
#         self.b=b
#         self.c=c

#     def value(self, x):
#         return (self.a)*x**2+(self.b)*x+(self.c)
        
#     def get_roots(self):
#         d = (self.b**2) - (4*self.a*self.c)

#         sol1 = (-self.b-cmath.sqrt(d))/(2*self.a)
#         sol2 = (-self.b+cmath.sqrt(d))/(2*self.a)

#         print(f'solution: {sol1}, {sol2}')

# e = Quadratic(1, 5, 6)
# e.get_roots()

# class Animal:
#     def __init__(self, age):
#         self.age=age

#     def eat(self):
#         print("동물이 먹고 있습니다. ")


# class Cat(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(age)
#         self.name=name
#         self.breed=breed


# a = Cat("aaa", 2, "Pure")
# b = Cat("bbb", 3, "Pure")
# c = Cat("ccc", 5, "Pure")

# def get_oldest_cat(*args):
#     return max(args)

# age = get_oldest_cat(a.age, b.age, c.age)
# print(f"가장 나이가 많은 고양이는  {age} 살입니다.")


