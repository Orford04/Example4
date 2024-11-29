"""IBlendable class.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""
from abc import ABC, abstractmethod
from typing import List


class IBlendable(ABC):
    """IBlendable class."""

    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        if cls is IBlendable:
            attr: List[str] = []
            callables: List[str] = ['blend']
            ret = True
            for call in callables:
                ret = ret and (hasattr(subclass, call) and
                                callable(getattr(subclass, call)))
            return ret
        else:
            return NotImplemented

    @abstractmethod
    def blend(self) -> None:
        raise NotImplementedError