import tkinter as tk

def update_w_c(*args):
    global editing_lock
    if editing_lock:
        return
    else:
        editing_lock = True
    try:
        celsius = float(celsius_var.get())
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        fahrenheit_var.set("%.2f" % fahrenheit)
        kelvin_var.set("%.2f" % kelvin)
    except ValueError:
        pass
    editing_lock = False
def update_w_f(*args):
    global editing_lock
    if editing_lock:
        return
    else:
        editing_lock = True
    try:
        fahrenheit = float(fahrenheit_var.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_var.set("%.2f" % celsius)
        kelvin = celsius + 273.15
        kelvin_var.set("%.2f" % kelvin)
    except ValueError:
        pass
    editing_lock = False
def update_w_k(*args):
    global editing_lock
    if editing_lock:
        return
    else:
        editing_lock = True
    try:
        kelvin = float(kelvin_var.get())
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_var.set("%.2f" % fahrenheit)
        celsius_var.set("%.2f" % celsius)
    except ValueError:
        pass
    editing_lock = False

root = tk.Tk()
root.title("Temperature Converter")

celsius_var = tk.StringVar()
celsius_var.trace("w", update_w_c)
celsius_entry = tk.Entry(root, textvariable=celsius_var)
celsius_entry.grid(row=0, column=0)

fahrenheit_var = tk.StringVar()
fahrenheit_var.trace("w", update_w_f)
fahrenheit_entry = tk.Entry(root, textvariable=fahrenheit_var)
fahrenheit_entry.grid(row=0, column=1)

kelvin_var = tk.StringVar()
kelvin_var.trace("w", update_w_k)
kelvin_entry = tk.Entry(root, textvariable=kelvin_var)
kelvin_entry.grid(row=0, column=2)

celsius_label = tk.Label(root, text="Celsius")
celsius_label.grid(row=1, column=0)

fahrenheit_label = tk.Label(root, text="Fahrenheit")
fahrenheit_label.grid(row=1, column=1)

kelvin_label = tk.Label(root, text="Kelvin")
kelvin_label.grid(row=1, column=2)

editing_lock = False

root.mainloop()
