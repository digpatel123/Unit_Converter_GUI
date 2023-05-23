from tkinter import *

# Initializing the window
window = Tk()
window.config(padx=30, pady=30)
window.title("Miles to km Converter")

# Textbox to enter number in miles
miles = Entry(width=10)
miles.insert(END, string="0")
miles.config()
miles.grid(column=1, row=0)

# Text for miles
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# Text for converted mles is equal to
iqt_label = Label(text="Is equal to")
iqt_label.grid(column=0, row=1)

# Textbox for converted km
km = Entry(width=10)
km.insert(END, string="0")
km.grid(column=1, row=1)

# Text for km
km_label = Label(text="km")
km_label.grid(column=2, row=1)

# Function to convert miles
def convert():
    m = float(miles.get())
    k = round(m * 1.60934, 2)
    km.delete(0, END)
    km.insert(END, string=f"{k}")
# Button to Convert
cal_button = Button(text="Convert", command=convert)
cal_button.grid(column=1, row=2)



window.mainloop()