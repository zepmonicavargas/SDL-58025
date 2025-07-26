
import tkinter as tk
from tkinter import ttk

class Inventory:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        self.inventory = {
            'motherboard': 0,
            'hard disk': 0,
            'diskette': 0,
            'compact disk': 0,
            'memory cards': 0
        }

        self.create_widgets()

    def create_widgets(self):
        # Labels
        ttk.Label(self.root, text="Inventory Management System", font=('Arial', 14)).grid(row=0, column=1, pady=10)

        # Treeview to display inventory
        self.tree = ttk.Treeview(self.root, columns=('Product', 'Quantity'), show='headings', height=5)
        self.tree.heading('Product', text='Product')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.grid(row=1, column=0, columnspan=3, padx=10)

        # Buttons
        ttk.Button(self.root, text="Display Inventory", command=self.display_inventory).grid(row=2, column=0, pady=5)
        ttk.Button(self.root, text="Add Items", command=self.add_items).grid(row=2, column=1, pady=5)
        ttk.Button(self.root, text="Remove Items", command=self.remove_items).grid(row=2, column=2, pady=5)
        ttk.Button(self.root, text="Quit", command=self.root.destroy).grid(row=3, column=1, pady=10)

    def display_inventory(self):
        # Clear existing items in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Populate treeview with current inventory
        for product, quantity in self.inventory.items():
            self.tree.insert('', 'end', values=(product, quantity))

    def add_items(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Items")

        # Labels and Entry widgets
        ttk.Label(add_window, text="Product:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(add_window, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)

        product_entry = ttk.Entry(add_window)
        quantity_entry = ttk.Entry(add_window)

        product_entry.grid(row=0, column=1, padx=5, pady=5)
        quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        # Button to add items
        ttk.Button(add_window, text="Add", command=lambda: self.add_items_action(product_entry.get(), quantity_entry.get(), add_window)).grid(row=2, column=0, columnspan=2, pady=10)

    def add_items_action(self, product, quantity, add_window):
        try:
            quantity = int(quantity)
            if product in self.inventory:
                self.inventory[product] += quantity
                self.display_inventory()
                add_window.destroy()
            else:
                tk.messagebox.showerror("Error", "Invalid product.")
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid quantity.")

    def remove_items(self):
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remove Items")

        # Labels and Entry widgets
        ttk.Label(remove_window, text="Product:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(remove_window, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)

        product_entry = ttk.Entry(remove_window)
        quantity_entry = ttk.Entry(remove_window)

        product_entry.grid(row=0, column=1, padx=5, pady=5)
        quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        # Button to remove items
        ttk.Button(remove_window, text="Remove", command=lambda: self.remove_items_action(product_entry.get(), quantity_entry.get(), remove_window)).grid(row=2, column=0, columnspan=2, pady=10)

    def remove_items_action(self, product, quantity, remove_window):
        try:
            quantity = int(quantity)
            if product in self.inventory and self.inventory[product] >= quantity:
                self.inventory[product] -= quantity
                self.display_inventory()
                remove_window.destroy()
            else:
                tk.messagebox.showerror("Error", "Invalid product or insufficient quantity.")
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid quantity.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Inventory(root)
    root.mainloop()
