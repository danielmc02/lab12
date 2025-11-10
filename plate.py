"""
plate.py

Defines the Plate interface for the Thanksgiving Dinner program.
"""

from abc import ABC, abstractmethod


class Plate(ABC):
    """Abstract base interface for all plates and decorated plates."""

    @abstractmethod
    def description(self) -> str:
        """
        Return a string description of the plate and what is on it.
        For base plates, this is the plate description; for decorated
        plates, this includes appended food names.
        """
        raise NotImplementedError

    @abstractmethod
    def area(self) -> int:
        """
        Return the remaining square inches the plate can hold.
        Base plates return their full area; decorators subtract food area.
        """
        raise NotImplementedError

    @abstractmethod
    def weight(self) -> int:
        """
        Return the remaining ounces the plate can support.
        Base plates return their full capacity; decorators subtract food weight.
        """
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        """
        Return the number of food items currently on the plate.
        Base plates return 0; decorators increment by 1 for each added food.
        """
        raise NotImplementedError
