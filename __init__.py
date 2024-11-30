"""
Translation Calculator
====================

A utility for calculating translation prices based on character count, 
with support for express translation surcharges and discounts.

Main Features:
- Calculate standard translation lines from character count
- Apply express translation surcharges
- Apply percentage-based discounts
- Display detailed price calculations
- Convert between standard lines and standard pages

Usage:
    from translation_calculator import calculate_price, print_price
    
    # Calculate price for a translation
    results = calculate_price(1000)  # 1000 characters
    characters, std_lines, price, discount, price_with_discount, final_price = results
    
    # Print detailed calculation
    print_price(*results)
"""

__version__ = "1.0.0"
__author__ = "Tade Strehk"

from .translation_calculator import (
    calculate_price,
    print_price,
    calculate_discount,
    calculate_surcharge,
)

__all__ = [
    "calculate_price",
    "print_price",
    "calculate_discount",
    "calculate_surcharge",
]
