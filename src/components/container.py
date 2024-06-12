from .component import Component
from icons.icon import Icon


class Container(Component):
    def __init__(self, icon: Icon, key: str, value: str) -> None:
        super().__init__(icon, key, value)
        self.icon = icon.container_icon
        self.children = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def draw(self, style, prefix, max_width, is_last) -> list:
        print_list = []
        print_line, next_prefix = style.draw_container(self.icon, self.key, prefix, max_width, is_last)
        print_list += print_line
        for index, child in enumerate(self.children):
            is_last = index == len(self.children) - 1
            print_line = child.draw(style, next_prefix, max_width, is_last)
            print_list += print_line
        return print_list
