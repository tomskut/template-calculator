from tkinter import *

def buttonclick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def buttonclear():
    global operator
    operator = ""
    input_value.set("")

def buttonEqual():
    global operator
    try:
        # Replace percentage calculations with decimal
        while '%' in operator:
            idx = operator.index('%')
            # Find the number before the %
            start_idx = idx - 1
            while start_idx >= 0 and (operator[start_idx].isdigit() or operator[start_idx] == '.'):
                start_idx -= 1
            start_idx += 1
            num = float(operator[start_idx:idx])
            decimal = num / 100
            # Replace the number% with the decimal
            operator = operator[:start_idx] + str(decimal) + operator[idx + 1:]
        
        # Replace 'x' with '*' for evaluation
        operator = operator.replace('x', '*')
        result = str(eval(operator))
        input_value.set(result)
    except Exception:
        input_value.set("Error")
    operator = ""

def buttonDelete():
    global operator
    if operator:   
        operator = operator[:-1]   
        input_value.set(operator)

def buttonComma():
    global operator
    if '.' not in operator:
        operator = operator + '.'
        input_value.set(operator)

def buttonPercentage():
    global operator
    operator = operator + '%'
    input_value.set(operator)

def buttonDivide():
    global operator
    operator = operator + '/'
    input_value.set(operator)

main = Tk()
main.title("Calculator")
operator = ""
input_value = StringVar()

# Entry display
display_text = Entry(main, font=("arial", 20, "bold"), textvariable=input_value, bd=30, insertborderwidth=4,
                    bg="Grey", justify=RIGHT)
display_text.grid(columnspan=4, sticky="nsew")

# Define button properties
button_properties = {
    'padx': 20,
    'bd': 8,
    'fg': "black",
    'font': ("arial", 20, "bold"),
}

# Row 1
Button(main, **button_properties, text="7", command=lambda: buttonclick(7)).grid(row=2, column=0, sticky="nsew")
Button(main, **button_properties, text="8", command=lambda: buttonclick(8)).grid(row=2, column=1, sticky="nsew")
Button(main, **button_properties, text="9", command=lambda: buttonclick(9)).grid(row=2, column=2, sticky="nsew")
Button(main, **button_properties, text="+", command=lambda: buttonclick("+")).grid(row=4, column=3, sticky="nsew")

# Row 2
Button(main, **button_properties, text="4", command=lambda: buttonclick(4)).grid(row=3, column=0, sticky="nsew")
Button(main, **button_properties, text="5", command=lambda: buttonclick(5)).grid(row=3, column=1, sticky="nsew")
Button(main, **button_properties, text="6", command=lambda: buttonclick(6)).grid(row=3, column=2, sticky="nsew")
Button(main, **button_properties, text="-", command=lambda: buttonclick("-")).grid(row=3, column=3, sticky="nsew")

# Row 3
Button(main, **button_properties, text="1", command=lambda: buttonclick(1)).grid(row=4, column=0, sticky="nsew")
Button(main, **button_properties, text="2", command=lambda: buttonclick(2)).grid(row=4, column=1, sticky="nsew")
Button(main, **button_properties, text="3", command=lambda: buttonclick(3)).grid(row=4, column=2, sticky="nsew")
Button(main, **button_properties, text="x", command=lambda: buttonclick("x")).grid(row=2, column=3, sticky="nsew")

# Row 4
Button(main, **button_properties, text="00", command=lambda: buttonclick(00)).grid(row=5, column=0, sticky="nsew")
Button(main, **button_properties, text="0", command=lambda: buttonclick(0)).grid(row=5, column=1, sticky="nsew")
Button(main, **button_properties, text="C", command=buttonclear).grid(row=1, column=0, sticky="nsew")
Button(main, **button_properties, text="=", command=buttonEqual).grid(row=5, column=3, sticky="nsew")
Button(main, **button_properties, text="⌫", command=buttonDelete).grid(row=1, column=2, sticky="nsew")

# Row 5 (additional row for decimal and percentage)
Button(main, **button_properties, text=".", command=buttonComma).grid(row=5, column=2, sticky="nsew")
Button(main, **button_properties, text="%", command=buttonPercentage).grid(row=1, column=1, sticky="nsew")
Button(main, **button_properties, text="÷", command=buttonDivide).grid(row=1, column=3, sticky="nsew") 

main.mainloop()