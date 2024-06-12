from .component import Component


class Leaf(Component):
    def draw(self, style, prefix, max_width, is_last):
        print_line, _ = style.draw_leaf(self.icon, self.key, self.value, prefix, max_width, is_last)
        return print_line
