import tkinter as tk
from tkinter import ttk

def run_filter():
    flavor = flavor_var.get()
    dairy = dairy_var.get()
    sugar = sugar_var.get()

    dairy_free = True if dairy == "Yes" else False if dairy == "No" else None
    low_sugar = True if sugar == "Yes" else False if sugar == "No" else None

    results = filter_ice_cream(df, flavor, dairy_free, low_sugar)

    output.delete("1.0", tk.END)
    if results.empty:
        output.insert(tk.END, "No matches found")
    else:
        for name in results["name"]:
            output.insert(tk.END, name + "\n")

root = tk.Tk()
root.title("Scoop Select")

flavor_var = tk.StringVar()
dairy_var = tk.StringVar()
sugar_var = tk.StringVar()

ttk.Label(root, text="Flavor Type").pack()
ttk.Combobox(root, textvariable=flavor_var, values=["", "chocolatey", "fruity", "classic"]).pack()

ttk.Label(root, text="Dairy Free").pack()
ttk.Combobox(root, textvariable=dairy_var, values=["", "Yes", "No"]).pack()

ttk.Label(root, text="Low Sugar").pack()
ttk.Combobox(root, textvariable=sugar_var, values=["", "Yes", "No"]).pack()

ttk.Button(root, text="Filter", command=run_filter).pack()

output = tk.Text(root, height=10)
output.pack()

root.mainloop()