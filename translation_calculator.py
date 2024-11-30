import os
import re
import time

from base_values import STANDARD_LINE, PRICE_PER_LINE, SURCHARGE, STANDARD_PAGE


def align_right(text, length):
    return str(text).rjust(length)


def calculate_surcharge(price):
    surcharge = input("Is this an express translation? (y/n) ")

    if surcharge == "y":
        price_with_surcharge = price + SURCHARGE
    else:
        price_with_surcharge = price

    return price_with_surcharge


def calculate_discount(price):
    discount_check = input("Should there be a discount? (y/n) ")
    if discount_check == "y":
        while True:
            try:
                discount_input = input("Enter the discount (in %): ")
                if discount_input.isdigit():
                    discount = float(discount_input) / 100
                    price_with_discount = price * (1 - discount)
                    return discount, price_with_discount
                else:
                    raise ValueError("Please enter a number.")
            except ValueError as e:
                print(e)
                continue
    else:
        return 0, price


def calculate_price(characters):
    characters = int(characters)
    standard_lines = round(characters / STANDARD_LINE, 2)
    price = round(standard_lines * PRICE_PER_LINE, 2)
    discount, price_with_discount = calculate_discount(price)
    price_with_surcharge = calculate_surcharge(price_with_discount)
    return (
        characters,
        standard_lines,
        price,
        discount,
        price_with_discount,
        price_with_surcharge,
    )


def print_price(
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
    prints.append(f"Standard line:    {STANDARD_LINE} characters")
    prints.append(f"Base price:       {PRICE_PER_LINE:.2f} € per standard line")
    if discount != 0:
        prints.append(f"Discount:         {discount * 100:.2f} %")
    if price_with_surcharge != price_with_discount:
        prints.append(f"Surcharge:        {SURCHARGE:.2f} € (express fee)")

    prints.append("\n----------------------------------------------------\n")

    prints.append(f"  {align_right(characters, 7)}    characters")
    prints.append(f"/ {align_right(STANDARD_LINE, 7)}    characters per standard line")
    prints.append("  ------- --")
    prints.append(f"  {align_right(f'{standard_lines:.2f}', 10)} standard lines")
    prints.append(
        f"  {align_right(f'(≙  {(standard_lines / STANDARD_PAGE):.2f}', 10)} standard pages)"
    )

    prints.append("\n----------------------------------------------------\n")

    prints.append(f"  {align_right(f'{standard_lines:.2f}', 10)}   standard lines")
    prints.append(
        f"* {align_right(f'{PRICE_PER_LINE:.2f}', 10)} € price per standard line"
    )
    prints.append("  ------- --")
    prints.append(f"  {align_right(f'{price:.2f}', 10)} € price")
    if price_with_surcharge != price_with_discount or discount != 0:
        if discount != 0:
            prints.append(
                f"- {align_right(f'{(price - price_with_discount):.2f}', 10)} € discount"
            )
        if price_with_surcharge != price_with_discount:
            prints.append(f"+ {align_right(f'{SURCHARGE:.2f}', 10)} € express fee")
        prints.append("  ------- --")
        prints.append(
            f"  {align_right(f'{price_with_surcharge:.2f}', 10)} € price with {'surcharge and discount' if price_with_surcharge != price_with_discount and discount != 0 else ('discount' if discount != 0 else 'surcharge')}"
        )

    prints.append("\n----------------------------------------------------\n")

    prints.append(
        f"The final price for {standard_lines} standard lines ({characters} characters{'' if price_with_discount == price_with_surcharge else f', {SURCHARGE:.2f}€ express fee'}{'' if discount == 0 else f', {round(discount * 100)}% discount'}) is: {price_with_surcharge:.2f} €\n\n\n"
    )

    for item in prints:
        print(item)
        time.sleep(0.2)

    time.sleep(4)

    _ = input("Press Enter to restart the program...")
    print("\n\n\n")


def main():
    os.system("clear")
    while True:
        try:
            characters = input("Enter the number of characters (including spaces): ")

            if characters.isdigit():
                (
                    characters,
                    standard_lines,
                    price,
                    discount,
                    price_with_discount,
                    price_with_surcharge,
                ) = calculate_price(characters)
                print_price(
                    characters,
                    standard_lines,
                    price,
                    discount,
                    price_with_discount,
                    price_with_surcharge,
                )

            else:
                raise ValueError("Please enter a number.")

        except ValueError as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
