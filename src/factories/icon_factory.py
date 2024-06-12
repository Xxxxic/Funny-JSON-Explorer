from abc import ABC, abstractmethod
from icons.icon import PokerIcon
from icons.icon import ChessIcon
from icons.icon import OtherIcon


class IconFactory(ABC):
    @abstractmethod
    def create_icon(self) -> 'Icon':
        pass


class PokerIconFactory(IconFactory):
    def create_icon(self) -> 'Icon':
        return PokerIcon()


class ChessIconFactory(IconFactory):
    def create_icon(self) -> 'Icon':
        return ChessIcon()


class OtherIconFactory(IconFactory):
    def create_icon(self) -> 'Icon':
        return OtherIcon()
