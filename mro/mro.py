# This is a study of MRO = 'Method Resolution Order' associated with
# the classes and multiple inheritance in the Object Oriented Programming.

# Define the class Father with recessive traits
class Father:
    
    def __init__(self):
        self.eye_color = 'blue'
        self.hair_color = 'blond'
        self.hair_type = 'straight'

    def __repr__(self):
        s = 'The eyes are {}. '.format(self.eye_color)
        s += 'The hair is {} and {}.'.format(self.hair_color,self.hair_type)
        return s


# Define the class Mother with dominating traits
class Mother:
    
    def __init__(self):
        self.eye_color = 'brown'
        self.hair_color = 'dark brown'
        self.hair_type = 'curly'

    def __repr__(self):
        s = 'The eyes are {}. '.format(self.eye_color)
        s += 'The hair is {} and {}.'.format(self.hair_color,self.hair_type)
        return s

# Define the class Child with the same attributes as Mother and Father
# in such a manner, that the Child inherits his/her characteristics
# from the Mother due to the fact, that Mother has the dominating
# traits.
class Child(Mother,Father):

   pass 

# Testing
m = Mother()
print("Mother's characteristics: ", m)
f = Father()
print("Father's characteristics: ", f)
c = Child()
help(Child)     # Prints the 'Method Resolution Order' of the class Child.
print("Child's characteristics: ", c)

