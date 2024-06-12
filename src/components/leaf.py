from .component import Component
from icons.icon import Icon


class Leaf(Component):
    def __init__(self, icon: Icon, key: str, value: str) -> None:
        super().__init__(icon, key, value)
        self.icon = icon.leaf_icon
        self.value = value

    def draw(self, style, prefix, max_width, is_last) -> list:
        print_line, _ = style.draw_leaf(self.icon, self.key, self.value, prefix, max_width, is_last)
        return print_line
