"""
small_plate.py

Concrete small, sturdy 10-inch paper plate.
"""

from plate import Plate


class SmallPlate(Plate):
    """Small sturdy plate: 78 sq in area, 32 oz capacity."""

    def description(self) -> str:
        """Return the plate description without any food."""
        return "Sturdy 10 inch paper plate"

    def area(self) -> int:
        """Return the remaining area (full capacity for the base plate)."""
        return 78  # per spec
    def weight(self) -> int:
        """Return the remaining weight capacity (full capacity for base)."""
        return 32  # per spec
    def count(self) -> int:
        """No food items yet on a base plate."""
        return 0
