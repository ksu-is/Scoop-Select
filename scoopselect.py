import tkinter as tk
from tkinter import ttk

# ---------------- ICE CREAM DATA ---------------- #

ice_cream_list = [

    {
        "name": "Vanilla",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["none"],
        "brand": "Publix Rich & Creamy Premium"
    },

    {
        "name": "French Vanilla",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["none"],
        "brand": "Publix Rich & Creamy Premium"
    },

    {
        "name": "Moose Tracks",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["nuts"],
        "brand": "Publix Rich & Creamy Premium"
    },

    {
        "name": "Otter Paws",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["nuts", "caramel"],
        "brand": "Publix Rich & Creamy Premium"
    },

    {
        "name": "Cool Lime",
        "type": "fruit",
        "dairy_free": "yes",
        "toppings": ["none"],
        "brand": "Publix Sherbet"
    },

    {
        "name": "It's Your Birthday Cake!",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["cookies"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Southern Banana Pudding",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["cookies"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Heavenly Hash",
        "type": "chocolate",
        "dairy_free": "no",
        "toppings": ["nuts"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Chocolate Cherish Passion",
        "type": "fruit",
        "dairy_free": "no",
        "toppings": ["fruit"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Black Jack Cherry",
        "type": "fruit",
        "dairy_free": "no",
        "toppings": ["fruit"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Moose Tracks Frozen Yogurt",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["nuts"],
        "brand": "Publix Frozen Yogurt"
    },
    {
        "name": "Chocolate Moose Tracks",
        "type": "chocolate",
        "dairy_free": "no",
        "toppings": ["nuts"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Brownie Moose Tracks",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["brownies"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Vanilla, Homestyle",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["none"],
        "brand": "Publix Premium"
    },
    {
        "name": "Banana Split",
        "type": "fruit",
        "dairy_free": "no",
        "toppings": ["fruit", "nuts"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Raspberry Blush",
        "type": "fruit",
        "dairy_free": "yes",
        "toppings": ["none"],
        "brand": "Publix Sherbet"
    },
    {
        "name": "Rainbow Dream",
        "type": "fruit",
        "dairy_free": "yes",
        "toppings": ["none"],
        "brand": "Publix Sherbet"
    },
    {
        "name": "Sunny Orange",
        "type": "fruit",
        "dairy_free": "yes",
        "toppings": ["none"],
        "brand": "Publix Sherbet"
    },
    {
        "name": "Coconut Road",
        "type": "fruit",
        "dairy_free": "no",
        "toppings": ["fruit", "nuts", "caramel"],
        "brand": "Publix Frozen Yogurt"
    },
    {
        "name": "Creamy Coconut Road",
        "type": "fruit",
        "dairy_free": "non",
        "toppings": ["fruit", "nuts", "caramel"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Black Jack Cherry",
        "type": "fruit",
        "dairy_free": "no",
        "toppings": ["fruit"],
        "brand": "Publix Frozen Yogurt"
    },
    {
        "name": "Roadrunner Raspberry",
        "type": "chocolate",
        "dairy_free": "no",
        "toppings": ["fruit"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Cookies & Cream",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["cookies"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Chocolate",
        "type": "chocolate",
        "dairy_free": "no",
        "toppings": ["none"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Chocolate Chip Cookie Dough",
        "type": "classic",
        "dairy_free": "no",
        "toppings": ["cookies"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Chocolate Almond",
        "type": "chocolate",
        "dairy_free": "no",
        "toppings": ["nuts"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Cherry Nut",
        "type": "fruit",
        "dairy_free": "no",
        "toppings": ["fruit", "nuts"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Strawberry",
        "type": "fruit",
        "dairy_free": "no",
        "toppings": ["fruit"],
        "brand": "Publix Rich & Creamy Premium"
    },
    {
        "name": "Mango Peach",
        "type": "fruit",
        "dairy_free": "yes",
        "toppings": ["none"],
        "brand": "Publix Sherbet"
    },
]
# ---------------- FILTER FUNCTION ---------------- #

def filter_ice_cream():

    flavor = flavor_var.get()
    dairy = dairy_var.get()

    # Get selected toppings
    selected_toppings = []

    for topping, var in topping_vars.items():
        if var.get() == 1:
            selected_toppings.append(topping)

    # Clear old results
    output_text.delete(1.0, tk.END)

    results = []

    # ---------------- FILTERING ---------------- #

    for ice_cream in ice_cream_list:

        if flavor and ice_cream["type"] != flavor:
            continue

        if dairy and ice_cream["dairy_free"] != dairy:
            continue

        # Multiple topping filter
        if selected_toppings:

            match = False

            for topping in selected_toppings:
                if topping in ice_cream["toppings"]:
                    match = True

            if not match:
                continue

        results.append(ice_cream)

    # ---------------- DISPLAY RESULTS ---------------- #

    output_text.insert(tk.END, "🍦 Scoop Select Results 🍦\n\n")

    if len(results) == 0:
        output_text.insert(tk.END, "No matching ice creams found 😢")

    else:

        output_text.insert(
            tk.END,
            f"Found {len(results)} matching options!\n\n"
        )

        for item in results:

            output_text.insert(
                tk.END,
                f"Name: {item['name']}\n"
            )

            output_text.insert(
                tk.END,
                f"Brand: {item['brand']}\n"
            )

            output_text.insert(
                tk.END,
                f"Flavor Type: {item['type']}\n"
            )

            output_text.insert(
                tk.END,
                f"Dairy-Free: {item['dairy_free']}\n"
            )

            output_text.insert(
                tk.END,
                f"Toppings: {', '.join(item['toppings'])}\n"
            )

            output_text.insert(
                tk.END,
                "-----------------------------------\n"
            )

# ---------------- GUI WINDOW ---------------- #

root = tk.Tk()
root.title("Scoop Select 🍦")
root.geometry("600x700")

# ---------------- TITLE ---------------- #

title_label = tk.Label(
    root,
    text="Welcome to Scoop Select 🍦",
    font=("Arial", 18)
)

title_label.pack(pady=10)

# ---------------- FLAVOR FILTER ---------------- #

tk.Label(root, text="Flavor Type").pack()

flavor_var = tk.StringVar()

flavor_dropdown = ttk.Combobox(
    root,
    textvariable=flavor_var,
    values=["", "chocolate", "fruit", "classic"]
)

flavor_dropdown.pack(pady=5)

# ---------------- DAIRY FILTER ---------------- #

tk.Label(root, text="Dairy-Free").pack()

dairy_var = tk.StringVar()

dairy_dropdown = ttk.Combobox(
    root,
    textvariable=dairy_var,
    values=["", "yes", "no"]
)

dairy_dropdown.pack(pady=5)

# ---------------- MULTIPLE TOPPING FILTERS ---------------- #

tk.Label(
    root,
    text="Select Favorite Toppings"
).pack(pady=10)

# Store checkbox variables
topping_vars = {}

toppings = [
    "brownies",
    "cookies",
    "fruit",
    "caramel",
    "nuts",
    "none"
]

# Create checkboxes
for topping in toppings:

    var = tk.IntVar()

    checkbox = tk.Checkbutton(
        root,
        text=topping,
        variable=var
    )

    checkbox.pack(anchor="w", padx=220)

    topping_vars[topping] = var

# ---------------- BUTTON ---------------- #

filter_button = tk.Button(
    root,
    text="Find Ice Cream",
    command=filter_ice_cream,
    font=("Arial", 12)
)

filter_button.pack(pady=15)

# ---------------- OUTPUT BOX ---------------- #

output_text = tk.Text(
    root,
    height=20,
    width=65
)

output_text.pack(pady=10)

# ---------------- START PROGRAM ---------------- #

root.mainloop()