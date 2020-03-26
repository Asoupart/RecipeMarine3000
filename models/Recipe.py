class Recipe:

    def __init__(self, id_recipe=None, name=None, nbr_person=None, id_src=None):
        if id_recipe is not None:
            self.id_recipe = id_recipe
        if name is not None:
            self.name = name
        if nbr_person is not None:
            self.nbr_person = nbr_person
        if id_src is not None:
            self.id_src = id_src

    def __repr__(self):
        return f"({self.id_recipe}, {self.name}, {self.id_src})"

    def to_dict(self):
        return {"id": self.id_recipe, "name": self.name, "id_src": self.id_src}
