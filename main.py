import sys
import random
from Jokes import *
import userData
from FunFacts import *
import time
import datetime

today = datetime.datetime.now()
print(today)


def error_m():
    print("I couldn't understand that. Sorry :[")


def end():
    print("Good bye " + user)


# functions
def greeting():
    if 12 > today.strftime("%H") >= 3:
        print("Good morning!")
    elif 21 > today.strftime("%H") >= 12:
        print("Good afternoon!")
    elif today.strftime("%H") >= 21:
        print("Good evening!")
    else:
        print("Time to sleep!")
    return input()

# more input message to features


def input():
    a = raw_input(">> ")
    if a == "Hi" or a == "hi":
        return greeting()
    elif a == "Jokes" or a == "jokes":
        print(random.choice(Jokes['dark_jokes'])) # output = lorem ipsum? connect with jokes plz
        return input()
    elif a == "Fun facts" or a == "fun facts":
        print(random.choice(FunFacts))
        return input()
    elif a == "Bye" or a == "bye":
        return end()
    else:
        error_m()
        return input()


def features():
    time.sleep(1.0)
    print("Hey " + user + "! Here are some options that you can ask me. Try the command below! ;]")
    time.sleep(1.0)
    list = ["Jokes, Fun facts, Hi, Bye"]
    print(list)
    return input()


def user_name():
    global user
    user = raw_input("My name is... >> ")
    time.sleep(1.0)
    print("Hi " + user + " I am your personal assistant chat bot!")
    return features()


class Chatbot:
    def sayHello(self):
        print("Hello My name is Sunny :]")
        time.sleep(1.5)
        print("What should I call you?")
        user_name()


chatbot = Chatbot()
chatbot.sayHello()


# print(random.choice(Jokes['dark_jokes']))
# print(random.choice(FunFacts))