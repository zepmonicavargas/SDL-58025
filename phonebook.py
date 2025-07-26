import csv
import tkinter as tk
from tkinter import messagebox

class PhonebookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Phonebook Search")

        # Set window size
        self.master.geometry("400x180")

        # Create and set up GUI components with modified sizes
        self.label = tk.Label(master, text="Enter Name:", font=("Helvetica", 12, "bold"), fg="black")
        self.label.pack(pady=13)

        self.name_entry = tk.Entry(master, width=30)  # Adjust the width of the entry
        self.name_entry.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12))  # Adjust the font size
        self.result_label.pack(pady=10)

        self.search_button = tk.Button(master, text="Search", font=("Helvetica", 10, "bold"), command=self.search_phone, width=15)  # Adjust the width of the button
        self.search_button.pack(pady=10)

    def search_phone(self):
        name_to_search = self.name_entry.get().lower()

        try:
            with open('phonebook.csv', 'r') as file:
                reader = csv.reader(file)
                phonebook = {name.lower(): phone for name, phone in reader}

                if name_to_search in phonebook:
                    phone_number = phonebook[name_to_search]
                    self.result_label.config(text=f"The phone number for {name_to_search} is {phone_number}")
                else:
                    self.result_label.config(text=f"No phone number found for {name_to_search}")

        except FileNotFoundError:
            messagebox.showerror("Error", "Phonebook file not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhonebookApp(root)
    root.mainloop()

