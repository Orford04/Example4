"""Mango class.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""
from src.fruit.Fruit import Fruit
from src.fruit.IBlendable import IBlendable


class Mango(Fruit, IBlendable):
    """Mango class."""

    def blend(self) -> None:
        """Blend method.

        Prints the result of blending this object.
        """
        print("Strange mangoey orange goop")

    @property
    def fruit_name(self) -> str:
        return "Mango"
