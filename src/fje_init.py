import json
import sys


def load_json(path):
    lines = []  # 第一步：定义一个列表， 打开文件
    with open(path) as f:
        for row in f.readlines():  # 第二步：读取文件内容
            if row.strip().startswith("//"):  # 第三步：对每一行进行过滤
                continue
            lines.append(row)  # 第四步：将过滤后的行添加到列表中.
    return json.loads("\n".join(lines))  # 将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！


# ├─♢oranges
# │  └─♢mandarin
# │     ├─♤clementine
# │     └─♤tangerine: cheap & juicy!
# └─♢apples
#    └─♤gala
def print_json_tree(data, indent='', is_last=True):
    """Print a JSON tree."""
    if isinstance(data, dict):
        size = len(data)
        for i, (key, value) in enumerate(data.items()):
            is_last_item = i == (size - 1)
            if is_last_item:
                print(f"{indent}└─ {key}")
                new_indent = indent + "    "
            else:
                print(f"{indent}├─ {key}")
                new_indent = indent + "│   "
            if value is None or not isinstance(value, (dict, list)):
                if value is not None:
                    print(f"{new_indent}{'└─ ' if is_last_item else '├─ '}{value}")
            else:
                print_json_tree(value, new_indent, is_last_item)
    elif isinstance(data, list):
        size = len(data)
        for i, value in enumerate(data):
            is_last_item = i == (size - 1)
            if is_last_item:
                print(f"{indent}└─ [{i}]")
                new_indent = indent + "    "
            else:
                print(f"{indent}├─ [{i}]")
                new_indent = indent + "│   "
            if value is None or not isinstance(value, (dict, list)):
                if value is not None:
                    print(f"{new_indent}{'└─ ' if is_last_item else '├─ '}{value}")
            else:
                print_json_tree(value, new_indent, is_last_item)


# ┌─ oranges ───────────────────────────────┐
# │  ├─ mandarin ───────────────────────────┤
# │  │  ├─ clementine ──────────────────────┤
# │  │  ├─ tangerine: cheap & juicy! ───────┤
# ├─ apples ────────────────────────────────┤
# └──┴─ gala ───────────────────────────────┘

# def print_rectangle_style(data, indent=''):
#     """Print JSON in rectangle style."""
#
#     def print_border(content, is_last=False):
#         if is_last:
#             print(f"{indent}└─ {content} ─{'─' * (40 - len(content))}┘")
#         else:
#             print(f"{indent}├─ {content} ─{'─' * (40 - len(content))}┤")
#
#     if isinstance(data, dict):
#         size = len(data)
#         for i, (key, value) in enumerate(data.items()):
#             is_last_item = i == (size - 1)
#             print_border(key, is_last_item)
#             if isinstance(value, dict) or isinstance(value, list):
#                 print_rectangle_style(value, indent + "│  ")
#             else:
#                 if value is not None:
#                     print_border(f"{key}: {value}", is_last_item)
#     elif isinstance(data, list):
#         size = len(data)
#         for i, value in enumerate(data):
#             is_last_item = i == (size - 1)
#             print_border(f"[{i}]", is_last_item)
#             if isinstance(value, dict) or isinstance(value, list):
#                 print_rectangle_style(value, indent + "│  ")
#             else:
#                 if value is not None:
#                     print_border(f"[{i}]: {value}", is_last_item)


def get_max_length(data, indent=0):
    """Get the maximum length of the keys and values in the JSON structure."""
    max_len = 0
    if isinstance(data, dict):
        for key, value in data.items():
            max_len = max(max_len, indent + len(key) + 2)
            if isinstance(value, (dict, list)):
                max_len = max(max_len, get_max_length(value, indent + 4))
            elif value is not None:
                max_len = max(max_len, indent + len(f"{key}: {value}") + 2)
    elif isinstance(data, list):
        for i, value in enumerate(data):
            max_len = max(max_len, indent + len(f"[{i}]") + 2)
            if isinstance(value, (dict, list)):
                max_len = max(max_len, get_max_length(value, indent + 4))
            elif value is not None:
                max_len = max(max_len, indent + len(f"[{i}]: {value}") + 2)
    return max_len


# def print_rectangle_style(data, indent='', max_len=0):
#     """Print JSON in rectangle style."""
#
#     def print_border(content, is_last=False, is_top=False, is_bottom=False, is_leaf=False):
#         if is_top:
#             border = f"{indent}┌─ {content} "
#             filler = '─' * (max_len - len(border))
#             print(f"{border}{filler}┐")
#         elif is_bottom:
#             border = f"{indent}└─ {content} "
#             filler = '─' * (max_len - len(border))
#             print(f"{border}{filler}┘")
#         elif is_leaf:
#             border = f"{indent}├─ {content} "
#             filler = '─' * (max_len - len(border))
#             print(f"{border}{filler}┤")
#         elif is_last:
#             border = f"{indent}└─ {content} "
#             filler = '─' * (max_len - len(border))
#             print(f"{border}{filler}┤")
#         else:
#             border = f"{indent}│  {content} "
#             filler = ' ' * (max_len - len(border))
#             print(f"{border}{filler}│")
#
#     # 单个节点
#     if isinstance(data, dict):
#         size = len(data)
#         for i, (key, value) in enumerate(data.items()):
#             is_last_item = i == (size - 1)
#             is_leaf = not isinstance(value, (dict, list))
#             if i == 0:
#                 print_border(key, is_last_item, is_top=True)
#             else:
#                 print_border(key, is_last_item, is_leaf=is_leaf)
#             if isinstance(value, (dict, list)):
#                 print_rectangle_style(value, indent + "│  ", max_len)
#             elif value is not None:
#                 print_border(f"{key}: {value}", is_last_item)
#         if size == 0:
#             print_border('', is_last=True, is_bottom=True)
#     # 列表节点
#     elif isinstance(data, list):
#         size = len(data)
#         for i, value in enumerate(data):
#             is_last_item = i == (size - 1)
#             is_leaf = not isinstance(value, (dict, list))
#             print_border(f"[{i}]", is_last_item, is_leaf=is_leaf)
#             if isinstance(value, (dict, list)):
#                 print_rectangle_style(value, indent + "│  ", max_len)
#             elif value is not None:
#                 print_border(f"[{i}]: {value}", is_last_item)
#         if size == 0:
#             print_border('', is_last=True, is_bottom=True)


def print_rectangle_style(data, indent='', max_len=0, is_last=False):
    """Print JSON in rectangle style."""

    def print_border(content, is_last=False, is_top=False, is_bottom=False, is_leaf=False):
        if is_top:
            border = f"{indent}┌─ {content} "
            filler = '─' * (max_len - len(border))
            print(f"{border}{filler}┐")
        elif is_bottom:
            border = f"{indent}└─ {content} "
            filler = '─' * (max_len - len(border))
            print(f"{border}{filler}┘")
        elif is_leaf:
            border = f"{indent}├─ {content} "
            filler = '─' * (max_len - len(border))
            print(f"{border}{filler}┤")
        elif is_last:
            border = f"{indent}└─ {content} "
            filler = '─' * (max_len - len(border))
            print(f"{border}{filler}┤")
        else:
            border = f"{indent}│  {content} "
            filler = ' ' * (max_len - len(border))
            print(f"{border}{filler}│")

    if isinstance(data, dict):
        size = len(data)
        for i, (key, value) in enumerate(data.items()):
            is_last_item = i == (size - 1)
            is_leaf = not isinstance(value, (dict, list))
            if i == 0:
                print_border(key, is_top=True)
            else:
                print_border(key, is_leaf=is_leaf)
            if isinstance(value, (dict, list)):
                print_rectangle_style(value, indent + "│  ", max_len, is_last=is_last_item and is_last)
            elif value is not None:
                print_border(f"{key}: {value}")
        if size == 0:
            print_border('', is_last=True, is_bottom=True)
    elif isinstance(data, list):
        size = len(data)
        for i, value in enumerate(data):
            is_last_item = i == (size - 1)
            is_leaf = not isinstance(value, (dict, list))
            print_border(f"[{i}]", is_leaf=is_leaf)
            if isinstance(value, (dict, list)):
                print_rectangle_style(value, indent + "│  ", max_len, is_last=is_last_item and is_last)
            elif value is not None:
                print_border(f"[{i}]: {value}")
        if size == 0:
            print_border('', is_last=True, is_bottom=True)


if __name__ == "__main__":
    json_string = "./test.json"

    try:
        json_data = load_json(json_string)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(1)

    print(json_data)

    # print_json_tree(json_data)
    max_len = get_max_length(json_data, 5)
    # print(max_len)
    print_rectangle_style(json_data, max_len=max_len)
