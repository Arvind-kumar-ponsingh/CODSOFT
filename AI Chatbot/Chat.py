import random
import json
import pickle
from keras.models import load_model
from chatbot import predict_class, get_response

with open('intents.json', 'r') as file:
    intents = json.load(file)

def chatbot_response(user_input):
    ints = predict_class(user_input)
    
    return get_response(ints, intents)


print("The Bot is running!")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bye!")
        break
    response = chatbot_response(user_input)
    print("Mila:", response)
