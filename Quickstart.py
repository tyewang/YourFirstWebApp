from flask import Flask
import random
import os
app = Flask(__name__)

file = open('demonyms.txt', 'r')
demonyms = file.read().split('\n')
file.close()

file = open('dishes.txt', 'r')
dishes = file.read().split('\n')
file.close()

file = open('ingredients.txt', 'r')
ingredients = file.read().split('\n')
file.close()

@app.route('/')
def display():
    dish = random.choice(dishes)
    demonym = random.choice(demonyms)
    ingredient = random.choice(ingredients)
    return "It's like " + dish + " except " + demonym + " and with more " + ingredient + "!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
