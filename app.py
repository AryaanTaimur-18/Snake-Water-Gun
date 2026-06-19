from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

Choices = {"S": 1, "W": -1, "G": 0}
revChoices = {1: "S", -1: "W", 0: "G"}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():

    choice = request.json["choice"]

    you = Choices[choice]
    comp = random.choice([-1, 0, 1])

    if you == comp:
        result = "draw"

    elif (
        (you == 1 and comp == -1)
        or (you == 0 and comp == 1)
        or (you == -1 and comp == 0)
    ):
        result = "win"
    else:
        result = "lose"

    return jsonify({
        "comp": revChoices[comp],
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)