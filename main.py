import pickle
import customtkinter as ctk
from tkinter import messagebox
from base_values import (
    base_values,
    STANDARD_LINE,
    PRICE_PER_LINE,
    SURCHARGE,
    STANDARD_PAGE,
)
import os
from version import __version__

BASE_VALUE_PATH = "tmp/base_values.pickle"


def align_right(text, length):
    return str(text).rjust(length)


class TranslationCalculator:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Translation Calculator")

        try:
            with open(BASE_VALUE_PATH, "rb") as f:
                self.base_values: base_values = pickle.load(f)
        except FileNotFoundError:
            self.base_values = base_values(
                PRICE_PER_LINE, SURCHARGE, STANDARD_LINE, STANDARD_PAGE
            )
            self.save_base_values()

        # Main window setup
        self.setup_main_window()

    def save_base_values(self):
        if not os.path.exists("tmp"):
            os.makedirs("tmp")
        with open(BASE_VALUE_PATH, "wb") as f:
            pickle.dump(self.base_values, f)

    def setup_main_window(self):
        # Input fields
        ctk.CTkLabel(self.root, text="Characters:").grid(
            row=0, column=0, padx=10, pady=10
        )
        self.chars_entry = ctk.CTkEntry(self.root)
        self.chars_entry.grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.root, text="Discount (%):").grid(
            row=1, column=0, padx=10, pady=10
        )
        self.discount_entry = ctk.CTkEntry(self.root)
        self.discount_entry.grid(row=1, column=1, padx=10, pady=10)

        # Express surcharge switch
        self.express_var = ctk.BooleanVar()
        self.express_switch = ctk.CTkSwitch(
            self.root, text="Express Surcharge", variable=self.express_var
        )
        self.express_switch.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Buttons
        ctk.CTkButton(self.root, text="Calculate", command=self.show_results).grid(
            row=3, column=0, padx=10, pady=10
        )
        ctk.CTkButton(self.root, text="Options", command=self.show_options).grid(
            row=3, column=1, padx=10, pady=10
        )

        # Version label
        ctk.CTkLabel(self.root, text=f"Version: {__version__}", font=("", 10)).grid(
            row=4, column=0, columnspan=2
        )

    def calculate_discount(self, price):
        if self.discount_entry.get():
            discount = float(self.discount_entry.get()) / 100
            price_with_discount = price * (1 - discount)
            return discount, price_with_discount
        else:
            return 0, price

    def calculate_surcharge(self, price):
        if self.express_var.get():
            return price + self.base_values.express_surcharge
        return price

    def calculate_price(self, characters):
        characters = int(characters)
        standard_lines = round(characters / self.base_values.standard_line, 2)
        price = round(standard_lines * self.base_values.base_price_per_line, 2)
        discount, price_with_discount = self.calculate_discount(price)
        price_with_surcharge = self.calculate_surcharge(price_with_discount)
        return (
            characters,
            standard_lines,
            price,
            discount,
            price_with_discount,
            price_with_surcharge,
        )

    def print_price(
        self,
        characters,
        standard_lines,
        price,
        discount,
        price_with_discount,
        price_with_surcharge,
    ):
        prints = []

        prints.append("\n")
        prints.append("Calculation basis:\n")
        prints.append(
            f"Characters:       {characters} translated characters (including spaces)"
        )
        prints.append(f"Standard line:    {self.base_values.standard_line} characters")
        prints.append(
            f"Standard page:    {self.base_values.standard_page} standard lines"
        )
        prints.append(
            f"Base price:       {self.base_values.base_price_per_line:.2f} € per standard line"
        )
        if discount != 0:
            prints.append(f"Discount:         {discount * 100:.2f} %")
        if price_with_surcharge != price_with_discount:
            prints.append(
                f"Surcharge:        {self.base_values.express_surcharge:.2f} € (express fee)"
            )

        prints.append("\n----------------------------------------------------\n")

        prints.append(f"  {align_right(characters, 7)}    characters")
        prints.append(
            f"/ {align_right(self.base_values.standard_line, 7)}    characters per standard line"
        )
        prints.append("  ------- --")
        prints.append(f"  {align_right(f'{standard_lines:.2f}', 10)} standard lines")
        prints.append(
            f"  {align_right(f'(≙  {(standard_lines / self.base_values.standard_page):.2f}', 10)} standard pages)"
        )

        prints.append("\n----------------------------------------------------\n")

        prints.append(f"  {align_right(f'{standard_lines:.2f}', 10)}   standard lines")
        prints.append(
            f"* {align_right(f'{self.base_values.base_price_per_line:.2f}', 10)} € price per standard line"
        )
        prints.append("  ------- --")
        prints.append(f"  {align_right(f'{price:.2f}', 10)} € price")
        if price_with_surcharge != price_with_discount or discount != 0:
            if discount != 0:
                prints.append(
                    f"- {align_right(f'{(price - price_with_discount):.2f}', 10)} € discount"
                )
            if price_with_surcharge != price_with_discount:
                prints.append(
                    f"+ {align_right(f'{self.base_values.express_surcharge:.2f}', 10)} € express fee"
                )
            prints.append("  ------- --")
            prints.append(
                f"  {align_right(f'{price_with_surcharge:.2f}', 10)} € price with {'surcharge and discount' if price_with_surcharge != price_with_discount and discount != 0 else ('discount' if discount != 0 else 'surcharge')}"
            )

        prints.append("\n----------------------------------------------------\n")

        prints.append(
            f"The final price for {standard_lines} standard lines ({characters} characters{'' if price_with_discount == price_with_surcharge else f', {self.base_values.express_surcharge:.2f}€ express fee'}{'' if discount == 0 else f', {round(discount * 100)}% discount'}) is: {price_with_surcharge:.2f} €\n\n\n"
        )

        return "\n".join(prints)

    def show_results(self):
        try:

            results = self.calculate_price(self.chars_entry.get())
            if results:
                results_window = ctk.CTkToplevel(self.root)
                results_window.geometry("600x600")
                results_window.title("Calculation Results")

                text = ctk.CTkTextbox(
                    results_window, font=("Courier", 12), padx=20, pady=20
                )
                text.insert("end", self.print_price(*results))
                text.pack(expand=True, fill="both")
            else:
                raise Exception("Invalid input")
        except Exception as e:
            messagebox.showerror("Error", f"Please enter valid numbers ({e})")

    def show_options(self):
        options_window = ctk.CTkToplevel(self.root)
        options_window.title("Options")

        ctk.CTkLabel(options_window, text="Price per character:").grid(
            row=0, column=0, padx=10, pady=10
        )
        price_entry = ctk.CTkEntry(options_window)
        price_entry.insert(0, str(self.base_values.base_price_per_line))
        price_entry.grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(options_window, text="Express surcharge:").grid(
            row=1, column=0, padx=10, pady=10
        )
        surcharge_entry = ctk.CTkEntry(options_window)
        surcharge_entry.insert(0, str(self.base_values.express_surcharge))
        surcharge_entry.grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkLabel(options_window, text="Standard line:").grid(
            row=2, column=0, padx=10, pady=10
        )
        standard_line_entry = ctk.CTkEntry(options_window)
        standard_line_entry.insert(0, str(self.base_values.standard_line))
        standard_line_entry.grid(row=2, column=1, padx=10, pady=10)

        ctk.CTkLabel(options_window, text="Standard page:").grid(
            row=3, column=0, padx=10, pady=10
        )
        standard_page_entry = ctk.CTkEntry(options_window)
        standard_page_entry.insert(0, str(self.base_values.standard_page))
        standard_page_entry.grid(row=3, column=1, padx=10, pady=10)

        def save_options():
            try:
                self.base_values.base_price_per_line = float(price_entry.get())
                self.base_values.express_surcharge = float(surcharge_entry.get())
                self.base_values.standard_line = int(standard_line_entry.get())
                self.base_values.standard_page = int(standard_page_entry.get())
                self.save_base_values()
                options_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")

        ctk.CTkButton(options_window, text="Save", command=save_options).grid(
            row=4, column=0, columnspan=2, padx=10, pady=10
        )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = TranslationCalculator()
    app.run()
