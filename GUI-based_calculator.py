import tkinter as tk
from tkinter import *
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("460x600")
root.resizable(0, 0)

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
    
        expression_for_eval = expression.replace("sin(", "math.sin(") \
                                         .replace("cos(", "math.cos(") \
                                         .replace("tan(", "math.tan(") \
                                         .replace("^", "**") \
                                         .replace("x", "*") \
                                         .replace("÷", "/") \
                                         .replace("−", "-")
        
        
        expression_for_eval = add_parentheses_for_sqrt(expression_for_eval)
        
        total = str(eval(expression_for_eval))  
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def add_parentheses_for_sqrt(expr):
    """Automatically add parentheses after a square root symbol if missing."""
    result = ""
    i = 0
    while i < len(expr):
        if expr[i] == "√":
            result += "math.sqrt("
            i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                result += expr[i]
                i += 1
            result += ")" 
        else:
            result += expr[i]
            i += 1
    return result

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

def trig_func_symbol(symbol):
    """Display trigonometric function symbol and append parentheses."""
    global expression
    expression += symbol + "("
    equation.set(expression)

def sqrt_symbol():
    """Display square root symbol (√)."""
    global expression
    expression += "√"
    equation.set(expression)

equation = StringVar()


entry = Entry(root, textvariable=equation, font=('arial', 20, 'bold'), bd=20, insertwidth=10, width=28, justify='right')
entry.grid(columnspan=5)

button_text = [
    '7', '8', '9', '÷', 'sin',
    '4', '5', '6', 'x', 'cos',
    '1', '2', '3', '−', 'tan',
    '0', '.', '=', '+', '√',
    '(', ')', '^', 'C', 'DEL'
]

buttons = []

row_value = 1
col_value = 0

for text in button_text:
    if text.isdigit() or text in [".", "(", ")"]:
        button = Button(root, text=text, padx=20, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda x=text: press(x))
    elif text in ["+", "−", "x", "÷"]:
        button = Button(root, text=text, padx=20, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda x=text: press(x))
    elif text == "=":
        button = Button(root, text=text, padx=20, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=equalpress)
    elif text == "√":
        button = Button(root, text=text, padx=32, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=sqrt_symbol)
    elif text == "sin":
        button = Button(root, text=text, padx=22, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda: trig_func_symbol('sin'))
    elif text == "cos":
        button = Button(root, text=text, padx=19, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda: trig_func_symbol('cos'))
    elif text == "tan":
        button = Button(root, text=text, padx=21, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda: trig_func_symbol('tan'))
    elif text == "DEL":
        button = Button(root, text=text, padx=16, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=delete_last)
    elif text == "C":
        button = Button(root, text=text, padx=18, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=clear)
    elif text == "^":
        button = Button(root, text=text, padx=20, pady=20, bd=8, font=('arial', 18, 'bold'),
                        command=lambda: press("^"))  


    button.grid(row=row_value, column=col_value)
    col_value += 1
    if col_value > 4:
        col_value = 0
        row_value += 1

root.mainloop()
