"""Fruit class.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""
from abc import ABC, abstractmethod

class Fruit(ABC):
    """Fruit class."""

    @property
    @abstractmethod
    def fruit_name(self) -> str:
        raise NotImplementedError