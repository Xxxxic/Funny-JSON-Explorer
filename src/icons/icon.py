from abc import ABC, abstractmethod


# 图标类
class Icon(ABC):
    def __init__(self):
        self.container_icon = None
        self.leaf_icon = None

    @abstractmethod
    def set_icons(self, config_path=None, icon_name=None):
        pass


class PokerIcon(Icon):
    def __init__(self):
        super().__init__()
        self.set_icons()

    def set_icons(self, config_path=None, icon_name=None):
        self.container_icon = '♢'
        self.leaf_icon = '♧'

