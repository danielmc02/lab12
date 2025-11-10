"""
pie.py

Pumpkin pie food decorator.
"""

from plate_decorator import PlateDecorator


class Pie(PlateDecorator):
    """Adds a serving of pumpkin pie: area 19, weight 8."""

    def description(self) -> str:
        """Append 'Pie' to the current plate description."""
        base = super().description()
        return f"{base} with Pie" if " with " not in base else f"{base} and Pie"

    def area(self) -> int:
        """Reduce remaining area by the pie's footprint."""
        return super().area() - 19

    def weight(self) -> int:
        """Reduce remaining weight capacity by the pie's weight."""
        return super().weight() - 8

    def count(self) -> int:
        """Increment food count by 1."""
        return super().count() + 1

