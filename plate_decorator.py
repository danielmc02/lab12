"""
plate_decorator.py

Base decorator that wraps a Plate and delegates operations.
"""

from abc import ABC
from plate import Plate


class PlateDecorator(Plate, ABC):
    """
    Abstract decorator that forwards all Plate operations
    to the wrapped Plate instance.
    """

    def __init__(self, p: Plate) -> None:
        """
        Initialize the decorator with an existing Plate.
        :param p: Plate to decorate.
        """
        self._plate = p

    def description(self) -> str:
        """Delegate description to the wrapped plate."""
        return self._plate.description()

    def area(self) -> int:
        """Delegate area to the wrapped plate."""
        return self._plate.area()

    def weight(self) -> int:
        """Delegate weight to the wrapped plate."""
        return self._plate.weight()

    def count(self) -> int:
        """Delegate count to the wrapped plate."""
        return self._plate.count()
