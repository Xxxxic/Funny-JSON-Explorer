from abc import ABC, abstractmethod
from styles.tree_style import TreeStyle
from styles.rectangle_style import RectangleStyle

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
