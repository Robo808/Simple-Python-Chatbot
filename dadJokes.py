# We import the requests and random modules and create a function in order to use the API in our main file.

import requests
import random

def API_JOKE():

    joke_input = input("What should the topic of the joke be? (if you want to Quit type 'quit' or 'Quit'. \n")
    if joke_input == 'quit' or joke_input == 'Quit':
        return 'quit'

    # We make an API call and add our user's joke topic via the joke_input variable. We also use the headers to request the JSON file specifically as noted in the API documentation.

    initial_request = requests.get("https://icanhazdadjoke.com/search?term=" + joke_input, headers={"Accept": "application/json"})

    # We decode the JSON response and assign it to a variable.

    decoded_request = initial_request.json()

    # We count the number of jokes returned by our user's keyword. We know the list is named "results" after inspecting the JSON file.

    number_of_jokes = len(decoded_request["results"])

    # We return a random joke from the request or ask the user to enter another keyword if no joke was found.

    if number_of_jokes != 0:
        joke = random.choice(decoded_request["results"])['joke']
        return joke
    else:
        print("\nYour keyword did not return any jokes, please try again or type Quit to quit \n")
        return API_JOKE()
