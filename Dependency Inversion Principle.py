# The Abbreviation Dependency Inversion Principle is DIP

# Dependency inversion is intended to implement an interface
# to define some rules for other object that obey those rules
# i explain that more in a few moments later. but now i want
# to note something, pay attention in below. 
# \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/
# python doesn't has the abbstraction built in, and for 
# implementing abbstraction we must use of a module that
# called ABC(Abbstraction Base Class) this is just for 
# developers and to increase readability, and the python
# interperetor doesn't do any actual type checking.
# sooooo...code....

from abc import ABC, abstractmethod

# Dependency Inversion Has two properties:
# 1 - High-level modules should not depend on the low-level modules.
# Both should depend on abstractions.

# 2 - Abstractions should not depend on details. Details should 
# depend on abstractions.

# Patterns are notions and this notion can includes some class,
# or some file, or some functions, or some line of codes, or some
# related projects, etc.
# so we want to underestand them and attend them in the projects.
# i want to start with an example.

# we have a class that is Android

class Android():
    def camera(self,status='off'):
        if status == 'off':
            print('The camera is off')

        if status == 'on':
            print('The camera is on')
        
        if status == 'take_photo':
            print('The camera toke a photo')

class Person():
    def __init__(self,person: str, android: Android):
        self.person = person
        self.android = android
    def take_photo(self):
        self.android.camera('take_photo')
        print(self.person,' toke a photo')

    def on_camera(self):
        self.android.camera('on')
        print(self.person,' turned on the camera')
        
    def off_camera(self):
        self.android.camera('off')
        print(self.person,' turned off the camera')

# you can see we have a Android class that has a method
# that is camera and has three status that are ('on','off','take_photo')
# and we have a Person class that has three method that are take_photo,on_camera,off_camera
# and we want to create a person that use of his Android Phon

# lets create a person

android_1 = Android()
person_1 = Person('Sara',android_1)

person_1.on_camera()
# The camera is on
# Sara  turned on the camera

person_1.take_photo()
# The camera toke a photo
# Sara  toke a photo

person_1.off_camera()
# The camera is off
# Sara  turned off the camera

# the problem here is that the Android class is depend
# on the Person class, that's mean if we want to use of
# Android class must be use or must be there when we use of
# Person class.
# imaging Person want to use of Ios Phon, person what
# can do there???

# the dependency inversion says that invert the dependency between 
# Person class and Android class, to Android class don't be dependent,
# for example we want to use another class in init of person class, and
# there we can't because if we want to use of take_photo option we must
# use of Android class and we can't change The Android class instead of
# another class.

# what we can do in this situation.

# we must create an abstraction no insterface, somebodies
# make mistake between these words. please explore about interface.

# so lets change these classes to obey Dependency Inversion Principle

# first we must use of ABC

from abc import ABC,abstractmethod

# we was used of an Android class to define,
# camera and contact method.
# we want to add a layer to define our abstraction or our rule,
# to other classes obey of these rules, as result other classed,
# will depend on abstraction, as result detailed classes is 
# depend on abstraction



class Phon(ABC):
    @abstractmethod
    def camera():
        pass

# we define a photo class that has camera and contact method
# in abstracting structure we must create the method like these,
# because this is an abstract of some rules, we want to define rule
# for other classes, to use of the rules that they need, 
#  ----------------------------------------------------------------
#  ADVANTAGE ADVANTAGE ADVANTAGE ADVANTAGE ADVANTAGE

# \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/

# i said the advantage of abstracting at first of the 
# document but i review that >>>>>>>>>>>>>>>>>>>>
# i said these are an abstract of some rules, why we must do this,
# this is just for developers to develop their application easily,
# to pay attention to the methods that they must use.

# /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ 

print('\/ \/ \/ \/ \/  \/ \/ \/ \/ \/ Dependency Inversion Principle \/ \/ \/ \/ \/  \/ \/ \/ \/ \/')

class Android(Phon):
    def camera(self,status='off'):
        if status == 'off':
            print('The camera is off',' - class is Android')

        if status == 'on':
            print('The camera is on',' - class is Android')
        
        if status == 'take_photo':
            print('The camera toke a photo',' - class is Android')

class IOS(Phon):
    def camera(self,status='off'):
        if status == 'off':
            print('The camera is off',' - class is IOS')

        if status == 'on':
            print('The camera is on',' - class is IOS')
        
        if status == 'take_photo':
            print('The camera toke a photo',' - class is IOS')



class Person():
    def __init__(self,person: str, phon: Phon):
        self.person = person
        self.phon = phon
    def take_photo(self):
        self.phon.camera('take_photo')
        print(self.person,' toke a photo')

    def on_camera(self):
        self.phon.camera('on')
        print(self.person,' turned on the camera')
        
    def off_camera(self):
        self.phon.camera('off')
        print(self.person,' turned off the camera')


android_1 = Android()
ios_1 = IOS()


print('\n------------------------- Android Class -------------------------\n')
person_1 = Person('Sara', Android)

person_1.on_camera()
# The camera is on - class is Android
# Sara  turned on the camera

person_1.take_photo()
# The camera toke a photo - class is Android
# Sara  toke a photo

person_1.off_camera()
# The camera is off - class is Android
# Sara  turned off the camera


print('\n------------------------- IOS Class -------------------------\n')
person_2 = Person('Sara', IOS)

person_2.on_camera()
# The camera is off  - class is IOS
# Sara  turned on the camera

person_2.take_photo()
# The camera toke a photo - class is IOS
# Sara  toke a photo

person_2.off_camera()
# The camera is off - class is IOS
# Sara  turned off the camera


# Now we can use of another class instead of just Android class in
# Person Class