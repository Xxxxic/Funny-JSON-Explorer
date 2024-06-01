import json
import Container


class FunnyJsonExplorer:
    def __init__(self, json_string):
        try:
            self.json_data = json.loads(json_string)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            sys.exit(1)

    def show(self, style):
        if style == 'tree':
            Container(self.json_data).draw_tree()
        elif style == 'rectangle':
            Container(self.json_data).draw_rectangle()
        else:
            print("Unknown style. Available styles: tree, rectangle")
            sys.exit(1)

    def load_json(path):
        lines = []  # 第一步：定义一个列表， 打开文件
        with open(path) as f:
            for row in f.readlines():  # 第二步：读取文件内容
                if row.strip().startswith("//"):  # 第三步：对每一行进行过滤
                    continue
                lines.append(row)  # 第四步：将过滤后的行添加到列表中.
        return json.loads("\n".join(lines))  # 将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！
