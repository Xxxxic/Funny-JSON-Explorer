import json
from abc import ABC, abstractmethod


# 图标类
class Icon(ABC):
    def __init__(self):
        self.container_icon = None
        self.leaf_icon = None

    def set_icons(self, config_path=None, icon_name=None):
        if config_path is not None:
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)
            try:
                self.container_icon = config[icon_name]["container_icon"]
                self.leaf_icon = config[icon_name]["leaf_icon"]
            except:
                raise ValueError(f"Unknown icon: {icon_name}")
        else:
            raise ValueError(f'Config path missed.')
