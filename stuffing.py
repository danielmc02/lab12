"""
stuffing.py

Stuffing food decorator.
"""

from plate_decorator import PlateDecorator


class Stuffing(PlateDecorator):
    """Adds a serving of stuffing: area 18, weight 7."""

    def description(self) -> str:
        """Append 'Stuffing' to the current plate description."""
        base = super().description()
        return f"{base} with Stuffing" if " with " not in base else f"{base} and Stuffing"

    def area(self) -> int:
        """Reduce remaining area by stuffing's footprint."""
        return super().area() - 18

    def weight(self) -> int:
        """Reduce remaining weight capacity by stuffing's weight."""
        return super().weight() - 7

    def count(self) -> int:
        """Increment food count by 1."""
        return super().count() + 1
