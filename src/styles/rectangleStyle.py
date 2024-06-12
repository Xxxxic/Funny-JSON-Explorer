from .style import Style


class RectangleStyle(Style):
    def render_container(self, icon: str, key: str, prefix: str, max_width: int, is_last: bool) \
            -> tuple[list[str], str]:
        connector = "├─"
        line = f"{connector}{icon}{key} {'─' * (max_width - len(prefix) - len(key) - len(connector) - 2)}" + "─┤"
        print_line = f"{prefix}{line}"
        extension = "│  "
        return [print_line], prefix + extension

    def render_leaf(self, icon: str, key: str, value: str, prefix: str, max_width: int, is_last: bool) \
            -> tuple[list[str], str]:
        connector = "├─"
        if value == 'None':
            line = f"{connector}{icon}{key} {'─' * (max_width - len(prefix) - len(key) - len(connector) - 2)}" + "─┤"
            print_line = f"{prefix}{line}"
        else:
            line = f"{connector}{icon}{key}: {value} {'─' * (max_width - len(prefix) - len(key) - len(connector) - len(value) - 4)}" + "─┤"
            print_line = f"{prefix}{line}"
        return [print_line], ''

    def render(self, print_list: list) -> list:
        new_print_list = []
        for index, l in enumerate(print_list):
            if index == 0:
                for i, s in enumerate(l):
                    if s == "├":
                        l = l[:i] + "┌─" + l[i + 2:]
                    elif s == "┤":
                        l = l[:i - 1] + "─┐" + l[i + 1:]
            elif index == len(print_list) - 1:
                for i, s in enumerate(l):
                    if i == 0 and s == "│":
                        l = l[:i] + "└─" + l[i + 2:]
                    elif s == "│" or s == "├":
                        l = l[:i - 1] + "─┴─" + l[i + 2:]
                    elif s == "┤":
                        l = l[:i - 1] + "─┘" + l[i + 1:]
            new_print_list.append(l)
        return new_print_list
