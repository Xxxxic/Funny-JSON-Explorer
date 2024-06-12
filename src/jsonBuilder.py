class JSONBuilder:
    def __init__(self, factory):
        self.factory = factory

    # build 出工厂对象
    def build(self, data, name="root"):
        if isinstance(data, dict):
            container = self.factory.create_container(name)
            for key, value in data.items():
                child = self.build(value, key)
                container.add_child(child)
            return container
        elif isinstance(data, list):
            container = self.factory.create_container(name)
            for i, value in enumerate(data):
                child = self.build(value, str(i))
                container.add_child(child)
            return container
        else:
            return self.factory.create_leaf(name, data)
