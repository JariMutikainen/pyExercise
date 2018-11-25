# Learning to define two classes: a base class and another class inheriting
# stuff from the base class.

class Character:

    def __init__(self, name, hp, level):
        self.name = name # The name of a role play character
        self.hp = hp     # The health of a role play character
        self.level = level # The skill level of a role play character

    def __repr__(self):
        s1 = f'{self.name} has {self.hp} hit points and a skill level' 
        s2 = f' of {self.level}.'
        return s1 + s2

# Non-Player Character (= NPC) inherits everything from the base class 
# 'Character'.
class NPC(Character): 
    pass





# Testing
c1 = Character('Spider man', 100, 9)
c2 = Character('Incredible Hulk', 200, 8)
print(c1)
print(c2)
