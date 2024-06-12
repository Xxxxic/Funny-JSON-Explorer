from .component import Component


class Container(Component):
    def __init__(self, icon, key):
        super().__init__(icon, key)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self, style, prefix, max_width, is_last):
        print_list = []
        print_line, next_prefix = style.draw_container(self.icon, self.key, prefix, max_width, is_last)
        print_list += print_line
        for index, child in enumerate(self.children):
            is_last_child = index == len(self.children) - 1
            print_list += child.draw(style, next_prefix, max_width, is_last_child)
        return print_list
