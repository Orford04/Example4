"""Strawberry class.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""
from src.fruit.Fruit import Fruit
from src.fruit.IBlendable import IBlendable


class Strawberry(Fruit, IBlendable):
    """Strawberry class."""

    def blend(self) -> None:
        """Blend method.

        Prints the result of blending this object.
        """
        print("Sweet red strawberry goodness")

    @property
    def fruit_name(self) -> str:
        return "Strawberry"