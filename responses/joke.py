# An experiment of using the requests package to access data in a remote
# server.

from random import randint
from requests import get
url = 'https://icanhazdadjoke.com/search'
my_header = {'Accept': 'application/json'}
topic = input('Enter your desired topic for a joke: ')
my_params = {'limit': 30, 'page': 1, 'term': topic}
r = get(url, headers=my_header, params=my_params)


# print(r.url)    # This shows the contents of the url sent from the client.
# print(r)        # This shows if the access to the remote server was OK.
# 2xx = OK, 3xx = Redirected,
# 4xx = Client error, 5xx = Server error
# print(r.text)   # This makes a good visual representation of the results
# print(r.json()) # json() makes a python dictionary of the results
# print(r.json()['status'])
dictionary = r.json()  # Make a python dictionary of the returned results
if dictionary['total_jokes'] == 0:
    print(f"I'm sorry, but I have no jokes about {topic}.")
elif dictionary['total_jokes'] == 1:
    print(f"I have only one joke about {topic}. Here it comes.")
    print(dictionary['results'][0]['joke'])
else:
    print(f"I have {dictionary['total_jokes']} jokes about {topic}.")
    print("This is one of them.")
    joke_list = dictionary['results']  # joke_list is a list of dicts
    # Select a random dict of the joke_list and print the value
    # corresponding to the key='joke' from it.
    print(joke_list[randint(0, len(joke_list) - 1)]['joke'])
