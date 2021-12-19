class userRepository:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def insert(self,data):
        pass
    
    def update(self,data):
        pass
    
    def delete(self,data):
        pass

    def get(self,query):
        pass

    # put method that has a another responsibility is not currect 
    # we must create another class that method be related to that 
    def hashPassword(self,password):
        pass

# this is the currect way of defining methods
class PasswordGenerator():

    def hashPassword(self,password):
        pass

    def verifyPassword(self,hash):
        pass