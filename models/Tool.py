class Tool:

    def __init__(self, id_tool=None, name=None):
        if id_tool is not None:
            self.id_tool = id_tool
        if name is not None:
            self.name = name

    def __repr__(self):
        return f"({self.id_tool}, {self.name})"

    def to_dict(self):
        return {"id": self.id_tool, "name": self.name}
