"""IceCubes class.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""
from src.fruit.IBlendable import IBlendable


class IceCubes(IBlendable):
    """IceCubes class."""

    def blend(self) -> None:
        """Blend method.

        Prints the result of blending this object.
        """
        print("Slush and snow")
