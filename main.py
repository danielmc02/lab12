"""
main.py

Names:
Date:
Brief: Thanksgiving Dinner game using the Decorator Pattern. The user
selects a plate and adds foods without exceeding area or weight limits.
"""

from typing import Type, Dict
import check_input  # provided by course; used for all input validation

from plate import Plate
from small_plate import SmallPlate
from large_plate import LargePlate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie


def examine_plate(p: Plate) -> bool:
    """
    Display the plate's description and hints based on *remaining* area/weight.
    Return True if the plate fails (area <= 0 or weight <= 0), otherwise False.

    Failure messages:
      - Area failure: "Your plate isn't big enough..."
      - Weight failure: "Your plate can't support this much weight..."
    Hint ranges (from spec suggestions):
      Weight remaining: 1–6 -> Bending, 7–12 -> Weak, 13+ -> Strong
      Area remaining  : 1–20 -> A tiny bit, 21–40 -> Some, 41+ -> Plenty
    """
    print(p.description())

    remaining_area = p.area()
    remaining_weight = p.weight()

    # Failure checks first (<= 0 in either dimension)
    failed = False
    if remaining_area <= 0:
        print("Your plate isn't big enough for this much food! Your food spills over the edge.")
        failed = True
    if remaining_weight <= 0:
        print("Your plate can't support this much weight! It buckles and spills.")
        failed = True
    if failed:
        return True

    # Weight hint -> "Sturdiness"
    if remaining_weight >= 13:
        sturdiness = "Strong"
    elif remaining_weight >= 7:
        sturdiness = "Weak"
    else:
        sturdiness = "Bending"

    # Area hint -> "Space available"
    if remaining_area >= 41:
        space = "Plenty"
    elif remaining_area >= 21:
        space = "Some"
    else:
        space = "A tiny bit"

    print(f"Sturdiness: {sturdiness}")
    print(f"Space available: {space}")
    return False


def main() -> None:
    """Run the Thanksgiving Dinner buffet game."""
    print("- Thanksgiving Dinner -")
    print("Serve yourself as much food as you")
    print("like from the buffet, but make sure")
    print("that your plate will hold without")
    print("spilling everywhere!")

    # Choose plate
    print("Choose a plate:")
    print("1. Small Sturdy Plate")
    print("2. Large Flimsy Plate")
    plate_choice = check_input.get_int_range("", 1, 2)

    plate: Plate = SmallPlate() if plate_choice == 1 else LargePlate()

    # Food menu mapping
    menu: Dict[int, Type[Plate]] = {
        1: Turkey,
        2: Stuffing,
        3: Potatoes,
        4: GreenBeans,
        5: Pie,
    }

    # Repeatedly add food until quit or failure
    while True:
        print("1. Turkey")
        print("2. Stuffing")
        print("3. Potatoes")
        print("4. Green Beans")
        print("5. Pie")
        print("6. Quit")
        choice = check_input.get_int_range("", 1, 6)

        if choice == 6:  # quit
            print(plate.description())
            print(f"Good job! You made it to the table with {plate.count()} items.")
            print(f"There was still {plate.area()} square inches left on your plate.")
            print(f"Your plate could have held {plate.weight()} more ounces of food.")
            print("Don't worry, you can always go back for more. Happy Thanksgiving!")
            break

        # Decorate the plate with the selected food
        plate = menu[choice](plate)

        # Examine after each addition; stop on failure
        if examine_plate(plate):
            break


if __name__ == "__main__":
    main()
