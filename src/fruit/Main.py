"""Sample Inheritance Program.

This is a sample program to demonstrate
inheritance, interfaces, and polymorphism.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""
from typing import List
from src.fruit.Apple import Apple
from src.fruit.Banana import Banana
from src.fruit.CellPhone import CellPhone
from src.fruit.ConcreteBlock import ConcreteBlock
from src.fruit.Fruit import Fruit
from src.fruit.IBlendable import IBlendable
from src.fruit.IceCubes import IceCubes
from src.fruit.OldBanana import OldBanana
from src.fruit.Mango import Mango
from src.fruit.Strawberry import Strawberry


class Main:
    """Simple Main Class."""
    @staticmethod
    def main(args: List[str]) -> None:
        """Main method for the program to test features.

        Args:
            args: The command-line arguments provided to the program.
        """
        #Duck Typing
        ducklist: List[object] = list()
        ducklist.append(Banana())
        ducklist.append(CellPhone())
        #ducklist.append(ConcreteBlock())
        ducklist.append(IceCubes())
        ducklist.append(Mango())
        ducklist.append(Strawberry())

        for obj in ducklist:
            obj.blend() # type: ignore

        # Shared Superclass
        fruitlist: List[Fruit] = list()
        fruitlist.append(Apple())
        fruitlist.append(Banana())
        fruitlist.append(Mango())
        fruitlist.append(Strawberry())
        #fruitlist.append(Fruit())

        print("Fruit list ===========")
        for f in fruitlist:
            print(f.fruit_name + " : ", end = '')
            f.blend()

        # Shared Interface
        blendlist: List[IBlendable] = list()
        blendlist.append(Apple())
        blendlist.append(Banana())
        blendlist.append(OldBanana())
        blendlist.append(CellPhone())
        blendlist.append(IceCubes())
        blendlist.append(Mango())
        blendlist.append(Strawberry())

        print("Blend list ============")
        for b in blendlist:
            if isinstance(b, Fruit):
                print(b.fruit_name + " : ", end = '')
            b.blend()
