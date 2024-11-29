"""Banana class.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""
from src.fruit.Fruit import Fruit
from src.fruit.IBlendable import IBlendable


class Banana(Fruit, IBlendable):
    """Banana class."""

    def blend(self) -> None:
        """Blend method.

        Prints the result of blending this object.
        """
        print("Yellow banana mush")

    @property
    def fruit_name(self) -> str:
        return "Banana"
