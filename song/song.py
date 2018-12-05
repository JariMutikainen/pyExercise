# Use a python generator to generate verses of a song as shown below.
# The dafault count should be 99 and the default beverage should be soda.
# kombucha_song = make_song(5, "kombucha")
# next(kombucha_song) # '5 bottles of kombucha on the wall.'
# next(kombucha_song) # '4 bottles of kombucha on the wall.'
# next(kombucha_song) # '3 bottles of kombucha on the wall.'
# next(kombucha_song) # '2 bottles of kombucha on the wall.'
# next(kombucha_song) # 'Only 1 bottle of kombucha left!'
# next(kombucha_song) # 'No more kombucha!'
# next(kombucha_song) # StopIteration
# 
# default_song = make_song()
# next(default_song) # '99 bottles of soda on the wall.'
# '''
def make_song(count=99, beverage='soda'):
    while True:
        if count > 1:
            yield '{} bottles of {} on the wall.'.format(count,beverage)
        elif count == 1:
            yield 'Only 1 bottle of {} left!'.format(beverage)
        elif count == 0:
            yield 'No more {}!'.format(beverage)
        else:
            raise StopIteration
        count -= 1


# Testing
cola_song = make_song(5, 'cola')
print(next(cola_song))
print(next(cola_song))
print(next(cola_song))
print(next(cola_song))
print(next(cola_song))
print(next(cola_song))
print(next(cola_song))
