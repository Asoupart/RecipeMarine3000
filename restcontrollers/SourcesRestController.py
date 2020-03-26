import json
from flask import make_response, abort
from DAO import SourceDAOimpl
from models.Source import Source


def read_all():
    sources = []
    for source in SourceDAOimpl.findAll():
        sources.append(source.to_dict())
    json.dumps(sources)
    return sources


def read_one(id_src):
    return SourceDAOimpl.findOneById(id_src).to_dict()


def create(source):
    name = source.get("name", None)
    source = Source(None, name)
    SourceDAOimpl.insert(source)


def update(id_src, source):
    name = source.get("name", None)
    source = Source(id_src, name)
    SourceDAOimpl.update(source)


def delete(id_src):
    SourceDAOimpl.deleteById(id_src)
