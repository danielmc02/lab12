"""
turkey.py

Turkey food decorator.
"""

from plate_decorator import PlateDecorator


class Turkey(PlateDecorator):
    """Adds a serving of turkey: area 15, weight 4."""

    def description(self) -> str:
        """Append 'Turkey' to the current plate description."""
        base = super().description()
        return f"{base} with Turkey" if " with " not in base else f"{base} and Turkey"

    def area(self) -> int:
        """Reduce remaining area by the turkey's footprint."""
        return super().area() - 15

    def weight(self) -> int:
        """Reduce remaining weight capacity by the turkey's weight."""
        return super().weight() - 4

    def count(self) -> int:
        """Increment food count by 1."""
        return super().count() + 1
