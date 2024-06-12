from .abstract_factory import AbstractFactory
from src.components.container import Container
from src.components.leaf import Leaf
from src.styles.tree_style import TreeStyle
from src.icons.icon import PokerIcon


class ConcreteFactory1(AbstractFactory):
    def create_container(self, key):
        return Container(self.create_icon().container_icon, key)

    def create_leaf(self, key, value):
        return Leaf(self.create_icon().leaf_icon, key, value)

    def create_style(self):
        return TreeStyle()

    def create_icon(self):
        return PokerIcon()
