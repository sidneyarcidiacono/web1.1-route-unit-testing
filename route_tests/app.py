"""Import packages."""
from flask import Flask, request
from unit_tests.string_functions import *

app = Flask(__name__)


@app.route("/")
def index():
    """Return Hello World."""
    return "Hello, World!"


@app.route("/color_form")
def show_color_form():
    """Return form to pick favorite color."""
    return """
    <form action="/color_results" method="GET">
        <label>
            What's your favorite color?
            <input type="text" name="color">
        </label>
        <input type="submit" name="Submit!">
    </form>
    """


@app.route("/color_results")
def process_color_results():
    """Show color results to user."""
    users_favorite_color = request.args.get("color")
    return f"Wow, {users_favorite_color} is my favorite color, too!"


@app.route("/froyo")
def choose_froyo():
    """Show a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/><br/>
        What toppings do you want?
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """


@app.route("/froyo_results")
def show_froyo_results():
    """Show froyo choice results to user."""
    try:
        users_froyo_flavor = request.args.get("flavor")
        toppings = request.args.get("toppings")
        return f"You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {toppings}!"
    except (ValueError):
        return "Plase enter only letters A-Z"


@app.route("/reverse_message")
def reverse_message_form():
    """Reverse user's message."""
    return """
    <form action="/message_results" method="POST">
        What's your message?
        <input type="text" name="message">
        <input type="submit" value="Submit!">
    </form>
    """


@app.route("/message_results", methods=["POST"])
def message_results():
    """Show user reversed message."""
    message = request.form.get("message")
    reversed_message = reverse(message)
    return f"Here's your reversed message: {reversed_message}"


@app.route("/calculator")
def calculator():
    """Allow user to use calculator."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """


@app.route("/calculator_results")
def calculator_results():
    """Show user their calculator results."""
    try:
        operand1 = int(request.args.get("operand1"))
        operand2 = int(request.args.get("operand2"))
        operation = request.args.get("operation")
        if operation == "add":
            result = operand1 + operand2
        elif operation == "subtract":
            result = operand1 - operand2
        elif operation == "multiply":
            result = operand1 * operand2
        elif operation == "divide":
            result = operand1 / operand2
        return f"You chose to {operation} {operand1} and {operand2}. Your result is: {result}"
    except:
        return "Incorrect operator"


if __name__ == "__main__":
    app.run(debug=True)
