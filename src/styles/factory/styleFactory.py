from abc import ABC, abstractmethod

from ..rectangleStyle import RectangleStyle
from ..style import Style
from ..treeStyle import TreeStyle


class StyleFactory(ABC):
    @abstractmethod
    def create_style(self) -> 'Style':
        pass


class TreeStyleFactory(StyleFactory):
    def create_style(self) -> 'Style':
        return TreeStyle()


class RectangleStyleFactory(StyleFactory):
    def create_style(self) -> 'Style':
        return RectangleStyle()
