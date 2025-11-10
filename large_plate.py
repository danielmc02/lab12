"""
large_plate.py

Concrete large, flimsy 12-inch paper plate.
"""

from plate import Plate


class LargePlate(Plate):
    """Large flimsy plate: 113 sq in area, 24 oz capacity."""

    def description(self) -> str:
        """Return the plate description without any food."""
        return "Flimsy 12 inch paper plate"

    def area(self) -> int:
        """Return the remaining area (full capacity for the base plate)."""
        return 113  # per spec
    def weight(self) -> int:
        """Return the remaining weight capacity (full capacity for base)."""
        return 24   # per spec
    def count(self) -> int:
        """No food items yet on a base plate."""
        return 0
