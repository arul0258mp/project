import tkinter as tk
from tkinter import *
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("460x600")
root.resizable(0, 0)

# Global expression variable to store the input string
expression = ""

def press(num):
    """Handles button press and updates expression."""
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    """Evaluate the final expression."""
    try:
        global expression
        total = str(eval(expression))  # Evaluate the expression using eval()
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def clear():
    """Clear the input field."""
    global expression
    expression = ""
    equation.set("")

def delete_last():
    """Delete the last character in the expression."""
    global expression
    expression = expression[:-1]
    equation.set(expression)

def sqrt():
    """Calculate square root."""
    global expression
    try:
        result = math.sqrt(float(expression))
        equation.set(result)
        expression = str(result)
    except:
        equation.set(" error ")
        expression = ""

def trig_func(func):
    """Handle trigonometric functions."""
    global expression
    try:
        result = getattr(math, func)(math.radians(float(expression)))
        equation.set(result)
        expression = str(result)
    except:
        equation.set(" error ")
        expression = ""

equation = StringVar()

# Entry box for the expression to be displayed
entry = Entry(root, textvariable=equation, font=('arial', 20, 'bold'), bd=20, insertwidth=10, width=28, justify='right')
entry.grid(columnspan=5)

# Digit buttons and other functional buttons
button_text = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '=', '+', '√ ',
    '(', ')', '^', 'C', 'DEL'
]

buttons = []

row_value = 1
col_value = 0

for text in button_text:
    if text.isdigit() or text in [".", "(", ")"]:
        button = Button(root, text=text, padx=20, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda x=text: press(x))
    elif text in ["+", "-", "*", "/"]:
        button = Button(root, text=text, padx=20, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda x=text: press(x))
    elif text == "=":
        button = Button(root, text=text, padx=20, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=equalpress)
    elif text == "√ ":
        button = Button(root, text=text, padx=29, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=sqrt)
    elif text == "sin":
        button = Button(root, text=text, padx=22, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda: trig_func('sin'))
    elif text == "cos":
        button = Button(root, text=text, padx=19, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda: trig_func('cos'))
    elif text == "tan":
        button = Button(root, text=text, padx=21, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda: trig_func('tan'))
    elif text == "DEL":
        button = Button(root, text=text, padx=16, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=delete_last)
    elif text == "C":
        button = Button(root, text=text, padx=18, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=clear)
    elif text == "^":
        button = Button(root, text=text, padx=20, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda: press("**"))  # Use Python's exponentiation operator


    button.grid(row=row_value, column=col_value)
    col_value += 1
    if col_value > 4:
        col_value = 0
        row_value += 1

root.mainloop()
