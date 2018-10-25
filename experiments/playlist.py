# This program experiments making more complex data strustures in python.
play_list = []
play_list.append(
    dict(title    = "Born in the USA",
         artist   = "Bruce Springsteen",
         album    = "The best of the E-street band",
         duration = "04:35")
    )
play_list.append(
    dict(title    = "Waterloo",
         artist   = "Abba",
         album    = "The best of the ABBA",
         duration = "03:35")
    )
play_list.append(
    { 
        'title'    : 'Thunderstruck',
        'artist'   : 'AC/DC',
        'album'    : 'Australian rock',
        'duration' : '04:53'
    }
    )

for line in play_list:
    print(f"{line['title']}")
    print(f"by {line['artist']}")
    print(f"From the album: {line['album']}")
    print(f"Duration: {line['duration']}\n")

