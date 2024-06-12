from .style import Style
from typing import Union

VERTICAL = "│"
HORIZONTAL = "─"
TEE = "├─"
ELBOW = "└─"


class TreeStyle(Style):
    def draw_container(self, icon: str, key: str, prefix: str, max_width: int, is_last: bool) -> Union[list, str]:
        connector = ELBOW if is_last else TEE
        print_line = f"{prefix}{connector}{icon}{key}"
        extension = "   " if is_last else f"{VERTICAL}  "
        return [print_line], prefix + extension

    def draw_leaf(self, icon: str, key: str, value: str, prefix: str, max_width: int, is_last: bool) -> Union[
        list, str]:
        connector = ELBOW if is_last else TEE
        if value == 'None':
            print_line = f"{prefix}{connector}{icon}{key}"
        else:
            print_line = f"{prefix}{connector}{icon}{key}: {value}"
        return [print_line], ''

    def beautification(self, print_list: list) -> list:
        return print_list
