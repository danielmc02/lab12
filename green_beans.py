"""
green_beans.py

Green beans food decorator.
"""

from plate_decorator import PlateDecorator


class GreenBeans(PlateDecorator):
    """Adds a serving of green beans: area 20, weight 3."""

    def description(self) -> str:
        """Append 'Green Beans' to the current plate description."""
        base = super().description()
        return f"{base} with Green Beans" if " with " not in base else f"{base} and Green Beans"

    def area(self) -> int:
        """Reduce remaining area by green beans' footprint."""
        return super().area() - 20

    def weight(self) -> int:
        """Reduce remaining weight capacity by green beans' weight."""
        return super().weight() - 3

    def count(self) -> int:
        """Increment food count by 1."""
        return super().count() + 1
