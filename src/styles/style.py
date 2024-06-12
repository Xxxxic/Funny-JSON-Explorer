from abc import ABC, abstractmethod


class Style(ABC):
    @abstractmethod
    def draw_container(self, icon, key, prefix, max_width, is_last):
        pass

    @abstractmethod
    def draw_leaf(self, icon, key, value, prefix, max_width, is_last):
        pass

    @abstractmethod
    def beautification(self, print_list):
        pass
