# The Abbreviation Interface Segregation Principle is ISP

# i want to introduce this principle by an example.
# assume you have a mathematic class that has some
# function such as sum, mind,multiplication,Trigonometry
class Mathematic():
    def sum():
        pass
    def mind():
        pass
    def multiplication():
        pass
    def Trigonometry():
        pass

# on other hand you have a function with programmerCalc that
# inherited of Methematic class, but the is a problem,
# The programmerCalc just need to use of sum and mind function
# but now got multiplication and Trigonometry functions as well,
# the Interface Segregation Principle says, your classes should
# use of function that they need, not more, because the programmer
# doesn't use them and it is not necessary to see them
class programmerCalc(Mathematic):
    def sum():
        pass
    def mind():
        pass
    def multiplication(): # we don't need this function
        pass
    def Trigonometry(): # we don't need this function
        pass

# there is two way to obey Interface Segregation Principle

# we can define our class like this

class programmerCalc(Mathematic):
    def sum():
        pass
    def mind():
        pass
    def multiplication(): # we don't need this function so we can get rid of them with this way
        raise NotImplementedError('your class can not use this function')
    def Trigonometry(): # we don't need this function so we can get rid of them with this way
        raise NotImplementedError('your class can not use this function')

# But This is not the best way, in this way, you have the unnecessary functions yet

# you can define two class insted of Mathematic class
class programmerMathematic():
    def sum():
        pass
    def mind():
        pass


class otherMathematics():
    def multiplication():
        pass
    def Trigonometry(): 
        pass



class programmerCalc(programmerMathematic):
    def sum():
        pass
    def mind():
        pass

# so we defined to class that means we defined two concepts
# to use of mathematic functions.
# i think this is the best way.