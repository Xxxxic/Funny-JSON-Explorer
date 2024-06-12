from .style import Style


class TreeStyle(Style):
    def draw_container(self, icon, key, prefix, max_width, is_last):
        connector = "└─" if is_last else "├─"
        print_line = f"{prefix}{connector}{icon}{key}"
        extension = "   " if is_last else "│  "
        return [print_line], prefix + extension

    def draw_leaf(self, icon, key, value, prefix, max_width, is_last):
        connector = "└─" if is_last else "├─"
        if value is None:
            print_line = f"{prefix}{connector}{icon}{key}"
        else:
            print_line = f"{prefix}{connector}{icon}{key}: {value}"
        return [print_line], ''

    def beautification(self, print_list):
        return print_list
