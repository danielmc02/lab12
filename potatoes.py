"""
potatoes.py

Potatoes food decorator.
"""

from plate_decorator import PlateDecorator


class Potatoes(PlateDecorator):
    """Adds a serving of potatoes: area 18, weight 6."""

    def description(self) -> str:
        """Append 'Potatoes' to the current plate description."""
        base = super().description()
        return f"{base} with Potatoes" if " with " not in base else f"{base} and Potatoes"

    def area(self) -> int:
        """Reduce remaining area by potatoes' footprint."""
        return super().area() - 18

    def weight(self) -> int:
        """Reduce remaining weight capacity by potatoes' weight."""
        return super().weight() - 6

    def count(self) -> int:
        """Increment food count by 1."""
        return super().count() + 1

