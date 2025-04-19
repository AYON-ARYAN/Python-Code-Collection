import tkinter as tk


def radio_clicked():
    selected_radio.set("Radio Button " + str(radio_var.get()) + " clicked")
    print("Value of the radio button clicked:", radio_var.get())


def check_clicked():
    check_state1 = "checked" if check_var1.get() else "unchecked"
    check_state2 = "checked" if check_var2.get() else 'unchecked'
    check_label.config(text="Check Button 1 is " + check_state1 + "\nCheck Button 2 is " + check_state2)


root = tk.Tk()
root.title("Radio and Check Buttons")

radio_var = tk.IntVar()
check_var1 = tk.BooleanVar()
check_var2 = tk.BooleanVar()
selected_radio = tk.StringVar()

radio_button1 = tk.Radiobutton(root, text="Radio Button 1", variable=radio_var, value=1, command=radio_clicked)
radio_button1.pack()

radio_button2 = tk.Radiobutton(root, text="Radio Button 2", variable=radio_var, value=2, command=radio_clicked)
radio_button2.pack()

radio_button3 = tk.Radiobutton(root, text="Radio Button 3", variable=radio_var, value=3, command=radio_clicked)
radio_button3.pack()

check_button1 = tk.Checkbutton(root, text="Check Button 1", variable=check_var1, command=check_clicked)
check_button1.pack()

check_button2 = tk.Checkbutton(root, text="Check Button 2", variable=check_var2, command=check_clicked)
check_button2.pack()

check_label = tk.Label(root, text="")
check_label.pack()

root.mainloop()
