"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


NOUNS = ["Hamburger", "Iphone", "Sunflower", "Lambourgini", "Hackbright"]

ADJECTIVES = ["smart", "brave", "delicious", "expensive", "cool"]

ANIMALS =["cat", "dog", "polar bear", "koala"]


@app.route('/')
def start_here():
    """Display homepage."""

    return """Hi! This is the home page. <br><br>
        <a href="/hello"><button>Click to continue</button></a>
         """


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Ask User Choice"""

    user_choice = request.args.get("play_game")
    player = request.args.get("person")

    if user_choice == "no":
        return render_template("goodbye.html", person=player)
    else:
        return render_template("game.html", noun_list=NOUNS, adj=ADJECTIVES, animals=ANIMALS)


@app.route('/madlib')
def show_madlib():
    """Renders the funny result"""

    color = request.args.get("color")
    person = request.args.get("person")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    animals = request.args.getlist("animal")

    return render_template('madlib.html', color=color, noun=noun, person=person,
                          adjective=adjective, animals=animals)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
