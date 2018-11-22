# OOP exercise about using class attributes.
# Model a back yard coop of hens. Each hen is able to lay an egg.
# Keep track of how many eggs any given hen has laid, and how many eggs
# they have laid in total.


class Chicken:
    total_eggs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


# Testing
hen1 = Chicken('Minna', 'big hen')
hen2 = Chicken('Mari', 'little hen')
hen1.lay_egg()
hen1.lay_egg()
hen1.lay_egg()
hen2.lay_egg()
hen2.lay_egg()

print(f'\n{hen1.name} laid {hen1.eggs} eggs.')
print(f'{hen2.name} laid {hen2.eggs} eggs.')
print(f'In total it makes {Chicken.total_eggs} eggs.')
