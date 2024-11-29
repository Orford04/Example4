"""OldBanana class.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""
from src.fruit.Banana import Banana


class OldBanana(Banana):
    """OldBanana class."""

    def blend(self) -> None:
        """Blend method.

        Prints the result of blending this object.
        """
        print("Brown banana mush")