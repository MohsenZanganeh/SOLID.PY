
# SUBCLASSES SHOULD BEHAVE NICELY WHEN USED IN PLACE OF THEIR BASE CLASS
# in other WORDS when we use of subclasses we should be 
# accessible to the properties of Parents and use them
# in order that we use of subclasses insted of the Parent

# The Abbreviation Liskov Substitution principle is LCP

# assume we have a class Android 
# and has | brand , name, camera | properties

class Android():
    def __init__(self,brand,name,camera):
        self.brand = brand
        self.name = name
        self.camera = camera
    
    def __str__(self):
        return f'{self.name} is from {self.brand}, the camera is {self.camera}Mp, the Os is ANDROID'

class IOS(Android):
    def __init__(self,brand,name,camera):
        super().__init__(brand,name,camera)

# we want to create some instances of Android phon
android_1 = Android('Samsung','A30s',16)
android_2 = Android('Sony','Xperia PRO 5G',64)
android_3 = Android('Xiaomi ','Redmi Note 10 Pro',16)

print(android_1)
# A30s is from Samsung, the camera is 16Mp, the Os is ANDROID
 
print(android_2)
# Xperia PRO 5G is from Sony, the camera is 64Mp, the Os is ANDROID
 
print(android_3)
# Redmi Note 10 Pro is from Xiaomi , the camera is 16Mp, the Os is ANDROID


# And now we want to create a instance of IOS Phon

ios_1 = IOS('Apple','13 Promax',64)
print(ios_1)
# 13 Promax is from Apple, the camera is 64Mp, the Os is ANDROID

# The Os of apple phons are Android ??🤔🤔
# I don't think so 🤨

# so we must change the behavior of IOS class
# so for doing this we must create a new class

class IOS(Android):
    def __init__(self,brand,name,camera):
        super().__init__(brand,name,camera)

    def __str__(self):
        return f'{self.name} is from {self.brand}, the camera is {self.camera}Mp, the Os is IOS'


ios_2 = IOS('Apple','13 Promax',64)
print(ios_2)

# congratulation, the os of apple phons are IOS, BUT
# you didn't obey the Liskov Substitution principle
# the __str__ function was for The parent of IOS
# and you can use IOS insted of the parent

# the liskov says your class should be able
# to be used insted of its parrent, but now you can't
# for example we want to create a Android phon with IOS_2

android_4 = IOS('Samsung','A31s',16)
print(android_4)
# A31s is from Samsung, the camera is 16Mp, the Os is IOS

# the sumsung phon is IOS, NO. so we can't create a android phon
# with IOS, but our class should be able. because subclass should
# be able to behave like its parent and some more, but they
# mustn't change the behavior of their parent, they must be
# like a extention not more

# if we want to obey this principle we must create 
# new class that be our parent

class Phon():
    def __init__(self,brand,name,camera,OS):
        self.brand = brand
        self.name = name
        self.camera = camera
        self.OS = OS
    
    def __str__(self):
        return f'{self.name} is from {self.brand}, the camera is {self.camera}Mp, the Os is {self.OS}'
# it is very meaningful to create a Phon class
# that be parent of Android and IOS phons
# if our classes be irrelevant to each other
# or doesn't be meaningful, we will make mistake
# in creating structure of our project

class Android(Phon):
    def __init__(self,brand,name,camera):
        super().__init__(brand,name,camera,"ANDROID")

android_5 = Android('Samsung','A70s',64)
 
print(android_5)
# A70s is from Samsung, the camera is 64Mp, the Os is ANDROID
class IOS(Phon):
    def __init__(self,brand,name,camera):
        super().__init__(brand,name,camera,"IOS")


ios_3 = IOS('Apple','13 Promax',64)
 
print(ios_3)
# 13 Promax is from Apple, the camera is 64Mp, the Os is IOS

# Now we have
# Phon Class
#      Android Class
#      IOS     Class
# now we are obeying of Liskov Principle
# because subclasses don't change their parent behavior.
# so subclasses have their parent abilities as well their abilities

# oooo their parents are very arrogant he does not want to change his behavior
