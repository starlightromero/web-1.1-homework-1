"""Import Flask and randint."""
from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    """Shows a greeting to the user."""
    return render_template("main.html")


@app.route("/penguins", methods=["GET"])
def penguins():
    """Tell the user about penguins."""
    return render_template("penguins.html")


@app.route("/animal/<users_animal>", methods=["GET"])
def favorite_animal(users_animal):
    """Display a message to the user based on their favorite animal."""
    return f"Wow, {users_animal} is my favorite animal, too!"


@app.route("/dessert/<users_dessert>", methods=["GET"])
def favorite_dessert(users_dessert):
    """Display a message to the user based on their favorite dessert."""
    return f"How did you know I liked {users_dessert}?"


@app.route("/madlibs/<adjective>/<noun>", methods=["GET"])
def madlibs(adjective, noun):
    """Display a dynamic message to the user based on an adjective and noun."""
    return f"One day my {adjective} friend and I went to see the {noun}."


@app.route("/multiply/<number1>/<number2>", methods=["GET"])
def multiply(number1, number2):
    """Display the product of two numbers based on the user's input."""
    if number1.isdigit() and number2.isdigit():
        return f"{number1} times {number2} is {int(number1) * int(number2)}."
    return "Invalid inputs. Please try again by entering 2 numbers!"


@app.route("/sayntimes/<word>/<n>", methods=["GET"])
def sayntimes(word, n):
    """Display a word an n amout of times as specified by the user."""
    if n.isdigit():
        return f"{word} " * int(n)
    return "Invalid input. Please try again by entering a word and a number!"


@app.route("/reverse/<word>", methods=["GET"])
def reverse(word):
    """Reverse a word based on the user's input."""
    return word[::-1]


@app.route("/strangecaps/<word>", methods=["GET"])
def strangecaps(word):
    """Display a word, specifiedby the user, with stange capital letters."""
    output = ""
    for w in range(len(word)):
        if w % 2 != 0:
            output += word[w].upper()
        else:
            output += word[w].lower()
    return output


@app.route("/dicegame", methods=["GET"])
def dicegame():
    """Picks a random number between 1 and 6. If number is 6 the user wins.
    If number is not 6 the user looses."""
    num = randint(1, 6)
    result = "lost"
    if num == 6:
        result = "won"
    return render_template("dice.html", num=num, result=result)


@app.errorhandler(404)
def catch_all(error):
    """Catch all other routes. Display button allowing user to return home."""
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)
