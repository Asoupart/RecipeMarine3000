import json
import configparser
import os
from flask import make_response, abort
from DAO import ImageDAOImpl
from models.Image import Image


config_api = configparser.ConfigParser()
config_api.read('config.ini')
folder = config_api['UPLOAD_FOLDER']['Folder']


def read_all():
    images = []
    for image in ImageDAOImpl.findAll():
        images.append(image.to_dict())
    json.dumps(images)
    return images


def read_by_recipe(id_recipe):
    images = []
    for image in ImageDAOImpl.findByRecipe(id_recipe):
        images.append(image.to_dict())
    json.dumps(images)
    return images


def read_one(id_img):
    return ImageDAOImpl.findOneById(id_img).to_dict()


def create(image):
    name = image.get("name", None)
    id_recipe = image.get("id_recipe", None)
    image = Image(None, name, id_recipe)
    id_img = ImageDAOImpl.insert(image)
    json.dumps(id_img)
    return id_img


def update(id_img, image):
    name = image.get("name", None)
    id_recipe = image.get("id_recipe", None)
    image = Image(id_img, name, id_recipe)
    ImageDAOImpl.update(image)


def delete(id_img):
    image = ImageDAOImpl.findOneById(id_img)
    if os.path.exists(folder + image.name):
        os.remove(folder + image.name)
    ImageDAOImpl.deleteById(id_img)

