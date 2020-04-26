class Category:

    def __init__(self, id_cat=None, name=None):
        if id_cat is not None:
            self.id_cat = id_cat
        if name is not None:
            self.name = name

    def __repr__(self):
        return f"({self.id_cat}, {self.name})"

    def to_dict(self):
        return {"id": self.id_cat, "name": self.name}