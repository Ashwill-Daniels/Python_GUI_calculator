""" A basic GUI calculator build with the tkinter module."""
import tkinter as tk

# Create the GUI window.
calc_window = tk.Tk()

# Adjust the window dimensions.
calc_window.geometry("300x275")

# Shown on the window bar.
calc_window.title("Python Calculator")

# Used to hold all calculations.
calculation = ""


def add_to_calculation(symbol):
    """ Shows the appropriate value on the calculator when a button is 
     clicked.
     """
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    """ Used when the equals(=) button is clicked."""
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    """ Clears the calculator screen."""
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# The calculator screen.
text_result = tk.Text(calc_window, height = 2, width = 16, 
                      font = ("Arial", 24))
text_result.grid(columnspan = 5)

# Button 1.
btn_1 = tk.Button(calc_window, text = "1", 
                  command = lambda: add_to_calculation(1), width = 5, 
                  font = ("Arial", 14))
btn_1.grid(row = 2, column = 1)

# Button 2.
btn_2 = tk.Button(calc_window, text = "2", 
                  command = lambda: add_to_calculation(2), width = 5, 
                  font = ("Arial", 14))
btn_2.grid(row = 2, column = 2)

# Button 3.
btn_3 = tk.Button(calc_window, text = "3", 
                  command = lambda: add_to_calculation(3), width = 5, 
                  font = ("Arial", 14))
btn_3.grid(row = 2, column = 3)

# Button 4.
btn_4 = tk.Button(calc_window, text = "4", 
                  command = lambda: add_to_calculation(4), width = 5, 
                  font = ("Arial", 14))
btn_4.grid(row = 3, column = 1)

# Button 5.
btn_5 = tk.Button(calc_window, text = "5", 
                  command = lambda: add_to_calculation(5), width = 5, 
                  font = ("Arial", 14))
btn_5.grid(row = 3, column = 2)

# Button 6.
btn_6 = tk.Button(calc_window, text = "6", 
                  command = lambda: add_to_calculation(6), width = 5, 
                  font = ("Arial", 14))
btn_6.grid(row = 3, column = 3)

# Button 7.
btn_7 = tk.Button(calc_window, text = "7", 
                  command = lambda: add_to_calculation(7), width = 5, 
                  font = ("Arial", 14))
btn_7.grid(row = 4, column = 1)

# Button 8.
btn_8 = tk.Button(calc_window, text = "8", 
                  command = lambda: add_to_calculation(8), width = 5, 
                  font = ("Arial", 14))
btn_8.grid(row = 4, column = 2)

# Button 9.
btn_9 = tk.Button(calc_window, text = "9", 
                  command = lambda: add_to_calculation(9), width = 5, 
                  font = ("Arial", 14))
btn_9.grid(row = 4, column = 3)

# Button 0.
btn_0 = tk.Button(calc_window, text = "0", 
                  command = lambda: add_to_calculation(0), width = 5, 
                  font = ("Arial", 14))
btn_0.grid(row = 5, column = 2)

# Addition button.
btn_plus = tk.Button(calc_window, text = "+", 
                  command = lambda: add_to_calculation("+"), width = 5, 
                  font = ("Arial", 14))
btn_plus.grid(row = 2, column = 4)

# Minus button.
btn_minus = tk.Button(calc_window, text = "-", 
                  command = lambda: add_to_calculation("-"), width = 5, 
                  font = ("Arial", 14))
btn_minus.grid(row = 3, column = 4)

# Multiply button.
btn_multiply = tk.Button(calc_window, text = "*", 
                  command = lambda: add_to_calculation("*"), width = 5, 
                  font = ("Arial", 14))
btn_multiply.grid(row = 4, column = 4)

# Divide button.
btn_divide = tk.Button(calc_window, text = "/", 
                  command = lambda: add_to_calculation("/"), width = 5, 
                  font = ("Arial", 14))
btn_divide.grid(row = 5, column = 4)

# Equals button.
btn_equals = tk.Button(calc_window, text = "=", 
                  command = evaluate_calculation, width = 5, 
                  font = ("Arial", 14))
btn_equals.grid(row = 5, column = 3)

# Clear button.
btn_clear = tk.Button(calc_window, text = "C", 
                  command = clear_field, width = 5, 
                  font = ("Arial", 14))
btn_clear.grid(row = 5, column = 1)

# Used to keep the program running.
calc_window.mainloop()