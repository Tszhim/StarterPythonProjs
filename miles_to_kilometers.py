# Simple GUI test using tkinter.

from tkinter import *

# Converts miles to kilometers when button is clicked.
def convert():
    miles = float(miles_input_entry.get())
    km = miles * 1.609
    converted_label.config(text=km)


# Window setup.
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=100)

# Labels
miles_label = Label(text="miles", font=("Helvetica", 12, "normal"))
is_equal_to_label = Label(text="is equal to", font=("Helvetica", 12, "normal"))
converted_label = Label(text="0", font=("Helvetica", 12, "normal"))
kilometers_label = Label(text="kilometers", font=("Helvetica", 12, "normal"))

# Button
calculate_button = Button(text="Calculate", command=convert)

# Entry
miles_input_entry = Entry(width=20)

miles_input_entry.grid(row=0, column=1, pady=5)
miles_label.grid(row=0, column=2, pady=5)
is_equal_to_label.grid(row=1, column=0, padx=5, pady=5)
converted_label.grid(row=1, column=1, pady=5)
kilometers_label.grid(row=1, column=2, padx=20, pady=5)
calculate_button.grid(row=2, column=1, pady=10)

window.mainloop()
