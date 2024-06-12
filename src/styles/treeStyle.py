from .style import Style


class TreeStyle(Style):
    def render_container(self, icon: str, key: str, prefix: str, max_width: int, is_last: bool) \
            -> tuple[list[str], str]:
        connector = "└─" if is_last else "├─"
        print_line = f"{prefix}{connector}{icon}{key}"
        extension = "   " if is_last else "│  "
        return [print_line], prefix + extension

    def render_leaf(self, icon: str, key: str, value: str, prefix: str, max_width: int, is_last: bool) \
            -> tuple[list[str], str]:
        connector = "└─" if is_last else "├─"
        if value == 'None':
            print_line = f"{prefix}{connector}{icon}{key}"
        else:
            print_line = f"{prefix}{connector}{icon}{key}: {value}"
        return [print_line], ''

    def render(self, print_list: list) -> list:
        return print_list
