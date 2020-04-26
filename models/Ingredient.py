class Ingredient:

    def __init__(self, id_ing=None, name=None):
        if id_ing is not None:
            self.id_ing = id_ing
        if name is not None:
            self.name = name

    def __repr__(self):
        return f"({self.id_ing}, {self.name})"

    def to_dict(self):
        return {"id": self.id_ing, "name": self.name}
