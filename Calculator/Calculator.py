import tkinter as std

def button_click(number):
    current = display.get()
    display.delete(0, std.END)
    display.insert(std.END, current + str(number))

def button_clear():
    display.delete(0, std.END)

def button_equal():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, std.END)
        display.insert(std.END, result)
    except:
        display.delete(0, std.END)
        display.insert(std.END, "Error")

# Create the GUI window
window = std.Tk()
window.title("Calculator")

# Create the display
display = std.Entry(window, width=30)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Add padding to the display

# Define colors
button_bg = "#E0E0E0"  # Button background color (light gray)
button_fg = "#000000"  # Button text color
display_bg = "#FFFFFF"  # Display background color (white)
display_fg = "#000000"  # Display text color

# Create the number buttons with padding
button_7 = std.Button(window, text="7", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click(7))
button_8 = std.Button(window, text="8", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click(8))
button_9 = std.Button(window, text="9", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click(9))
button_4 = std.Button(window, text="4", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click(4))
button_5 = std.Button(window, text="5", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click(5))
button_6 = std.Button(window, text="6", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click(6))
button_1 = std.Button(window, text="1", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click(1))
button_2 = std.Button(window, text="2", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click(2))
button_3 = std.Button(window, text="3", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click(3))
button_0 = std.Button(window, text="0", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click(0))

# Create the operator buttons with padding
button_subtract = std.Button(window, text="-", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click("-"))
button_add = std.Button(window, text="+", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click("+"))
button_multiply = std.Button(window, text="*", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click("*"))
button_divide = std.Button(window, text="/", padx=10, pady=5, bg=button_bg, fg=button_fg, command=lambda: button_click("/"))
button_clear = std.Button(window, text="C", padx=10, pady=5, bg=button_bg, fg=button_fg, command=button_clear)
button_equal = std.Button(window, text="=", padx=10, pady=5, bg=button_bg, fg=button_fg, command=button_equal)

# Position the buttons on the grid with spacing
button_7.grid(row=1, column=0, padx=5, pady=5)
button_8.grid(row=1, column=1, padx=5, pady=5)
button_9.grid(row=1, column=2, padx=5, pady=5)
button_4.grid(row=2, column=0, padx=5, pady=5)
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6.grid(row=2, column=2, padx=5, pady=5)
button_1.grid(row=3, column=0, padx=5, pady=5)
button_2.grid(row=3, column=1, padx=5, pady=5)
button_3.grid(row=3, column=2, padx=5, pady=5)
button_0.grid(row=4, column=1, padx=5, pady=5)

button_add.grid(row=1, column=3, padx=5, pady=5)
button_subtract.grid(row=2, column=3, padx=5, pady=5)
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide.grid(row=4, column=3, padx=5, pady=5)
button_clear.grid(row=4, column=0, padx=5, pady=5)
button_equal.grid(row=4, column=2, padx=5, pady=5)

# Configure colors for display
display.configure(bg=display_bg, fg=display_fg)

# Start the GUI event loop
window.mainloop()
