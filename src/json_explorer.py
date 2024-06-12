import json
from json_builder import JSONBuilder

class FunnyJsonExplorer:
    def __init__(self, factory):
        self.factory = factory

    # 将json数据转换为指定风格输出
    def show(self, json_data):
        builder = JSONBuilder(self.factory)
        root = builder.build(json_data)
        style = self.factory.create_style()
        print_list = root.draw(style, "", 80, True)
        beautified_list = style.beautification(print_list)
        for line in beautified_list:
            print(line)

    # 从json字符串中加载数据
    def _load(self, json_str):
        return json.loads(json_str)
