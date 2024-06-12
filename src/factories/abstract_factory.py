from abc import ABC, abstractmethod
# from ..components.container import Container
# from ..components.leaf import Leaf
# from ..styles.style import Style
# from ..icons.icon import Icon


# 抽象工厂类
class AbstractFactory(ABC):
    @abstractmethod
    def create_container(self, key):
        pass

    @abstractmethod
    def create_leaf(self, key, value):
        pass

    @abstractmethod
    def create_style(self):
        pass

    @abstractmethod
    def create_icon(self):
        pass
