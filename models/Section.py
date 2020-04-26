class Section:

    def __init__(self, id_sec=None, name=None, id_recipe=None):
        if id_sec is not None:
            self.id_sec = id_sec
        if name is not None:
            self.name = name
        if id_recipe is not None:
            self.id_recipe = id_recipe

    def __repr__(self):
        return f"({self.id_sec}, {self.name})"

    def to_dict(self):
        return {"id": self.id_sec, "name": self.name, "id_recipe": self.id_recipe}


