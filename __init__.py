"""
Translation Calculator
======================

A GUI-based utility for calculating translation prices based on character count, 
with support for express translation surcharges and discounts.

Main Features:
- Calculate standard translation lines from character count
- Apply express translation surcharges
- Apply percentage-based discounts
- Display detailed price calculations
- Convert between standard lines and standard pages
- Persistent settings storage

Usage:
    from translation_calculator import TranslationCalculator
    
    # Create and run the calculator
    calculator = TranslationCalculator()
    calculator.run()
"""

__version__ = "1.0.0"
__author__ = "Tade Strehk"

from .main import TranslationCalculator
from .base_values import base_values, STANDARD_LINE, PRICE_PER_LINE, SURCHARGE, STANDARD_PAGE

__all__ = [
    "TranslationCalculator",
    "base_values",
    "STANDARD_LINE",
    "PRICE_PER_LINE",
    "SURCHARGE",
    "STANDARD_PAGE"
]
