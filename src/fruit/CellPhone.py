"""CellPhone class.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""
from src.fruit.IBlendable import IBlendable


class CellPhone(IBlendable):
    """CellPhone class."""

    def blend(self) -> None:
        """Blend method.

        Prints the result of blending this object.
        """
        print("Cell phone dust and dangerous chemicals - don't breathe this!")
