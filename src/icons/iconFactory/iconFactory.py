from abc import ABC, abstractmethod
from ..icon import Icon


class IconFactory(ABC):
    def create_icon(self) -> 'Icon':
        return Icon()