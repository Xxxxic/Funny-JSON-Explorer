from .node import Node
from icons.icon import Icon
from .iterator import Iterator


class Leaf(Node):
    def __init__(self, icon: Icon, key: str, value: str) -> None:
        super().__init__(icon, key, value)
        self.icon = icon.leaf_icon
        self.value = value

    def render(self, style, prefix, max_width, is_last) -> list:
        rendered_line, _ = style.render_leaf(self.icon, self.key, self.value, prefix, max_width, is_last)
        return rendered_line

    def create_iterator(self):
        return LeafIterator(self)

    def accept(self, visitor):
        visitor.visit_leaf(self)


class LeafIterator(Iterator):
    def __init__(self, leaf: Leaf):
        self._leaf = leaf
        self._visited = False

    def has_next(self) -> bool:
        return not self._visited

    def next(self):
        if not self._visited:
            self._visited = True
            return self._leaf
        else:
            raise StopIteration
