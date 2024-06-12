from abc import ABC, abstractmethod


class Style(ABC):
    # 根据参数打印container节点
    @abstractmethod
    def render_container(self, icon, key, prefix, max_width, is_last):
        pass

    # 根据参数打印leaf节点
    @abstractmethod
    def render_leaf(self, icon, key, value, prefix, max_width, is_last):
        pass

    # 根据给定的列表打印
    @abstractmethod
    def render(self, print_list):
        pass
