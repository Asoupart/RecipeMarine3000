class Source:

    def __init__(self, id_src=None, name=None):
        if id_src is not None:
            self.id_src = id_src
        if name is not None:
            self.name = name

    def __repr__(self):
        return f"({self.id_src}, {self.name})"

    def to_dict(self):
        return {"id": self.id_src, "name": self.name}
