import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")

# Global variable to store the expression
expression = ""

# Function to update the expression in the text entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def equal_press():
    try:
        global expression
        # Evaluate the expression and store the result
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Function to clear the expression in the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Create the text entry box for displaying the equation
equation = tk.StringVar()
entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry_field.grid(row=0, column=0, columnspan=4)

# Create the buttons for the calculator
button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1),  # Add parentheses buttons
]

# Loop to create buttons
for (text, row, col) in button_texts:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=equal_press)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=clear)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: press(t))
    
    button.grid(row=row, column=col)

# Start the main event loop
root.mainloop()
