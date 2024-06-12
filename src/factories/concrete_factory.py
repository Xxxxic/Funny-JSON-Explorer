# from .abstract_factory import AbstractFactory
# from src.components.container import Container
# from src.components.leaf import Leaf
# from src.styles.tree_style import TreeStyle
# from src.icons.icon import PokerIcon
#
#
# class ConcreteFactory1(AbstractFactory):
#     def create_container(self, key):
#         return Container(self.create_icon().container_icon, key)
#
#     def create_leaf(self, key, value):
#         return Leaf(self.create_icon().leaf_icon, key, value)
#
#     def create_style(self):
#         return TreeStyle()
#
#     def create_icon(self):
#         return PokerIcon()


from .abstract_factory import AbstractFactory
from src.components.container import Container
from src.components.leaf import Leaf
from src.styles.tree_style import TreeStyle
from src.styles.rectangle_style import RectangleStyle
from src.icons.icon import PokerIcon
from src.icons.icon import ChessIcon
from src.icons.icon import OtherIcon

class ConcreteFactory1(AbstractFactory):
    def create_container(self, key):
        return Container(self.create_icon().container_icon, key)

    def create_leaf(self, key, value):
        return Leaf(self.create_icon().leaf_icon, key, value)

    def create_style(self):
        return TreeStyle()

    def create_icon(self):
        return PokerIcon()

class ConcreteFactory2(AbstractFactory):
    def create_container(self, key):
        return Container(self.create_icon().container_icon, key)

    def create_leaf(self, key, value):
        return Leaf(self.create_icon().leaf_icon, key, value)

    def create_style(self):
        return RectangleStyle()

    def create_icon(self):
        return ChessIcon()

class CustomIconFactory(AbstractFactory):
    def __init__(self, config_path, icon_name):
        self.config_path = config_path
        self.icon_name = icon_name

    def create_container(self, key):
        return Container(self.create_icon().container_icon, key)

    def create_leaf(self, key, value):
        return Leaf(self.create_icon().leaf_icon, key, value)

    def create_style(self):
        raise NotImplementedError("CustomIconFactory does not implement create_style method.")

    def create_icon(self):
        icon = OtherIcon()
        icon.set_icons(self.config_path, self.icon_name)
        return icon
