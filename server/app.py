#!/usr/bin/env python3

from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    # Print the parameter to the console
    print(parameter)
    # Return the parameter as plain text
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    # Generate a string with numbers from 0 to parameter - 1, each on a new line
    count_string = '\n'.join(str(i) for i in range(parameter)) + '\n'  # Add a trailing newline
    return count_string

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Cannot divide by zero', 400  # Handle division by zero
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400  # Handle invalid operations

    return str(result)  # Return the result as a string

if __name__ == '__main__':
    app.run(port=5555, debug=True)
