from abc import ABC, abstractmethod
from styles.style import Style
from icons.icon import Icon


class Component(ABC):
    def __init__(self, icon: Icon, key: str, value: str) -> None:
        self.icon = str()
        self.key = key

    @abstractmethod
    def draw(self, style: Style, prefix: str, max_width: int, is_last: bool) -> list:
        pass
