from abc import ABC, abstractmethod
from styles.style import Style
from icons.icon import Icon


class Node(ABC):

    def __init__(self, icon: Icon, key: str, value: str) -> None:
        self.icon = str()
        self.key = key

    @abstractmethod
    def render(self, style: Style, prefix: str, max_width: int, is_last: bool) -> list:
        pass

    @abstractmethod
    def create_iterator(self):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass
