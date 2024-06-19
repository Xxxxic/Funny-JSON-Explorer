import json

from icons.iconFactory.iconFactory import IconFactory
from styles.factory.styleFactory import TreeStyleFactory, RectangleStyleFactory
from nodes.container import Container
from nodes.leaf import Leaf
from nodes.visitor import StyleVisitor


class FunnyJsonExplorer:
    def __init__(self, style: str, icon: str, config: str = None):
        self.json_data = None
        self.style = get_style_factory(style).create_style()
        self.icon = get_icon_factory().create_icon()
        self.icon.set_icons(config_path=config, icon_name=icon)
        self.max_width = 0
        self.root = None
        self.print_list = []

    def _load(self, file_name):
        with open(file_name, 'r') as json_file:
            self.json_data = json.load(json_file)

    def get_max_width(self, data, level=0):
        if isinstance(data, dict):
            max_width = max([len(key) + self.get_max_width(value, level + 1) for key, value in data.items()], default=0)
            return max_width + 4
        elif isinstance(data, list):
            max_width = max([self.get_max_width(item, level + 1) for item in data], default=0)
            return max_width + 4
        elif isinstance(data, str):
            return len(data) + 4
        return 0

    def parse_json(self, data):
        if isinstance(data, dict):
            container = Container(self.icon, '', '')
            for key, value in data.items():
                child = self.parse_json(value)
                child.key = key
                container.add_child(child)
            return container
        else:
            return Leaf(self.icon, "", str(data))

    # def build(self):
    #     self.max_width = self.get_max_width(self.json_data)
    #     self.root = self.parse_json(self.json_data)
    #     print_list = []
    #     for index, child in enumerate(self.root.children):
    #         is_last = index == len(self.root.children) - 1
    #         print_line = child.render(self.style, "", self.max_width, is_last)
    #         print_list += print_line
    #     self.print_list = self.style.render(print_list)

    # 修改为迭代器模式
    # def build(self):
    #     self.max_width = self.get_max_width(self.json_data)
    #     self.root = self.parse_json(self.json_data)
    #     print_list = []
    #
    #     # 使用 iterator 去遍历树节点和渲染
    #     iterator = self.root.create_iterator()
    #     while iterator.has_next():
    #         node = iterator.next()
    #         if isinstance(node, Container):
    #             is_last = not iterator.has_next()  # Determine if current container is the last one
    #             print_line = node.render(self.style, "", self.max_width, is_last)
    #             print_list += print_line
    #         else:
    #             print_line = node.render(self.style, "", self.max_width, True)
    #             print_list += print_line
    #
    #     self.print_list = self.style.render(print_list)

    # 迭代器模式 + 访问者模式
    def build(self):
        self.max_width = self.get_max_width(self.json_data)
        self.root = self.parse_json(self.json_data)

        # 创建访问者实例
        visitor = StyleVisitor(self.style, self.max_width)
        # 使用访问者遍历和渲染节点
        self.root.accept(visitor)

        self.print_list = visitor.get_print_list()
        self.print_list = self.style.render(self.print_list)

    def show(self):
        for line in self.print_list:
            print(line)


def get_style_factory(style: str):
    if style == "tree":
        return TreeStyleFactory()
    elif style == "rectangle":
        return RectangleStyleFactory()
    else:
        raise ValueError(f"Unknown style: {style}")


def get_icon_factory():
    return IconFactory()
