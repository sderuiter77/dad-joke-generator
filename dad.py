import requests
from random import choice
from pyfiglet import Figlet
from termcolor import colored
from colorama import init
init() 

f = Figlet(font='big')

url = "https://icanhazdadjoke.com/search"

print(colored(f.renderText('Dad Joke 9000'),color="magenta"))

term = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
    url, headers={"Accept": "application/json"},
    params={
        "term": term
    }
).json()

num_jokes = response['total_jokes']
jokes = response['results']

if num_jokes == 0:
    print("Sorry, I don't have any jokes about this topic. Please try again")
elif num_jokes == 1:
    print(f"I've got one joke with the word {term}.") 
    print(f"Here it is: {jokes[0]['joke']}")
else:
    print(f"I've got {num_jokes} jokes with the word {term}. Here's one:") 
    print(f"{choice(jokes)['joke']}")
