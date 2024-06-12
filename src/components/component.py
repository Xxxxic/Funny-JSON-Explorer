from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, icon, key, value=None):
        self.icon = icon
        self.key = key
        self.value = value

    @abstractmethod
    def draw(self, style, prefix, max_width, is_last):
        pass
