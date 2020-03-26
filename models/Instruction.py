class Instruction:

    def __init__(self, id_ins=None, text_ins=None, id_section = None):
        if id_ins is not None:
            self.id_ins = id_ins
        if text_ins is not None:
            self.text_ins = text_ins
        if id_section is not None:
            self.id_section = id_section

    def __repr__(self):
        return f"({self.id_ins}, {self.text_ins})"

    def to_dict(self):
        return {"id": self.id_ins, "text": self.text, "id_section": self.id_section}