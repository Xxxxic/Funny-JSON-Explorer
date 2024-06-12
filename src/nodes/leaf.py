from .node import Node
from icons.icon import Icon


class Leaf(Node):
    def __init__(self, icon: Icon, key: str, value: str) -> None:
        super().__init__(icon, key, value)
        self.icon = icon.leaf_icon
        self.value = value

    def render(self, style, prefix, max_width, is_last) -> list:
        rendered_line, _ = style.render_leaf(self.icon, self.key, self.value, prefix, max_width, is_last)
        return rendered_line
