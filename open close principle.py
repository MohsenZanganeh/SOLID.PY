# be open for extention and be close for editing
# The Abbreviation open close principle is OCP 

class userRepository1:
    def __init__(self):
        self.model = 'userModel' # this is an example
        self.entries = []
        self.count = 0
    
    def insert(self,data):
        pass
    
    def update(self,data):
        pass
    
    def delete(self,data):
        pass

    def get_by_name(self,name):
        self.model.query( name = name )
        # 2 days later
        # for example yo want to add another parameter to your
        # function, for example ( age )
        self.model.query( name = name, age = age)
    # this doesn't obey the open close principle


# we must create another method to get the age parameter
class userRepository2:
    def __init__(self):
        self.model = 'userModel' # this is an example
        self.entries = []
        self.count = 0
    
    def insert(self,data):
        pass
    
    def update(self,data):
        pass
    
    def delete(self,data):
        pass

    def get_by_name(self,name):
        self.model.query( name = name )

    def get_by_age(self,age):
        self.model.query(age = age)

    def get_by_name_and_age(self,name,age):
        self.model.query(name = name , age = age)

    # this obeys the open close principle So this is the currect way of creating methods

    # BUT THERE IS A BIG PROBLEM OO
    #                            \/
    #
    # This way obeys the open close principle
    #  ****      BUT IS NOT SCALABLE     **** 

    # what we can do????????????? 🤔🤔🤔
    # So create a method that be scalable and obey the open close principle, This is the answer
    # 
    # So go to create, why you are wait for me.
    # 🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶🚶
    # .........................................

    # i am joking

    # this is the way  \/ \/ \/ \/

class userRepository3:
    def __init__(self):
        self.model = 'userModel' # this is an example
        self.entries = []
        self.count = 0
    
    def insert(self,data):
        pass
    
    def update(self,data):
        pass
    
    def delete(self,data):
        pass

    def get_by_query(self,**query):

        # if you define get_by_query(name='mohsen', age= 20)
        # (query without stars) will get you a dictionary 
        # like this ( {'name':'mohsen', 'age':20} ) but if 
        # you use the query like this
        # (**query by stars) that gives you parameters like 
        # this (name = 'mohsen' , age = 20)
        
        self.model.query(**query)
        # slf.model.query(name='mohsen',age=20)

    # this is an example for scaling class, 
    # i don't know your problem in scaling,
    # because your problem is deferent and
    # and i didn't face that, you must try
    # to recognizing how you can fix the 
    # scaling problem and that obeys the 
    # open close principle.