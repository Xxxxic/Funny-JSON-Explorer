# nodes/visitor.py
from abc import ABC, abstractmethod
from .container import Container
from .leaf import Leaf


class Visitor(ABC):
    @abstractmethod
    def visit_container(self, container: Container):
        pass

    @abstractmethod
    def visit_leaf(self, leaf: Leaf):
        pass


class StyleVisitor(Visitor):
    def __init__(self, style, max_width):
        self.style = style
        self.max_width = max_width
        self.print_list = []

    def visit_container(self, container: Container):
        is_last = True
        iterator = container.create_iterator()
        while iterator.has_next():
            node = iterator.next()
            if isinstance(node, Container) and iterator.has_next():
                is_last = False
            print_line = node.render(self.style, "", self.max_width, is_last)
            self.print_list += print_line

    def visit_leaf(self, leaf: Leaf):
        print_line = leaf.render(self.style, "", self.max_width, True)
        self.print_list += print_line

    def get_print_list(self):
        return self.print_list
