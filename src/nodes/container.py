from .node import Node
from icons.icon import Icon
from .iterator import Iterator


class Container(Node):
    def __init__(self, icon: Icon, key: str, value: str) -> None:
        super().__init__(icon, key, value)
        self.icon = icon.container_icon
        self.children = []

    def add_child(self, node: Node) -> None:
        self.children.append(node)

    def render(self, style, prefix, max_width, is_last) -> list:
        rendered_lines = []
        rendered_line, next_prefix = style.render_container(self.icon, self.key, prefix, max_width, is_last)
        rendered_lines += rendered_line
        for index, child in enumerate(self.children):
            is_last_child = index == len(self.children) - 1
            rendered_line = child.render(style, next_prefix, max_width, is_last_child)
            rendered_lines += rendered_line
        return rendered_lines

    def create_iterator(self):
        return ContainerIterator(self)

    def accept(self, visitor):
        visitor.visit_container(self)


class ContainerIterator(Iterator):
    def __init__(self, container):
        self._container = container
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._container.children)

    def next(self):
        if self.has_next():
            item = self._container.children[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
