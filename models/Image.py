class Image:

    def __init__(self, id_img=None, name=None, id_recipe=None):
        if id_img is not None:
            self.id_img = id_img
        if name is not None:
            self.name = name
        if id_recipe is not None:
            self.id_recipe = id_recipe

    def __repr__(self):
        return f"({self.id_img}, {self.name})"

    def to_dict(self):
        return {"id": self.id_img, "name": self.name, "id_recipe": self.id_recipe}
